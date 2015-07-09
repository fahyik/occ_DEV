var room_selected = $("#selected_room option:selected").val();
console.log(room_selected, default_room);


$.get( url_get_chart_data, {"room": room_selected}, function(data_db) {
	
	if (room_selected) {
		$("#chart_room").empty().append($("#selected_room option:selected").text());
	}
	else {
		$("#chart_room").empty().append(default_room);
	}
	
	plot(data_db);
	
}, "json");


var plot = function (data_db) {

	// Get the context of the canvas element we want to select
	var canvas = document.getElementById("myChart");
	var ctx = canvas.getContext("2d");
	Chart.defaults.global.responsive = true;
	Chart.defaults.global.scaleIntegersOnly = false;

	var size = data_db.consumption.length;
	console.log(data_db.consumption.length);

	// create arrays from data from db
	var xlabels = [];
	var yvalues = [];

	for (var day = 0; day < size; day++) {
		xlabels.push(data_db.dates[day]);
		yvalues.push(data_db.consumption[day]);
	}
	console.log(yvalues);

// 	var data = {
// 		labels: xlabels,
// 		datasets: [
// 			{
// 				label: "Energy Consumption",
// 				fillColor: "rgba(151,187,205,0.2)",
// 				strokeColor: "rgba(151,187,205,1)",
// 				pointColor: "rgba(151,187,205,1)",
// 				pointStrokeColor: "#fff",
// 				pointHighlightFill: "#fff",
// 				pointHighlightStroke: "rgba(151,187,205,1)",
// 				data: yvalues
// 			},
// 			// {
// 	//             label: "My Second dataset",
// 	//             fillColor: "rgba(151,100,205,0.2)",
// 	//             strokeColor: "rgba(151,100,205,1)",
// 	//             pointColor: "rgba(151,100,205,1)",
// 	//             pointStrokeColor: "#fff",
// 	//             pointHighlightFill: "#fff",
// 	//             pointHighlightStroke: "rgba(151,100,205,1)",
// 	//             data: [2, 4, 4, 1, 8, 2, 9]
// 	//         }
// 		]
// 	};
// 
// 	var myLineChart = new Chart(ctx).Line(data, {});
	
	// bar chart instead:
	var data = {
		labels: xlabels,
		datasets: [
			{
				label: "Energy Consumption",
				fillColor: "rgba(151,187,205,0.2)",
				strokeColor: "rgba(151,187,205,1)",
				HighlightFill: "#fff",
				HighlightStroke: "rgba(151,187,205,1)",
				data: yvalues
			},
		]
	};

	var myLineChart = new Chart(ctx).Bar(data, {});
}