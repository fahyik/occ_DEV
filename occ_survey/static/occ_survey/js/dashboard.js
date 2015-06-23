$(document).ready(function(){
	
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