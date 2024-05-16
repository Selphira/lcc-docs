import os

STATIC_ROOT = os.path.join("mod_list", "static")
IMG_ROOT = os.path.join(STATIC_ROOT, "img")

icon_to_label = {
    "🟢": "Mod de qualité",
    "🟡": "Mod pouvant poser des problèmes",
    "🔴": "Mod à éviter ou obsolète",
    "✅": "Traduction à jour",
    "❎": "Traduction française non à jour",
    "❌": "Non traduit",
    "😀": "Mod Weidu",
    "😡": "Mod override, à vos risques et périls",
}

# TODO: ordre à définir
games = [
    "BG",
    "BG2",
    "BGT",
    "Tutu",
    "BGEE",
    "SoD",
    "BG2EE",
    "EET",
    "IWD",
    "IWD2",
    "IWDEE",
    "IWD2EE",
    "PST",
    "PSTEE",
]


# TODO: réduire/convertir les static/img
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
    # TODO: recentrer cet icône
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
