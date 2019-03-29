const login = document.getElementById('log_in');
console.log(login);
login.onclick = function(e) {
	let xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      console.log(xmlHttp.responseText);
    }
	}
	xmlHttp.open("GET", '/login', true); // true for asynchronous
	xmlHttp.send(null);
}
const singup = document.getElementById('sing_up');
