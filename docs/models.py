import os
import re
import unicodedata
from typing import List

from settings import (
    FLAG_DIR,
    IMG_ROOT,
    SITE_DIR,
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
        is_weidu,
        languages,
        authors=None,
    ):
        self.name = name
        self.categories = categories
        self.urls = urls
        self._notes = notes
        self.safe = safe
        self._description = description
        self.team = team
        self.games = games
        self.translation_state = translation_state
        self.is_weidu = is_weidu
        self.languages = languages
        self.authors = authors

    @property
    def id(self) -> str:
        return slugify(self.name)

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

    @property
    def description(self) -> str:
        description = self._convert_link(self._description)
        return self._convert_quote(description)

    @property
    def notes(self) -> list:
        notes = list()
        for note in self._notes:
            new_note = self._convert_link(note)
            new_note = self._convert_quote(new_note)
            notes.append(new_note)
        return notes


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
