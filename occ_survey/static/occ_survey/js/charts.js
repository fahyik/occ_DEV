// Get the context of the canvas element we want to select
var ctx = document.getElementById("myChart").getContext("2d");
Chart.defaults.global.responsive = true;

var size = data_db.consumption.length;
console.log(data_db.consumption.length);

// create arrays from data from db
var xlabels = [];
var yvalues = [];

for (var day = size-1; day >= 0; day--) {
    xlabels.push(data_db.dates[day]);
    yvalues.push(data_db.consumption[day]);
}

var data = {
    labels: xlabels,
    datasets: [
        {
            label: "Energy Consumption",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: yvalues
        },
        // {
//             label: "My Second dataset",
//             fillColor: "rgba(151,100,205,0.2)",
//             strokeColor: "rgba(151,100,205,1)",
//             pointColor: "rgba(151,100,205,1)",
//             pointStrokeColor: "#fff",
//             pointHighlightFill: "#fff",
//             pointHighlightStroke: "rgba(151,100,205,1)",
//             data: [2, 4, 4, 1, 8, 2, 9]
//         }
    ]
};

var myLineChart = new Chart(ctx).Line(data, {});