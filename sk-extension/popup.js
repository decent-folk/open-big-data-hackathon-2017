var access_token = "I2Q9RRFVJT0HMUP9OBN9JKF5K5C0EK0KUQN0P2SDTI3S21NBNOGKV2FTMO0B5NN0"

document.addEventListener('DOMContentLoaded', function() {
  var skSignIn = document.getElementById('sk_sign_in');
  skSignIn.addEventListener('click', function() {

      d = document;
      var f = d.createElement('form');
      f.action = 'http://gtmetrix.com/analyze.html?bm';
      f.method = 'post';
      var i = d.createElement('input');
      i.type = 'hidden';
      i.name = 'url';
      i.value = tab.url;
      f.appendChild(i);
      d.body.appendChild(f);
      f.submit();

  }, false);
}, false);