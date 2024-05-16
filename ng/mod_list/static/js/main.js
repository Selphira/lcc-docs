// reset des filtres et selects
document.addEventListener("DOMContentLoaded", () => {
  const checkedGames = document.querySelectorAll(".search_item.game input[type='checkbox']:checked")
  checkedGames.forEach(input => input.checked = false)
  document.querySelector("#search-text").value = ""
  document.querySelector("#translation-all").checked = true
})

function filterMod() {
  const mods = Array.from(document.querySelectorAll(".table .row.mod"))
  let modByName = filterByName(mods)
  let modByGame = filterByGame(mods)
  let modByTranslation = filterByTranslation(mods)
  let modsFiltered = mods

  if (modByName !== null) {
    modsFiltered = modByName
  }
  if (modByGame !== null) {
    modsFiltered = modByGame.filter(elt => new Set(modsFiltered).has(elt))
  }
  if (modByTranslation !== null) {
    modsFiltered = modByTranslation.filter(elt => new Set(modsFiltered).has(elt))
  }

  mods.forEach(mod => mod.classList.add("hidden"))
  modsFiltered.forEach(mod => mod.classList.remove("hidden"))

  // check des catégories (les enlèvent si aucun résultat n'est trouvé)
  let categories = document.querySelectorAll(".table .category")
  categories.forEach(category => category.style.display = category.querySelector(".row.mod:not(.hidden)") ? "" : "none")
}

function filterByGame(mods) {
  const checkedGames = Array.from(document.querySelectorAll(".search_item.game input[type='checkbox']:checked")).map(input => input.id)
  let modsFiltered = null
  if (checkedGames.length > 0) {
    modsFiltered = Array()
    mods.forEach(mod => {
      for (let modGame of mod.querySelectorAll(".jeu *")) {
        if (checkedGames.includes(modGame.textContent)) {
          modsFiltered.push(mod)
          break
        }
      }
    })
  }
  return modsFiltered
}

function filterByName(mods) {
  const input = document.querySelector("#search-text")
  let modsFiltered = null
  if (input.value !== "") {
    let inputValue = input.value.toLowerCase()
    modsFiltered = Array.from(mods).filter(mod => mod.querySelector(".name").textContent.toLowerCase().includes(inputValue))
  }
  return modsFiltered
}

function filterByTranslation(mods) {
  const currentTranslation = document.querySelector("#translation-select input:checked").value
  if (currentTranslation == "") {
    return null
  }
  return Array.from(mods).filter(mod => mod.querySelector(".icons").textContent.includes(currentTranslation))
}