    const express = require('express');
    const app = express();
    const port = 3000; // You can choose any available port

    app.get('/', (req, res) => {
      res.send('Hello World from Express!');
    });

    app.listen(port, () => {
      console.log(`Express app listening at http://localhost:${port}`);
    });