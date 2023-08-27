// Grab data
let apiLine = "/covid/info2";
function init() {
  d3.json(apiLine).then(function(data) {
    console.log(data);
    let datasingle = data["Alabama"];
      let dataPlot = [{
        x: datasingle["Years"],//Object.keys(data),
        y: datasingle["Rates"],//Object.values(data),
        type: 'line'
      }]
      Plotly.newPlot("plot3", dataPlot);
    });
  }
// Function called by DOM changes
function refreshPlot() {
  let dropdownMenu = d3.select("#selDataset1");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  // Call function to update the chart
  d3.json(apiLine).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],//Object.keys(data),
      y: datasingle["Rates"],//Object.values(data),
      type: 'line'
    }]
    Plotly.newPlot("plot3", dataPlot);
  });
  refreshbarPlot()
  refreshPlot1()

}
// On change to the DOM, call getData()
d3.selectAll("#selDataset1").on("change", refreshPlot);
init();
// // On change to the DOM, call getData()
// d3.selectAll("#selDataset1").on("change", refreshPlot);
// init();


