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
* Pas de mise à jour automatique de la page suite à une modification de la db
* Modifier un Json est moins sexy que de passer par un formulaire fait pour ça
* …


## TODO
* Une doc pour savoir comment remplir/modifier le fichier `mods.json` et les différents attributs attendus
* Remplacer le Json par du Yaml paraît être une bonne idée mais la multiplication des `'\"\'` en tout genre ne m'y a pas encouragé (peut-être une config permet de contourner le problème ou une autre solution est envisageable ?)
* Pouvoir automatiser la mise à jour de la page après une modification de la db (script JS ?)
* Formulaire d'ajout d'un mod qui renvoit son équivalent en Json (plus qu'à l'ajouter à la db)
