// define variables used for the rest of the script
var lightstate;
var room;
var lux;


// define get_status function to collect status data for room, attach to "refresh" button, display in page
var refresh = function(){
	$.get( "/get_status", function(data) {
		lightstate = data.res.lights;
		lux = data.res.lux;
		room = data.res.room;
		time = data.res.time;
		console.log(lightstate, lux, room, time);
		// update values in page html
		$("#lux_reading").empty().append(lux);
		$("#time_updated").empty().append("updated: "+time);
		// updateLightSwitch
		updateLightSwitch();
		
	}, "json");
}

// define get_status function to collect status data for room, attach to "refresh" button, display in page
var refreshSetPoints = function(){
	$.get( "/get_status", function(data) {
		// update values in page html
		$("#lux_th").empty().append(data.res2.lux_th);
		$("#lux_th_new").attr("value", data.res2.lux_th);
		$("#upp_th").empty().append(data.res2.upp_th);
		$("#upp_th_new").attr("value", data.res2.upp_th);
		$("#td_setting").empty().append(data.res2.td);
		$("#td_setting_new").attr("value", data.res2.td);
		
	}, "json");
}

// define function to update lightswitch
var updateLightSwitch = function(){
	lightbool = lightstate > 0 ? true : false;
	console.log(lightbool,lightstate,room,lux);
	
	//button starts off with no checked option;
	if (lightstate == 1) {
		$("#lightSwitch").attr("checked","checked");
	}
	
	$("#lightSwitch").bootstrapSwitch('state',lightbool);
	if (lightstate >= 0) {
		$("#lightSwitch").bootstrapSwitch('disabled', false);
	}
	else {
		$("#lightSwitch").bootstrapSwitch('disabled', true);
	}
}


$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip({html:true});
	$('[data-toggle="popover"]').popover({html:true});
	
	//call get_status
	refresh();
	refreshSetPoints();
	
	//refresh button
	$("#refresh_status").click(function(){
		refresh();
	});
	
	//refresh settings
	$("#refresh_settings").click(function(){
		refreshSetPoints();
		console.log("refresh settings");
	});
	
	//change settings button
	$("#change_settings").click(function(){
		console.log("show change settings");
		$(".change-settings").toggleClass("hidden");
		if ( $(this).html() == "Change Settings") {
			// call script to plot chart
			$(this).text("Hide Change Settings");
		}
		else {
			$(this).text("Change Settings");
		}
	});
	
	// show charts
	$("#db_toggle_charts").click(function(){

		$("#charts").toggleClass("hidden");
		if ( $(this).html() == "Show") {
			// call script to plot chart
			$.getScript(url_charts, function(){
			});
			$(this).text("Hide");
		}
		else {
			$(this).text("Show");
			$("#daily_consumption").empty();
		}
		
	});
	// endcode
	
	// light switch
	$("#lightSwitch").on('switchChange.bootstrapSwitch', function(event,state) {
		if (state) {
			$.get("http://129.132.32.187/lights.php/?state="+(+state)+"&room="+room);
			alert("Lights has been switched on!");
			refresh();
		}
		else if (!state) {
			$.get("http://129.132.32.187/lights.php/?state="+(+state)+"&room="+room);
			alert("Lights has been switched off!");
			refresh();
		}
	});
});