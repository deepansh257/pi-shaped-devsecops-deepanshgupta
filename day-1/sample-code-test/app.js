const express = require("express");
const app = express();
const PORT = process.env.PORT || 5000;

// ❌ Hardcoded fake secrets (intentionally for practice)
const DB_PASSWORD = "SuperSecretPassword123";
const API_KEY = "AIzaFakeAPIKey-123456789";
const AWS_SECRET = "aws_secret_key_example_ABC123456";

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
