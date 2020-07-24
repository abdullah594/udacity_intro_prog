// Select color & grid inputs
const cellColor = document.getElementById('colorPicker');
const grid = document.getElementById('pixelCanvas');
const gridSize = document.getElementById('sizePicker');
const gridHeight = document.getElementById('inputHeight').value;
const gridWidth = document.getElementById('inputWidth').value;
makeGrid(gridHeight, gridWidth);

/**
This is an eventListener that run the start() function which do
the following once the user click the submit boutton
1.prevent the defualt behavior of the for loop >> No GET request
2.delete the old grid if any
3.call for the makeGrid()
*/
gridSize.addEventListener ('click', function(start) {
  //stop the for loop behavior
  start.preventDefault();
  //delete the old grid
  grid.innerHTML = '';
  let gridHeight = document.getElementById('inputHeight').value;
  let gridWidth = document.getElementById('inputWidth').value;
  //call for the make makeGrid () function
  makeGrid (gridHeight, gridWidth);
});

/**
This is the makeGrid() function is to build the
grid based on the height & width entered by the user
// */
function makeGrid (gridHeight, gridWidth) {
  //for loop to build the rows
  for (let i = 0; i < gridHeight; i++) {
    let gridRow = grid.insertRow(i);
    //for loop to insert cells
    for (let j = 0; j < gridWidth; j++) {
      let gridCell = gridRow.insertCell(j);
      // /**
      // This is an eventListener that run the coloring() function which
      // color the selcted cell by the colorPicker value once the user
      // click any of the grid cells
      // */
      gridCell.addEventListener('click', function(coloring) {
        gridCell.style.backgroundColor = cellColor.value;
      });
    }
  }
}
