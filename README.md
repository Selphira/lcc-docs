Version POC de la liste des mods BG de FreddyGwendo : https://github.com/LaCouronnedeCuivre/lcc-docs

## Important

**Pour modifier un mod, c'est le ficher `mods.json` et uniquement lui qui doit être modifié.**\
En effet, le fichier `index.html` est généré automatiquement par le script `update_index.py` qui s'appuie sur le ficher db : `mods.json`.


## Améliorations par rapport à la v1

Cette version propose plusieurs améliorations techniques notables :
* Bien meilleure maintenabilité
* Merge des 8 jeux de données en un seul
* Merge des 8 templates : exit le fix typo à appliquer 8 fois
* Pas de connaissance nécessaire en html/css pour faire des modifications
* Suppression de la plage d'identifiant unique pour les mods
* Une seule feuille de style (avec utilisation de variable…)
* Retrait des styles inlines css
* Script de génération de la page `index.html`
* Les mods peuvent être dans plusieurs catégories
* Du responsive (un tableau ça a des limites)
* Une facilité de lecteure accrue (taille de police, des images etc)
* Modification aisée de la structure de la donnée (et des mods qui vont avec)
* Filtre par nom
* …

## Limites
* Modifier un Json est moins sexy que de passer par un formulaire fait pour ça
* …


## TODO
* Une doc pour savoir comment remplir/modifier le fichier `mods.json` et les différents attributs attendus
* Remplacer le Json par du Yaml paraît être une bonne idée mais la multiplication des `'\"\'` en tout genre ne m'y a pas encouragé (peut-être une config permet de contourner le problème ou une autre solution est envisageable ?)
* Formulaire d'ajout d'un mod qui renvoit son équivalent en Json (plus qu'à l'ajouter à la db)
* Rédaction de GuideLine pour les contributeurs


## Doc

Comme tout se fait dans le fichier `mods.json`, il est important de savoir ce qui est possible de faire ou non.

### Le JSON c'est quoi ?
Documentation sur le JSON : https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON
Outil en ligne pour valider le format de votre json : https://jsonformatter.curiousconcept.com


### Informations par défaut des mods :
```json
    {
        "name": "",
        "description": "",
        "urls": [],
        "categories": [],
        "games": [],
        "authors": [],
        "team": [],
        "notes": [],
        "is_weidu": 1,
        "translation_state": "no",
        "safe": 2,
        "languages": [],
        "status": "active",
        "last_update": "",
        "tp2": ""
    }
```


### Détails
`name` : nom du mod\
`description` : description du mod\
`urls` : liste de lien, généralement lien de téléchargement ou/et lien du forum le présentant\
`categories`: liste des catégories dans lesquelles le mod est placé. Valeurs possibles :
 - Patch non officiel
 - Utilitaire
 - Conversion partielle
 - Conversion totale
 - Interface
 - Cosmétique
 - Portrait et son
 - Quête
 - PNJ recrutable
 - PNJ One Day
 - PNJ (autre)
 - Forgeron et marchand
 - Sort et objet
 - Kit
 - Gameplay
 - Personnalisation du groupe

`games` : liste des jeux sur lesquels le mod est fonctionnel. Valeurs possibles :
 - BG
 - BG2
 - BGT
 - Tutu
 - BGEE
 - SoD
 - BG2EE
 - EET
 - IWD
 - IWD2
 - IWDEE
 - IWD2EE
 - PST
 - PSTEE

`authors`: liste des personnes ayant participé à la création/maintenance du mod, actuellement non affiché\
`team` : liste des personnes ayant participé à la traduction du mod\
`notes` : liste de messages indiquant des points d'attention\
`is_weidu` : si le mod est installable ou désinstallable via weidu. Valeurs possibles :
 - `2` : 😀 Mod Weidu
 - `1` : 😀 Mod Weidu (weidu "a priori" : cette valeur exprime un doute, à terme il faut choisir une autre valeur)
 - `0` : 😡 Mod override, non désinstalable

`translation_state` : le mod est traduit ou pas, ou s'il ne nécessite pas de traduction. Valeurs possibles :
 - `"yes"` : ✅ Mod traduit en français
 - `"no"` : ❌ Mod non traduit en français
 - `"n/a"` : ✅ Mod ne nécessitant pas de traduction
 - `"todo"` : ❎ Mod partiellement traduit
 - `"wip"` : ❌ Mod en cours de traduction

`safe` : si le mod est considéré comme fiable (installable via weidu, maintenu, ne génère pas d'incompatibilités). Valeurs possibles :
 - `2` : 🟢 Mod de qualité
 - `1` : 🟡 Mod pouvant poser des problèmes
 - `0` : 🔴 Mod à éviter ou obsolète

`languages` : langues dans lesquels le mod existe, actuellement non affiché, format [ISO-3166-1](https://fr.wikipedia.org/wiki/ISO_3166-1)

`status` : la raison peut être indiquée dans les `notes`, actuellement sans impact
 - `"active"` : mod actif
 - `"draft"` : mod en cours d'ajout mais pas encore finalisé
 - `"inactive"` : mod à ne pas afficher pour une autre raison à indiquer dans `notes`
 - `"obsolete"` : incompatible avec les dernières versions des jeux originaux ou/et EE (exemple d'un mod fait sous EE 1.3 mais jamais upgrade depuis)
 - `"embed"` : intégré en tant que composant (et maintenu) dans un autre mod ou pack
 - `"missing"` : lien de téléchargement disparu
 - `"wip"` : le mod est phase de développement

`last_update` : date connue de la dernière mise à jour du mod, champ automatique, format YYYY-MM

`tp2` : nom du fichier tp2 du mod. À terme, remplacera le champ `is_weidu`. Valeurs possibles :
 - `"nom du tp2"` : le vrai nom du tp2
 - `"n/a"` : non concerné (notamment pour les utilitaires)
 - `"non-weidu"` : pas de fichier tp2 car non-WeiDU
