import os
import re
from typing import List

from settings import IMG_ROOT, domain_to_image, icon_to_label, image_data


class Icon:
    def __init__(self, icon: str):
        self.icon = icon

    @property
    def label(self) -> str:
        return icon_to_label.get(self.icon, "")


class Mod:
    def __init__(
        self,
        name,
        categories,
        urls,
        warnings,
        description,
        team,
        games,
        safe,
        translation_state,
        is_weidu,
        language,
    ):
        self.name = name
        self.categories = categories
        self.urls = urls
        self.warnings = warnings
        self.safe = safe
        self.description = description
        self.team = team
        self.games = games
        self.translation_state = translation_state
        self.is_weidu = is_weidu
        self.language = language

    @property
    def urls_instance(self) -> list:
        return [Url(url) for url in self.urls]

    @property
    def ordered_games(self) -> list:
        return sorted(self.games)

    @property
    def icons(self) -> List[Icon]:
        icons = list()
        match self.safe:
            case None:
                icon = "🟡"
            case True:
                icon = "🟢"
            case False:
                icon = "🔴"
            case _:
                raise ValueError
        icons.append(Icon(icon))

        match self.translation_state:
            case True | None:
                icon = "🇨🇵"
            case "wip":
                icon = "❎"
            case False:
                icon = "❌"
            case "todo":
                icon = "✅"
            case _:
                raise ValueError
        icons.append(Icon(icon))

        if self.is_weidu is False:
            icon = "😡"
        else:
            icon = "😀"
        icons.append(Icon(icon))

        return icons


class Category:
    def __init__(self, name: str):
        self.name = name
        self.mods = list()

    @property
    def id(self) -> str:
        return self.name.lower().replace(" ", "-")


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
            else:
                img_data = image_data.get(
                    img, dict(title="titre de l'image", width=32, height=32)
                )

            img_dir = os.path.join("img", img)
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
        country = self.get_domain().rpartition(".")[-1]
        if country == "de":
            country = "ge"
        return country

    def get_image_country(self) -> str:
        country_img = f"{self.get_tld()}-flag-32.png"
        img = ""
        if os.path.exists(os.path.join(IMG_ROOT, country_img)):
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
