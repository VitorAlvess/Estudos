//importar dep

const express = require('express');
const path = require('path');
const pages = require('./pages.js');

//inicir o express
const server = express();
// utilizando os arq estaticos
server
    .use(express.static('public'))

    // conf template engine
    .set('views', path.join(__dirname, "views"))
    .set('view engine', 'hbs')
    // rotas da aplicação
    .get('/', pages.index)
    .get('/orphanages', pages.orphanages)
    .get('/orphanage', pages.orphanage)
    .get('/create-orphanage', pages.createOrphanage)
    

        
     
    

//ligar servidor
server.listen(5500)