window.onload = function() {

	let query = SK.search_input().val();
	console.log( SK.request(query) )
	$.ajax({
            url:        SK.request(query),
            dataType:   "json",
            success:    function(data){

            	console.log( query );

                var skills = data["requirements"]
				// var skills = ["UIKit", "Cocoa Touch", "Objective-C", "ООП", "Crashlytics"];

				let resume_id = "fa318ae9ff0314d9a60039ed1f6e623356535a";
				$.getJSON( SK.resume_request(resume_id), function( data ) {

					var resume_skills = data["skill_set"]
					skills.forEach(function(skill) {

						var skill_style = resume_skills.contains(skill) ? "sk_skill_match" : "sk_skill_missed"

						SK.search_results().prepend( SK.span_skill(skill, skill_style) );
					});
				});
            },
            error: function(jqXHR, textStatus, errorThrown) {
            	console.log(jqXHR.status);
            	console.log(textStatus);
            }/*,
            headers: {'Host': kServerURL}*/
        });
}
