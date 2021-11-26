const express = require('express')
var mysql      = require('mysql');
const app = express()
const port = 3000
var connection = mysql.createConnection({
    user     : 'root',
    password: 'root',
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

