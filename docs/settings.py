import enum
import os
from typing import Dict

STATIC_ROOT = os.path.join("src", "static")
IMG_ROOT = os.path.join(STATIC_ROOT, "img")

"""
    safe: les paramètres qui font baisser la note :
    - incompatibilités avec d'autres mods ou avec la dernière version du jeu (notamment pour les EE) ⇒ les mods override sont toujours concernés
    - autre version plus avancée existante (présence dans un mod plus conséquent, plus maintenu ou avec une meilleure compatibilité)
    - installation difficile
    - mod en version bêta ou wip
"""
attrs_icon_data: Dict[str, Dict[tuple, Dict[str, str]]] = {
    "safe": {
        (True,): {
            "icon": "🟢",
            "label": "Mod de qualité",
        },
        (None,): {
            "icon": "🟡",
            "label": "Mod pouvant poser des problèmes",
        },
        (False,): {
            "icon": "🔴",
            "label": "Mod à éviter ou obsolète",
        },
    },
    "translation_state": {
        (True, None): {
            "icon": "✅",
            "label": "Mod traduit",
        },
        ("todo",): {
            "icon": "❎",
            "label": "Mod partiellement traduit",
        },
        (False, "wip"): {
            "icon": "❌",
            "label": "Mod non traduit",
        },
    },
    "is_weidu": {
        (True, None): {
            "icon": "😀",
            "label": "Mod Weidu",
        },
        (False,): {
            "icon": "😡",
            "label": "Mod override, non désinstalable",
        },
    },
}


# TODO: ordre à définir
class Games(enum.StrEnum):
    BG = "BG"
    BG2 = "BG2"
    TUTU = "Tutu"
    BGT = "BGT"
    BGEE = "BGEE"
    BG2EE = "BG2EE"
    SOD = "SoD"
    EET = "EET"
    IWD = "IWD"
    IWD2 = "IWD2"
    IWDEE = "IWDEE"
    IWD2EE = "IWD2EE"
    PST = "PST"
    PSTEE = "PSTEE"

    @classmethod
    def pst(cls) -> list:
        return [cls.PST, cls.PSTEE]

    @classmethod
    def iwd(cls) -> list:
        return [cls.IWD, cls.IWD2, cls.IWDEE, cls.IWD2EE]

    @classmethod
    def bg2(cls) -> list:
        return [cls.BG2, cls.BGT, cls.BG2EE, cls.EET]

    @classmethod
    def bg1(cls) -> list:
        return [cls.BG, cls.TUTU, cls.BGT, cls.BGEE, cls.SOD, cls.EET]


categorie_names = [
    "Patch non officiel",
    "Utilitaire",
    "Conversion partielle",
    "Conversion totale",
    "Interface",
    "Cosmétique",
    "Portrait et son",
    "Quête",
    "PNJ recrutable",
    "PNJ One Day",
    "PNJ (autre)",
    "Forgeron et marchand",
    "Sort et objet",
    "Kit",
    "Gameplay",
    "Personnalisation du groupe",
]

FLAG_DIR = "flags"
SITE_DIR = "sites"

# TODO: réduire/convertir les static/img
domain_to_image = {
    "artisans-corner.com": "artisans700.avif",
    "baldursgateworld.fr": "logocc.png",
    "anomaly-studios.fr": "logocc.png",
    "baldursgatemods.com": "teambg.png",
    "beamdog.com": "beamdog.png",
    "blackwyrmlair.net": "bwl.gif",
    "gibberlings3.net": "g3icon.avif",
    "github.com": "github.png",
    "github.io": "github.png",
    "havredest.eklablog.fr": "luren.avif",
    "pocketplane.net": "ppg.jpg",
    "mediafire.com": "mediafire.png",
    "nexusmods.com": "nexus-230x230.png",
    "reddit.com": "reddit_76.png",
    "sasha-altherin.webs.com": "ab-logo.jpg",
    "sentrizeal.com": "sentrizeal.ico",
    "shsforums.net": "shs_reskit.avif",
    "sorcerers.net": "sorcerer.avif",
    "sourceforge.net": "sf.png",
    "weaselmods.net": "weasel.png",
    "weidu.org": "weidu.ico",
    # les cas particuliers récupérés de la version de freddy
    "clandlan.net": "sp-flag-32.png",
    "trow.cc": "cn-flag-32.png",
}

image_data = {
    "artisans700.avif": {"title": "The Artisan Corner", "width": 32},
    "logocc.png": {"title": "La Courrone de Cuivre", "width": 32},
    "teambg.png": {"title": "TeamBG", "width": 32},
    "beamdog.png": {"title": "Beamdog", "width": 32},
    "bwl.gif": {"title": "The Black Wyrm's Lair", "width": 32},
    "g3icon.avif": {"title": "Gibberlings3", "width": 32},
    "github.png": {"title": "GitHub", "width": 32},
    # TODO: raccourcir cet icône
    "luren.avif": {"title": "Retour à Havredest", "width": 78},
    "ppg.jpg": {"title": "Pocket Plane Group", "width": 32},
    "mediafire.png": {"title": "Mediafire", "width": 32},
    "nexus-230x230.png": {"title": "Nexus Mods", "width": 32},
    "reddit_76.png": {"title": "Reddit", "width": 32},
    "ab-logo.jpg": {"title": "AB aka Sasha al'Therin", "width": 32},
    "sentrizeal.ico": {"title": "Sentrizeal", "width": 32},
    "shs_reskit.avif": {"title": "Spellhold Studios", "width": 32},
    "sorcerer.avif": {"title": "Sorcerer's Place", "width": 32},
    "sf.png": {"title": "SourceForge", "width": 32},
    "weasel.png": {"title": "Weasel Mods", "width": 32},
    "weidu.ico": {"title": "WeiDU", "width": 16, "height": 16},
    "-flag-32.png": {"title": "Mod %s", "width": 32},
}
