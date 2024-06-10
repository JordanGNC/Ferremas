//localhost
//ejecutar en cmd: node server.js

const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 8000;

const server = http.createServer((req, res) => {
  let filePath;

  // Determina qué archivo HTML servir en función de la URL solicitada
  if (req.url === '/' || req.url === '/index.html') {
    filePath = path.join(__dirname, 'index.html');
  } else if (req.url === '/logistica' || req.url === '/logistica.html') {
    filePath = path.join(__dirname, 'logistica.html');
  } else {
    filePath = null;
  }

  // Sirve el archivo correspondiente o muestra un error 404 si no se encuentra
  if (filePath) {
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Error loading the file');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});