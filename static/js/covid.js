
let industry_data2 = "/covid/info";
function init() {
  d3.json(industry_data2).then(function(data) {
    console.log(data);

  
    let datasingle = data["Alaska"];
      let dataPlot = [{
        x: datasingle["Years"],
        y: datasingle["Rates"],
        type: 'bar'
      }]
      Plotly.newPlot("plot1", dataPlot);
    });
  }
// Function called by DOM changes
function refreshbarPlot() {console.log('Years')
  let dropdownMenu = d3.select("#selDataset1");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  console.log(filter)
  // Call function to update the chart
  d3.json(industry_data2).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],
      y: datasingle["Rates"],
      type: 'bar'
    }]
    Plotly.newPlot("plot1", dataPlot);
  });


}
// // On change to the DOM, call getData()
// d3.selectAll("#selDataset1").on("change", refreshbarPlot);
// init();



