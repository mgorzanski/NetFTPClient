function App() {
  this.currentDir = null;
  this.list = null;
}

App.scrollServerLog = function() {
  window.setInterval(function() {
    var elem = document.getElementById("server-log-tab");
    elem.scrollTop = elem.scrollHeight;
  }, 500);
}

App.getList = function() {
  var xhr = new XMLHttpRequest();
  var url = "/event/json/default";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      this.list = response.message;
      console.log(this.list);
    }
  }
  var data = JSON.stringify({"action": "get_list"});
  xhr.send(data);
}

App.getList();

App.getCurrentDir = function() {
  var xhr = new XMLHttpRequest();
  var url = "/event/json/default";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      this.currentDir = response.message;
    }
  }
  var data = JSON.stringify({"action": "pwd"});
  xhr.send(data);
}

App.disconnect = function() {
  var xhr = new XMLHttpRequest();
  var url = "/event/json/default";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      if(response.action == "goto_disconnect") {
        window.location.href = "/disconnect";
      }
    }
  }
  var data = JSON.stringify({"action": "disconnect"});
  xhr.send(data);
}

App.scrollServerLog();
App.getCurrentDir();

var disconnectBtn = document.getElementById('disconnect-btn');

disconnectBtn.addEventListener("click", App.disconnect);
