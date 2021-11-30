module.exports = {
    insert: function (table, values, connection) {
        let q = "INSERT INTO " + table + " VALUES("
        for(i=0;i<values.length-1;i++){
            q = q + values[i].toString() + ',';
        }
        q = q + values[values.length-1].toString() + ');';
        connection.query(q, function(err, rows, fields) {
            if (err) throw err;
          });
        console.log('Inserted data on ' + table + ' with query: ' + q)
    },
    getlast: function (table, connection) {
        let q = "SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1;"
        let result;
        connection.query(q, function(err, rows, fields) {
            if (err) throw err;
            return rows[0]
          });
    }
  };
