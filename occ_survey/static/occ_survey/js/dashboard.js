// define variables used for the rest of the script
var lightstate;
var room;
var lux;
var clicked = false;

// define get_status function to collect status data for room, attach to "refresh" button, display in page
var refresh = function(){
	$.get( url_get_status, function(data) {
		lightstate = data.res.lights;
		lux = data.res.lux;
		room = data.res.room;
		time = data.res.time;
		//console.log(lightstate, lux, room, time);
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
		$("#lux_th_new").val(data.res2.lux_th);
		$("#upp_th").empty().append(data.res2.upp_th);
		$("#upp_th_new").val(data.res2.upp_th);
		$("#td_setting").empty().append(data.res2.td);
		$("#td_setting_new").val(data.res2.td);
		
	}, "json");
}

// define function to update lightswitch
var updateLightSwitch = function(){
	lightbool = lightstate > 0 ? true : false;
	//console.log(lightbool,lightstate,room,lux);
	
	//button starts off with no checked option;
	if (lightstate == 1) {
		$("#lightSwitch").attr("checked","checked");
	}
	
	$("#lightSwitch").bootstrapSwitch('state',lightbool);
	
	//to disable light switch if lightstate is -2, i.e. dS not working.
	if (lightstate >= 0) {
		$("#lightSwitch").bootstrapSwitch('disabled', false);
	}
	else {
		$("#lightSwitch").bootstrapSwitch('disabled', true);
	}
	clicked = false;
}

var getOverride = function() {
	$.get( url_get_override_status+"?room="+default_room, function(data) {
		if (data.override == 1) {
			$("#override_status").removeClass("hidden");
		} else {
		
		}
		
	}, "json");	
}

$(document).ready(function(){

	$('[data-toggle="tooltip"]').tooltip({html:true, trigger:"hover"});
	$('[data-toggle="popover"]').popover({html:true});
	
	//call get_status
	refresh();
	refreshSetPoints();
	getOverride();

	
	//refresh button
	$("#refresh_status").click(function(){
		clicked = true;
		console.log("refresh status");
		refresh();
	});
	
	//refresh settings
	$("#refresh_settings").click(function(){
		refreshSetPoints();
		getOverride();
		console.log("refresh settings");
	});
	
	//change settings button
	$("#change_settings").click(function(){
		console.log("toggle change settings view");
		$("#refresh_settings").trigger("click");
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
		if (clicked) {
			clicked = false;
			console.log("switch changed, but not by click, no action");
		} else {
			console.log("switched");
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
			}

	});
	
	
	$("#submit_settings").click(function(){
		//submit new settings as POST request
		console.log($("#change-settings-form").serialize());
		var post_data = $("#change-settings-form").serializeArray();

		$.post(url_remote, post_data, function(data){
			console.log(data.success);
			if (data.error) {
				alert(data.error)
			}
			$("#refresh_settings").trigger("click");
		},"json");
		
		console.log("submit new settings");
		$("#change_settings").trigger("click");
	});
	
	//disable override
	$("#override").click(function(){
		console.log("disable override");
		$("#override_status").addClass("hidden");
		var post_data = $("#override-form").serializeArray();
		console.log(post_data);
		$.post(url_get_override_status, post_data, function(data){
			console.log(data);
			$("#refresh_settings").trigger("click");
		});
	
	});
});