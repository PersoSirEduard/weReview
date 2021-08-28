const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());

require("./routes")(app);

const PORT = process.env.PORT || 5555;
app.listen(PORT, () => console.log("API is up and running!"));