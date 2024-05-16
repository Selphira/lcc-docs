import os
import re
from typing import List

icon_to_label = {
    "🟢": "Mod de qualité",
    "🟡": "Mod pouvant poser des problèmes",
    "🔴": "Mod à éviter ou obsolète",
    "🇨🇵": "Traduction à jour",
    "✅": "Traduction française non à jour",
    "❎": "Non traduit mais traduction en cours",
    "❌": "Non traduit",
    "😀": "Mod Weidu",
    "😡": "Mod override, à vos risques et périls",
}


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


IMG_ROOT = os.path.join("mod_list", "static", "img")

domain_to_image = {
    "artisans-corner.com": "artisans700.png",
    "baldursgateworld.fr": "logocc.png",
    "anomaly-studios.fr": "logocc.png",
    "baldursgatemods.com": "teambg.png",
    "beamdog.com": "beamdog.png",
    "blackwyrmlair.net": "bwl.gif",
    "gibberlings3.net": "g3icon.ico",
    "github.com": "github.png",
    "github.io": "github.png",
    "havredest.eklablog.fr": "luren.jpg",
    "pocketplane.net": "ppg.jpg",
    "mediafire.com": "mediafire.png",
    "nexusmods.com": "nexus-230x230.png",
    "reddit.com": "reddit_76.png",
    "sasha-altherin.webs.com": "ab-logo.jpg",
    "sentrizeal.com": "sentrizeal.ico",
    "shsforums.net": "shs_reskit.png",
    "sorcerers.net": "sorcerer.jpg",
    "sourceforge.net": "sf.png",
    "weaselmods.net": "weasel.png",
    "weidu.org": "weidu.ico",
    # les cas particuliers récupérés de la version de freddy
    "clandlan.net": "sp-flag-32.png",
    "trow.cc": "ch-flag-32.png",
}

image_data = {
    "artisans700.png": {"title": "The Artisan Corner", "width": 32, "height": 32},
    "logocc.png": {"title": "La Courrone de Cuivre", "width": 32, "height": 32},
    "teambg.png": {"title": "TeamBG", "width": 32, "height": 32},
    "beamdog.png": {"title": "Beamdog", "width": 32, "height": 32},
    "bwl.gif": {"title": "The Black Wyrm's Lair", "width": 32, "height": 32},
    "g3icon.ico": {"title": "Gibberlings3", "width": 32, "height": 32},
    "github.png": {"title": "GitHub", "width": 32, "height": 32},
    # TODO: raccourcir cet icône
    "luren.jpg": {"title": "Retour à Havredest", "width": 78},
    "ppg.jpg": {"title": "Pocket Plane Group", "width": 32, "height": 32},
    "mediafire.png": {"title": "Mediafire", "width": 32, "height": 32},
    "nexus-230x230.png": {"title": "Nexus Mods", "width": 32, "height": 32},
    "reddit_76.png": {"title": "Reddit", "width": 32, "height": 32},
    "ab-logo.jpg": {"title": "AB aka Sasha al'Therin", "width": 32, "height": 32},
    "sentrizeal.ico": {"title": "Sentrizeal", "width": 32, "height": 32},
    "shs_reskit.png": {"title": "Spellhold Studios", "width": 32, "height": 32},
    "sorcerer.jpg": {"title": "Sorcerer's Place", "width": 32, "height": 32},
    "sf.png": {"title": "SourceForge", "width": 32, "height": 32},
    "weasel.png": {"title": "Weasel Mods", "width": 32, "height": 32},
    "weidu.ico": {"title": "WeiDU", "width": 16, "height": 16},
    "-flag-32.png": {"title": "Mod %s", "width": 32},
}

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
