require("dotenv").config();
const express = require("express");
const multer = require('multer');
const { exec } = require('child_process');
const bodyParser = require("body-parser");
const { GoogleGenerativeAI } = require("@google/generative-ai");


const app = express();
const port = 3000;
const genAI = new GoogleGenerativeAI(process.env.API_KEY)
const upload = multer({ dest: 'uploads/' });

// Middleware to parse incoming JSON requests
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Middleware to serve static files from the 'public' directory
app.use(express.static("public"));

// Serve HTML Webpage to the user on Page Load
app.get("/", (req, res) => {
  res.sendFile("index.html", { root: "public" });
});

// Handle PDF analysis when the form is submitted
app.post("/analyze", upload.single('file'), (req, res) => {
    const filePath = req.file.path;

    exec(`python3 analyze.py ${filePath}`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        res.send(stdout);
    });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});