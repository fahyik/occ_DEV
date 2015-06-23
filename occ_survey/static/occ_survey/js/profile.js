$(document).ready(function(){
	// code to make sure all radio buttons are checked
	var array = [];
	var name = "";
	var count;
   
	$("#profile-survey input:radio").each( function(){

		if ($(this).attr("name") != name ) {
			name = $(this).attr("name");
			array.push(name);
		}

		count = array.length;

		//$("#debug").text(count);
	});
	
	$("#profile-survey input:radio").click(function(){
		var n = $( "#profile-survey input:radio:checked" ).length;
		if (n == count) {
            $('#profile-submit').removeAttr('disabled');
        } 
        else {
            $('#profile-submit').attr('disabled', 'disabled');
        }
	});
	// endcode

});