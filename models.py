import os
import re
import unicodedata
from typing import List

from settings import (
    FLAG_DIR,
    IMG_ROOT,
    SITE_DIR,
    Games,
    attrs_icon_data,
    domain_to_image,
    image_data,
)


def slugify(value: str) -> str:
    """
    Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


class Icon:
    def __init__(self, icon: str, label: str):
        self.icon = icon
        self.label = label


link_regex = re.compile(r"\[\[[^].]+\]\]")
quote_regex = re.compile(r"`[^`]+`")


class Mod:
    def __init__(
        self,
        name,
        categories,
        urls,
        notes,
        description,
        team,
        games,
        safe,
        translation_state,
        languages,
        authors,
        status,
        last_update,
        tp2,
    ):
        self.name = name
        self.categories = categories
        self.urls = urls
        self._notes = notes
        self.safe = safe
        self._description = description
        self.team = team
        self._games = games
        self.translation_state = translation_state
        self.languages = languages
        self.authors = authors
        self.status = status
        self.last_update = last_update
        self.tp2 = tp2

    @property
    def id(self) -> str:
        return slugify(self.name)

    @property
    def is_weidu(self) -> bool:
        return self.tp2 != "non-weidu"

    @property
    def urls_instance(self) -> list:
        return [Url(url) for url in self.urls]

    @property
    def icons(self) -> List[Icon]:
        icons = list()
        for attr, data_icons in attrs_icon_data.items():
            value = getattr(self, attr)
            for k, v in data_icons.items():
                if value in k:
                    data_icon = v
                    break
            else:
                raise ValueError(f"icon not found for {self.name}")
            icons.append(Icon(**data_icon))

        return icons

    def _convert_quote(self, txt: str) -> str:
        quoted_txt = txt
        for quote in quote_regex.findall(quoted_txt):
            quoted_txt = quoted_txt.replace(
                quote, f'<span class="quote">{quote.strip("`")}</span>'
            )

        return quoted_txt

    def _convert_link(self, txt: str) -> str:
        linked_txt = txt
        for link in link_regex.findall(txt):
            mod_name = link.strip("[] ")
            linked_txt = linked_txt.replace(
                link, f'<a href="#{slugify(mod_name)}">{mod_name}</a>'
            )

        return linked_txt

    def _convert_pipe(self, txt: str) -> str:
        return txt.replace("|", "<br/>")

    @property
    def description(self) -> str:
        description = self._convert_link(self._description)
        description = self._convert_pipe(description)
        return self._convert_quote(description)

    @property
    def safe_note(self) -> int:
        note = 2
        if self.is_outdated:
            note -= 1
        if not self.is_weidu:
            note -= 1
        if "temnix" in self.authors:  # déso
            note -= 1
        if self.status == "archived":
            note -= 1
        elif self.status in {"embed", "obsolete"}:
            note = 0
        elif self.status in {"wip", "missing"}:
            note = min(1, note)
        return max(0, note)

    @property
    def is_EE(self) -> bool:
        return bool(set(self.games) & set(Games.BG_EE()))

    @property
    def is_outdated(self) -> bool:
        return bool(
            self.last_update
            and (
                self.last_update < "2007-01"
                or (self.last_update < "2019-01" and self.is_EE)
            )
        )

    def get_auto_notes(self) -> list:
        auto_notes = list()
        if self.is_outdated and self.safe <= 1:
            year, _ = self.last_update.split("-")
            if self.is_EE:
                auto_notes.append(
                    f"⚠️ EE : La dernière mise à jour date de {year}. Ce mod pourrait ne pas fonctionner avec la dernière version du jeu."
                )
            else:
                auto_notes.append(f"⚠️ : La dernière mise à jour date de {year}.")

        if not self.is_weidu:
            auto_notes.append(
                "⚠️ WeiDU : Ce mod écrase les fichiers et ne peut être désinstallé. Installez-le à vos risques et périls."
            )
        if self.status == "archived":
            auto_notes.append(
                "Ce mod a été archivé par son auteur qui ne semble pas vouloir lui donner suite."
            )
        return auto_notes

    @property
    def notes(self) -> list:
        notes = list()
        for note in self._notes + self.get_auto_notes():
            new_note = self._convert_link(note)
            new_note = self._convert_pipe(new_note)
            new_note = self._convert_quote(new_note)
            notes.append(new_note)
        return notes

    @property
    def games(self) -> list:
        return [game for game in Games if game in self._games]


class Category:
    def __init__(self, name: str):
        self.name = name
        self.mods = list()

    @property
    def id(self) -> str:
        return slugify(self.name)


domain_regex = re.compile(r"https?://(www\.)?(?P<domain>[^/]*).*")


class Url:
    country_image_suffix = "-flag-32.png"

    def __init__(self, url):
        self.url = url
        self.img = None

        img = self.get_image_name()
        if img:
            # cas spécial pour les drapeaux
            if img.endswith(self.country_image_suffix):
                img_data = image_data[self.country_image_suffix].copy()
                img_data["title"] = img_data["title"] % img.removesuffix(
                    self.country_image_suffix
                )
                dir = FLAG_DIR
            else:
                img_data = image_data.get(
                    img, dict(title="titre de l'image", width=32, height=32)
                )
                dir = SITE_DIR

            img_dir = os.path.join("img", dir, img)
            self.img = Image(src=img_dir, **img_data)

    def get_image_special(self) -> str:
        domain = self.get_domain()
        img = domain_to_image.get(domain, "")

        # check sous-domaine
        if not img and domain.count(".") >= 2:
            domain = domain.partition(".")[-1]
            img = domain_to_image.get(domain, "")

        return img

    def get_tld(self) -> str:
        return self.get_domain().rpartition(".")[-1]

    def get_image_country(self) -> str:
        country_img = f"{self.get_tld()}-flag-32.png"
        img = ""
        # auto-select
        if os.path.exists(os.path.join(IMG_ROOT, FLAG_DIR, country_img)):
            img = country_img

        return img

    def get_image_name(self) -> str:
        return self.get_image_special() or self.get_image_country()

    def get_domain(self) -> str:
        domain = domain_regex.search(self.url).group("domain")
        return domain or "localhost"

    @property
    def is_external(self) -> bool:
        return self.url.startswith("http")


class Image:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
