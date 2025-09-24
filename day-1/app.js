const express = require("express");
const app = express();
const PORT = process.env.PORT || 5000;

// AWS Access Key (valid pattern)
const DB_PASSWORD = "SuperSecretPassword123";

// AWS Secret Key (valid pattern - 40 chars)
const API_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

// Google API Key (valid pattern - 39 chars after AIza)
const AWS_SECRET = "AIzaSyA-1234567890abcdefghijklmnopqrstuvwx";

// Basic endpoint
app.get("/", (req, res) => {
  res.send("Hello from Sample Node.js App! 🚀");
});

// Endpoint using a fake API key
app.get("/api", (req, res) => {
  res.json({
    message: "This is a fake API response",
    apiKey: API_KEY
  });
});

app.listen(PORT, () => {
  console.log(`App running on http://localhost:${PORT}`);
});
