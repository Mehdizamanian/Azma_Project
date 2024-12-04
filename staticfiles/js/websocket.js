var socket = new WebSocket('ws://' + window.location.hostname + ':8000/ws/');

    socket.onopen = function() {
      console.log('WebSocket connection established.');
    };

    socket.onmessage = function(e) {
      var message = e.data;
      document.querySelector('#echo-log').value += (message + '\n');
    };

    socket.onclose = function(e) {
      console.error('WebSocket connection closed unexpectedly');
    };

    document.querySelector('#text-input').focus();
    document.querySelector('#text-input').onkeyup = function(e) {
      if (e.keyCode === 13) { // Enter key
        document.querySelector('#text-submit').click();
      }
    };

    document.querySelector('#text-submit').onclick = function() {
      var messageInputDom = document.querySelector('#text-input');
      var message = messageInputDom.value;
      socket.send(message);
      messageInputDom.value = '';
    };