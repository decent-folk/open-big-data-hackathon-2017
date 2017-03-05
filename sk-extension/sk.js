const kSearchInput = "input.bloko-input"
const kSearchResults = ".search-result"
const kServerURL = "http://185.158.153.129:5000"

class SK {}

SK.span_skill = function (element, skill_style){
	return "<a href=\"#\"><span class=\""+skill_style+" sk_skill\">"+element+"</span></a>"
}

SK.request = function(query) {
	// return "https://api.hh.ru/vacancies/"
	return kServerURL+"/getRequirements?name="+query
}

SK.resume_request = function (resume_id) {
	return "https://api.hh.ru/resumes/" + resume_id
}

SK.loading_view = function () {
	return "<span id=\"loading_view\">Загружаем большие данные...</span>"
}

SK.search_input = function() {
	return $( kSearchInput ).first()
}

SK.search_results = function() {
	return $( kSearchResults ).first()
}