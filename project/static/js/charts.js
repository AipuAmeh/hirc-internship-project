const getCharts = (event) => {
  const chart_type = event.target.value;
      try {
      fetch(`/api/data?chart_type=${chart_type}`)
      .then((res) => res.json())
      .then((chartData) => console.log(chartData))
      } catch (error) {
          console.log(error)
      }
};


