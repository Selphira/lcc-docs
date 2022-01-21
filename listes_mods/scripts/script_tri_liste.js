/* Code fourni par Selphira et modifié par Freddy_Gwendo
   ===================================================== */

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
/* Fonction originale sans traductions
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
