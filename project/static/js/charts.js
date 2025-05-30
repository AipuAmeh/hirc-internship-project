const getCharts = () => {
    try {
    fetch('/api/data')
    .then((res) => {
        res.json()
        console.log(res)
    })
    .then()
    } catch (error) {
        console.log(error)
    }

}

