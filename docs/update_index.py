#!/usr/bin/env python3
import json
import os

# import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from list_import import category_map
from models import Category, Mod
from models_import import games


def main(env):
    categories = [Category(k) for k in dict.fromkeys(category_map.values())]
    with open("mods.json", "r") as f:
        mods = json.load(f)
    # with open("mods.yaml", "r") as f:
    #     mods = yaml.safe_load(f)

    for category in categories:
        for mod_json in mods:
            # for mod_json in mods.values():
            mod = Mod(**mod_json)
            if category.name not in mod.categories:
                continue
            category.mods.append(mod)

    # FIXME: pour le poc: static="static{os.sep}"
    page_html = env.get_template("base.html").render(
        games=games, categories=categories, static=f"mod_list{os.sep}static{os.sep}"
    )

    with open("index.html", "w") as f:
        f.write(page_html)


if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("mod_list", "templates"),
        autoescape=select_autoescape(["html"]),
    )
    main(env)
