// define variables used for the rest of the script
var lightstate;
var room;
var lux;

// define get_status function to collect status data for room, attach to "refresh" button, display in page
var refresh = function(){
	$.get( url_get_status, function(data) {
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
	$.get( url_get_status, function(data) {
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

	$('[data-toggle="tooltip"]').tooltip({html:true, trigger:"hover"});
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
		console.log("toggle change settings view");
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
		$("#selected_room").toggleClass("hidden");
		
		if ( $(this).html() == "Show") {
			// call script to plot chart
			$.getScript(url_charts, function(){
			});
			$(this).text("Hide");
		}
		else {
			$(this).text("Show");
			$("#myChart").remove();
			$("#charts").append('<canvas id="myChart" style="height: 250px; width: 100%"></canvas>');
		}
		
	});
	// endcode
	
	// light switch
	$("#lightSwitch").on('switchChange.bootstrapSwitch', function(event,state) {
		$.get("http://129.132.32.187/lights.php/?state="+(+state)+"&room="+room);
		$.get("http://129.132.32.187/trigger_push_button.php/?state="+(+state)+"&room="+room+"&origin=web"+"&user="+username);
		$.get(url_remote + "?switch=true&user=" + username, function(data) {
			console.log(data);
			console.log(url_remote + "?switch=true&user=" + username);
		});
		
		if (state) {
			alert("Lights has been switched on!");
		}
		else if (!state) {
			alert("Lights has been switched off!");
		}
		
		var myVar = setTimeout(function(){
				refresh();
				console.log("refresh");
			},2000);
	});
	
	$("#submit_settings").click(function(){
		//submit new settings as POST request
		console.log($("#change-settings-form").serialize());
		post_data = $("#change-settings-form").serializeArray();
		console.log($("#change-settings-form").serializeArray());
		$.post(url_remote, post_data, function(data){
			console.log(data);
		});
		
		console.log("submit new settings");
		$("#refresh_settings").trigger("click");
		$("#change_settings").trigger("click");
	});
});