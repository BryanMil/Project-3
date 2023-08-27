// Grab data
let apiLine1 = "/covid/info3";
function init() {
  d3.json(apiLine1).then(function(data) {
    console.log(data);
    let datasingle = data["Alabama"];
      let dataPlot = [{
        x: datasingle["Years"],//Object.keys(data),
        y: datasingle["Rates"],//Object.values(data),
        type: 'line'
      }]
      Plotly.newPlot("plot4", dataPlot);
    });
  }
// Function called by DOM changes
function refreshPlot1() {
  let dropdownMenu = d3.select("#selDataset1");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  // Call function to update the chart
  d3.json(apiLine1).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],//Object.keys(data),
      y: datasingle["Rates"],//Object.values(data),
      type: 'line'
    }]
    Plotly.newPlot("plot4", dataPlot);
  });
 
}
// On change to the DOM, call getData()
// d3.selectAll("#selDataset1").on("change", refreshPlot1);
// init();
