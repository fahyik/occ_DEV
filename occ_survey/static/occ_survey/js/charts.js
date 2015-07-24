var room_selected = $("#selected_room option:selected").val();
console.log(room_selected, default_room);

google.setOnLoadCallback(drawChart);
var drawChart = function(data_db) {

	var size = data_db.consumption.length;
	console.log(data_db.consumption.length);

	// create arrays from data from db
	var data_set = [];
	data_set.push(['Day', 'Consumption', 'Consumption per hour occupancy', 'Occupancy']);
	
	for (var day = 0; day < size; day++) {
		data_set.push([data_db.dates[day], data_db.consumption[day], +(data_db.consumption[day]/data_db.occupancy[day]).toFixed(2), data_db.occupancy[day]]);
	}
	console.log(data_set);
	var data = google.visualization.arrayToDataTable(data_set);

	var options = {
		//title : 'Monthly Coffee Production by Country',
		//hAxis: {title: "Month"},
		vAxis: {
		  title: "Number of Hours",
		  minValue: 0,
		  //maxValue: 16,
		  baselineColor: '#DDD',
		  gridlines: {
			color: '#DDD',
			count: -1,
		  },
		  textStyle: {
			fontSize: 11
		  },
		  viewWindowMode: "maximize",
		},
		seriesType: "bars",
		series: {2: {type: "line"}},
		colors: ['#5da5ca','#97bbcd','#4c5f69'],
		legend: {
		  position: 'bottom',
		  textStyle: {
			fontSize: 12
		  }
		},
		fontName: 'Open Sans',
		chartArea: {
		  left: 50,
		  top: 10,
		  width: '100%',
		  height: '70%'
		},
	};

	var chart = new google.visualization.ComboChart(document.getElementById('myChart2'));

	chart.draw(data, options);
}

$.get( url_get_chart_data, {"room": room_selected}, function(data_db) {
	
	if (room_selected) {
		$("#chart_room").empty().append($("#selected_room option:selected").text());
	}
	else {
		$("#chart_room").empty().append(default_room);
	}
	
	drawChart(data_db);
	$(window).resize(function(){
		drawChart(data_db);
	});
}, "json");
