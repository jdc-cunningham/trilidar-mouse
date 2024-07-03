let socketInterval = null;
let socket = null;
let wasConnected = false;

const socketStatus = document.getElementById('status');

const connectToRaspberryPi = () => {
  socket = new WebSocket('ws://192.168.1.104:8000'); // raspberry pi

  // connection opened, send messages to robot
  socket.addEventListener('open', function (event) {
    socketStatus.innerText = 'connected'
 
    // keep connection to esp01 alivew
    socketInterval = setInterval(() => {
      socket.send('poll');
    }, 100);
  });
 
  // listen for messages from floating navigation sensor assembly
  socket.addEventListener('message', function (event) {
    const msg = event.data;
    updateCursor(msg);
  });
 
  socket.addEventListener('close', function (event) {
    socketStatus.innerText = wasConnected ? 'connection lost, reconnecting...' : 'failed to connect, connecting...';
    clearInterval(socketInterval);
  });

  socket.addEventListener('error', function (event) {
    socketStatus.innerText = 'error connecting, trying again...';
    clearInterval(socketInterval);

    setTimeout(() => {
      connectToRaspberryPi();
    }, 1000);
  });
}

connectToRaspberryPi();