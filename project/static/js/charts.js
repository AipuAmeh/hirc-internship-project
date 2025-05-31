// refactor logic later for simplicity
const barChart = (xArray, yArray) => {
  const chartId = document.querySelector("#bar-chart");
  chartId.innerHTML = "";
  const layout = { title: `A Project Manager's Task Load` };
  const data = [
    {
      x: xArray,
      y: yArray,
      type: "bar",
      orientation: "v",
      marker: { color: "rgba(0,0,255)" },
    },
  ];
  Plotly.newPlot(chartId, data, layout);
};

const pieChart = (xArray, yArray) => {
  const chartId = document.querySelector("#pie-chart");
  chartId.innerHTML = "";
  const layout = { title: "Research Types" };
  const data = [
    {
      labels: xArray,
      values: yArray,
      type: "pie",
    },
  ];
  Plotly.newPlot(chartId, data, layout);
};

const getCharts = (event) => {
  const chart_type = event.target.value;
  try {
    fetch(`/api/data?chart_type=${chart_type}`)
      .then((res) => res.json())
      .then((chartData) => {
        document.querySelector("#bar-chart").style.display = "none";
        document.querySelector("#pie-chart").style.display = "none";

        if (chart_type == "pm_vs_category" && chartData.length > 0) {
          let xArray = chartData.map((item) => item.project_manager);
          let yArray = chartData.map((item) => item.count);
          document.querySelector("#bar-chart").style.display = "block";
          barChart(xArray, yArray);

        } else if (chart_type == "rsch_category" && chartData.length > 0) {
          let xArray = chartData.map((item) => item.research_type);
          let yArray = chartData.map((item) => item.count);
          document.querySelector("#pie-chart").style.display = "block";
          pieChart(xArray, yArray);

        } else {
          console.log("nothing to see here");
        }
      });
  } catch (error) {
    console.log(error);
  }
};
