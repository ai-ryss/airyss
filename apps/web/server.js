const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('AIryss Web Placeholder');
});

server.listen(3000, () => {
  console.log('web listening on port 3000');
});
