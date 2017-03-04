function sk_span_skill(element){
	return "<span class=\"sk_skill\">"+element+"</span>"
}

function sk_request(query) {
	return "https://api.hh.ru/vacancies/"
}

function sk_resume_request (resume_id) {
	return "https://api.hh.ru/resumes/" + resume_id
}

var search_input = "input.bloko-input"

window.onload = function() {

	query = $( search_input ).first().val()

	$.getJSON( sk_request(query), function( data ) {

		// var skills = data["requirements"]
		var skills = ["UIKit", "Cocoa Touch", "Objective-C"];

		skills.forEach(function(skill) {
			$( ".search-result" ).prepend( sk_span_skill(skill) );
		});
	});
}
