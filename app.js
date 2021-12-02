const express = require('express')
var mysql      = require('mysql');
var functions = require('./functions')
const app = express()
const port = 3000

/*
EXEMPLE INSERCIÓ DE DADES: functions.insert('autobus_parada', [3,'NULL','NULL',"'L36'"], connection)
*/

var connection = mysql.createConnection({
    user     : 'root',
    password: 'Sciotra1234',
    host     : 'localhost',
    database: 'bbdd'
});
connection.connect();
app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

//EN PROCESO...
app.get('/last', (req, res) => {
  let result = functions.getlast('autobus_bus', connection)
  functions.getlast('autobus_bus', connection, function(result){
    console.log(result);
    res.send('ok  ' + result);
  });
})


functions.insert('autobus_bus', [0,1,3,"'L36'",'NULL'], connection)
