const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post("/getText", (req, res) => {
  const { text } = req.body;
  console.log("Received text:", text);

  // Make a POST request to the Flask server
  axios
    .post("http://localhost:5000/processText", { text: text })
    .then((response) => {
      console.log("Intent Detected :" + response.data);
      res.send("Text processed successfully"); // Send response after processing
    })
    .catch((error) => {
      console.error(error);
      res.status(500).send("Error occurred during text processing"); // Send error response if request to Flask server fails
    });
});

app.listen(4000, () => {
  console.log(`App running on port 4000`);
});
