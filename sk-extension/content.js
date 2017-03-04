function sk_span_skill(element){
	return "<span class=\"sk_skill\">"+element+"</span>"
function sk_span_skill(element, skill_style){
	return "<span class=\""+skill_style+" sk_skill\">"+element+"</span>"
}

function sk_request(query) {
	return "https://api.hh.ru/vacancies/"
}

function sk_resume_request (resume_id) {
	return "https://api.hh.ru/resumes/" + resume_id
}

var search_input = "input.bloko-input"

window.onload = function() {

	let query = $( search_input ).first().val();
	$.getJSON( sk_request(query), function( data ) {

		// var skills = data["requirements"]
		var skills = ["UIKit", "Cocoa Touch", "Objective-C"];


		let resume_id = "fa318ae9ff0314d9a60039ed1f6e623356535a";
		$.getJSON( sk_resume_request(resume_id), function( data ) {

			var resume_skills = data["skill_set"]
			skills.forEach(function(skill) {

				var skill_style = resume_skills.contains(skill) ? "sk_skill_match" : "sk_skill_missed"

				$( ".search-result" ).prepend( sk_span_skill(skill, skill_style) );
			});

		});

	});

}
