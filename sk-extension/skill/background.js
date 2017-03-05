// Utils

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

function timeConverter(UNIX_timestamp){

    var d = new Date(UNIX_timestamp*1000);
    return d.getDate() + '/' + (d.getMonth()+1) + '/' + d.getYear()
}

function row(img_src, title, url) {

    return "<center><div class=\"sk_row\"><img src=\'"+img_src+"\' class=\'course_img\' /><br>" + 
            "<a href=\'"+url+"\''>"+title+"</a></center></tr>"
}

// Design

var app = angular.module('SKSkills', ['ngMaterial']);

    app.config(function($mdThemingProvider) {

    $mdThemingProvider.theme('default')
    .primaryPalette('pink', {
      'default': '400', // by default use shade 400 from the pink palette for primary intentions
      'hue-1': '100', // use shade 100 for the <code>md-hue-1</code> class
      'hue-2': '600', // use shade 600 for the <code>md-hue-2</code> class
      'hue-3': 'A100' // use shade A100 for the <code>md-hue-3</code> class
    })
    // If you specify less than all of the keys, it will inherit from the
    // default shades
    .accentPalette('purple', {
      'default': '200' // use shade 200 for default, and keep all other shades the same
    });

});


window.onload = function() {


var skill = getUrlParameter('name')
    $("#stuff").text(skill) 


// Courses
    var courses_url = "http://185.158.153.129:5002/getCourses?skill="+skill
    $.ajax({
        url:        courses_url,
        dataType:   "json",
        success:    function(data){

            courses = data["recommendations"]
            courses.forEach(function(course) {
                url = course["url"]
                name = course["name"]
                img_src = "http://www.danpontefract.com/wp-content/uploads/2012/05/edx.jpg"//course["img"]

                $("#sk_courses").append( row(img_src,name,url) )
            })
        }
    })

// Books
    var books_url = "http://185.158.153.129:5003/getBooks?skill="+skill
    $.ajax({
        url:        books_url,
        dataType:   "json",
        success:    function(data){

            books = data["recommendations"]
            books.forEach(function(book) {
                url = book["url"]
                name = book["title"]
                img_src = book["image"]

                $("#sk_books").append( row(img_src,name,url) )
            })
        }
    })


// Graphis

var trend_url = "http://185.158.153.129:5001/getTrends?skill="+skill 
$.ajax({
        url:        trend_url,
        dataType:   "json",
        success:    function(data){

          info = data[skill]
          dates = $.map(info, function(v, i){
            return timeConverter(i);
          })
          searches = $.map(info, function(v, i){
            return v;
          });

          var trace = {
            type: 'scatter',                    // set the chart type
            mode: 'lines',                      // connect points with lines
            x: dates,
            y: searches,
            line: {                             // set the width of the line.
              width: 1
            },
          };

          var layout = {
            yaxis: {title: "Trends"},       // set the y axis title
            xaxis: {
              showgrid: false,                  // remove the x-axis grid lines
              tickformat: "%B, %Y"              // customize the date format to "month, day"
            },
            margin: {                           // update the left, bottom, right, top margin
              l: 40, b: 100, r: 10, t: 20
            }
          };

          Plotly.plot(document.getElementById('chart'), [trace], layout, {showLink: false});

        }
      });
}