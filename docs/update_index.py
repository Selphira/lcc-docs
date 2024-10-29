#!/usr/bin/env python3
import json
import os

# import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from models import Category, Mod
from settings import Games, attrs_icon_data

categorie_names = [
    "Patch non officiel",
    "Utilitaire",
    "Installation",
    "Conversion",
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


def main(env):
    categories = [Category(k) for k in categorie_names]
    with open("mods.json", "r") as f:
        mods = json.load(f)
    # with open("mods.yaml", "r") as f:
    #     mods = yaml.safe_load(f)

    mods.sort(key=lambda x: x["name"])

    for category in categories:
        for mod_json in mods:
            # for mod_json in mods.values():
            mod = Mod(**mod_json)
            if category.name not in mod.categories:
                continue
            category.mods.append(mod)

    page_html = env.get_template("base.html").render(
        games=Games,
        categories=categories,
        static=f"src{os.sep}static{os.sep}",
        attrs_icon_data=attrs_icon_data,
    )

    with open("index.html", "w") as f:
        f.write(page_html)


if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("src", "templates"),
        autoescape=select_autoescape(["html"]),
    )
    main(env)
