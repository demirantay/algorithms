// DOM elements
let box_container = document.getElementById("box_container");

function generate_random_int() {
  let min = Math.ceil(1);
  let max = Math.floor(100);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generate_box() {
  let value = generate_random_int();
  return `<div id="box_cell"><h3 id="box_cell_value"> ${value} </h3></div>`;
}




for (i = 0; i < 10; i++) {
  box_container.innerHTML += generate_box();
}
