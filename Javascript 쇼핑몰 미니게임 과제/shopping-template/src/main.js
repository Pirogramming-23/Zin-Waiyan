// Fetch the items from the JSON file
function loadItems() {
  return fetch('data/data.json')
  .then(response => response.json())
  .then(json => json.items);
}

// Update the list with the given items
function displayItems(items){
    const container = document.querySelector(".items");
    const html = items.map(item => createHTMLString(item));
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

// Create HTML list item from the given data item
function createHTMLString(item){
    return `
        <li class="item">
            <img src="img/yellow_p.png" alt="" class="item__thumbnail">
            <span class="item__description">male, large</span>
        </li>
    `;
}

// main
loadItems()
    .then(items => {
        console.log(items);
        displayItems(items);
        // setEventListeners(items)
    })
    .catch(console.log);