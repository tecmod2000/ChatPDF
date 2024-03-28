require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
const port = 3000;

const genAI = new GoogleGenerativeAI(process.env.API_KEY);

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Middleware to serve static files from the 'public' directory
app.use(express.static("public"));

// Serve HTML Webpage to the user on Page Load
app.get("/", (req, res) => {
  res.sendFile("index.html", { root: "public" });
});
// Handle sentiment analysis when the form is submitted
app.post("/analyze", async (req, res) => {
  try {
    const userInput = req.body.text;

    // Call Gemini API for sentiment analysis
    const geminiResponse = await run(userInput);

    const sentimentResult = geminiResponse;

    // Send sentiment result back to the client
    res.send(sentimentResult);
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).send("Internal Server Error");
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

// Basic Function API to generate content/result using Gemini
async function run(userInput) {
  // For text-only input, use the gemini-pro model
  const model = genAI.getGenerativeModel({ model: "gemini-pro" });

  const prompt = `Analyze the sentiment of the sentence given below.\n${userInput}\nThe output should be in the format- Semtiment: Value`;

  const result = await model.generateContent(prompt);
  const response = await result.response;
  const text = response.text();
  return text;
}

