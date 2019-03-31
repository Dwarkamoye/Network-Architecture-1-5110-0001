var net = require('net');
var sockets = [];
var server = net.createServer(function(socket){
sockets.push(socket);
});
server.on('connection', handleConnection);
server.listen(3000,'128.171.8.120', function() {
  console.log('Server listening to %j', server.address());
});
function handleConnection(conn) {  
  var remoteAddress = conn.remoteAddress + ':' + conn.remotePort;
  console.log('New client connection from %s', remoteAddress);
  conn.setEncoding('utf8');
  conn.on('data', onConnData);
  conn.once('close', onConnClose);
  conn.on('error', onConnError);
  function onConnData(data) {
    console.log('Connection data from %s: %j', remoteAddress, data);
    for (var i = 0; i < sockets.length; i++){
            if (sockets[i] === conn) continue;
            sockets[i].write(data.toString());
        }
  }
  function onConnClose() {
    console.log('Connection from %s closed', remoteAddress);
  }
  function onConnError(err) {
    console.log('Connection %s error: %s', remoteAddress, err.message);
  }
}
