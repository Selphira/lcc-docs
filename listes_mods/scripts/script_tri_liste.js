/* Code fourni par Selphira
   ======================== */

function filterByGame() {

	// Variables
	let dropdown, table, rows, cells, filterGame, filterTranslation, filtered;
	dropdown = document.getElementById("gamesDropdown");
	translationDropdown = document.getElementById("translationsDropdown");
	tables = document.getElementsByClassName("tableau");
            
	filterTranslation = translationDropdown.value;
	filterGame = dropdown.value;


	Array.from(tables).forEach((table) => {
		rows = table.getElementsByTagName("tr");

		for (let row of rows) {
			filtered = filtredByGame(filterGame, row) || filteredByTranslation(filterTranslation, row);

			row.style.display = filtered ? "none" : "";
		}
	});
}


function filtredByGame(filter, row) {

	let games;
            
	games = row.getElementsByClassName("jeu");


	if (filter === "Tous" || !games.length) {
		return false;
	}
            
	for (let game of games) {
		if (filter === game.textContent) {
			return false;
		}
	}
            
	return true;
}


function filteredByTranslation(filter, row) {

	let notrads, miseajr, encours, trads, celltrad;
            
	if (filter === "all" || row.getElementsByTagName('th').length > 0) {
		return false;
	}

	notrads = row.getElementsByClassName("mod");
	trads   = row.getElementsByClassName("modblue");
	encours = row.getElementsByClassName("modlime");
	miseajr = row.getElementsByClassName("modred");


	if ((filter === "in-progress"   && encours.length > 0)
		|| (filter === "to-update"  && miseajr.length > 0)
		|| (filter === "translated" && trads.length > 0)
	) {
		return false;
	}


    // La colonne des traductions est toujours la 3ème en partant de la fin
	celltrad = row.cells.item(row.cells.length - 3);

	if (celltrad
		&& ((filter === "not-translated" && notrads.length > 0 && celltrad.innerHTML !== "pas besoin de traduction") 
		|| (filter === "translated" && celltrad.innerHTML === "pas besoin de traduction"))
	) {
		return false;
	}


	return true;
}

/* Code fourni par Selphira et modifié par Freddy_Gwendo
   =====================================================

function filteredByTranslation(filter, row) {

	let notrads, miseajr, encours, trads, entete, special, docname;
            
	if (filter === "all") {
		return false;
	}

	notrads = row.getElementsByClassName("mod");
	trads   = row.getElementsByClassName("modblue");
	encours = row.getElementsByClassName("modlime");
	miseajr = row.getElementsByClassName("modred");
	docname = document.title
	entete = row.cells.item(2);
	special = row.cells.item(3); // cas des tableaux des mods objets, marchands et forgerons qui ont une première colonne supplémentaire

	if  ((filter === "in-progress" && encours.length > 0 )
	  || (filter === "to-update" && miseajr.length > 0)
	  || (filter === "translated" && trads.length > 0 || (entete && entete.innerHTML === "Traducteurs") || (special && special.innerHTML === "Traducteurs")) ) {
		return false;
	}

	cell = row.cells.item(5);
	celltrad = row.cells.item(6);

	if (docname === "Liste des mods pour BG - La Couronne de Cuivre") {
		cell = row.cells.item(7);
		celltrad = row.cells.item(8);
	} else {
		if (docname === "Liste des mods pour PST - La Couronne de Cuivre") {
			cell = row.cells.item(3);
			celltrad = row.cells.item(4);
		}
	}

	if (filter === "not-translated" && notrads.length > 0 && ((cell && cell.innerHTML !== "pas besoin de traduction" ) && (celltrad && celltrad.innerHTML !== "pas besoin de traduction")) ){
		return false
	}

	if (filter === "translated" && ((cell && cell.innerHTML === "pas besoin de traduction" ) || (celltrad && celltrad.innerHTML === "pas besoin de traduction")) ) {
		return false;
	}

	return true;
}

function filterByGame() {

	// Variables
	let dropdown, table, rows, cells, games, filter, notrads, miseajr, encours, trads;
	dropdown = document.getElementById("gamesDropdown");
	tables = document.getElementsByClassName("tableau");

	Array.from(tables).forEach((table) => {
		rows = table.getElementsByTagName("tr");
		filter = dropdown.value;

		for (let row of rows) {
			games   = row.getElementsByClassName("jeu");
			notrads = row.getElementsByClassName("mod");
			trads   = row.getElementsByClassName("modblue");
			encours = row.getElementsByClassName("modlime");
			miseajr = row.getElementsByClassName("modred");

			if (filter === "Tous" || !games.length) {
				row.style.display = "";
				continue;
			}

    		for (let game of games) {
				if (filter === game.textContent) {
					row.style.display = "";
					break;
				} else {
					if  ( (filter === "Non traduits" && notrads.length > 0)
					   || (filter === "Traduction en cours" && encours.length > 0)
					   || (filter === "Traduits" && trads.length > 0)
					   || (filter === "Mise à jour nécessaire" && miseajr.length > 0) ) {
					row.style.display = "";
				} else {
					row.style.display = "none";
				}
				}
			}

		}

	});
}
Fonction originale, sans traductions
====================================
function filterByGame() {

	// Variables
	let dropdown, table, rows, cells, games, filter;
	dropdown = document.getElementById("gamesDropdown");
	tables = document.getElementsByClassName("tableau");

	Array.from(tables).forEach((table) => {
		rows = table.getElementsByTagName("tr");
		filter = dropdown.value;

		for (let row of rows) {
			games = row.getElementsByClassName("jeu");

			if (filter === "Tous" || !games.length) {
				row.style.display = "";
				continue;
			}

    		for (let game of games) {
				if (filter === game.textContent) {
					row.style.display = "";
					break;
				} else {
					row.style.display = "none";
				}
			}

		}

	});
*/
