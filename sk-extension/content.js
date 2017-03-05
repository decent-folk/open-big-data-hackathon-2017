window.onload = function() {

	let query = SK.search_input().val();
	console.log( SK.request(query) )
	$.ajax({
            url:        SK.request(query),
            dataType:   "json",
            success:    function(data){

                var skills = data["requirements"]
				// var skills = ["UIKit", "Cocoa Touch", "Objective-C", "ООП", "Crashlytics"];

				SK.search_results().prepend( SK.skill_container_html() );
				SK.skill_container_view().prepend( SK.loading_html() );

				let resume_id = "fa318ae9ff0314d9a60039ed1f6e623356535a";
				$.getJSON( SK.resume_request(resume_id), function( r_data ) {

					var resume_skills = r_data["skill_set"]
					skills.forEach(function(skill) {

						var skill_style = "sk_skill_missed"

						resume_skills.forEach(function(resume_skill) {

							// $.getJSON( kServerURL+"/getDistance?a="+skill[0]+"&b="+resume_skill, function( distance ) {

							// 	skill_style = distance < 4 ? "sk_skill_match" : "sk_skill_missed"

							// })
						})

						SK.skill_container_view().append( SK.span_skill(skill, skill_style) );
					});
					SK.loading_view().hide();
				});
            },
            error: function(jqXHR, textStatus, errorThrown) {
            	console.log(jqXHR.status);
            	console.log(textStatus);
            }/*,
            headers: {'Host': kServerURL}*/
        });
}
