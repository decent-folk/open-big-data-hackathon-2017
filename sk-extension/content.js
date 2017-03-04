function sk_span_skill(element){
	return "<span class=\"sk_skill\">"+element+"</span>"
}


var search_input = "input.bloko-input"

window.onload = function() {

	query = $( search_input ).first().val()

	$.getJSON( "https://api.hh.ru/vacancies/", function( data ) {

		// var skills = data["requirements"]
		var skills = ["UIKit", "Cocoa Touch", "Objective-C"];

		skills.forEach(function(skill) {
			$( ".search-result" ).prepend( sk_span_skill(skill) );
		});
	});
}
