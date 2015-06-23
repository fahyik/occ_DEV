$(document).ready(function(){
	
	$("#db_toggle_charts").click(function(){
		$("#charts").toggleClass("hidden");
		if ( $(this).html() == "Show") {
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

});