const express = require('express');
const path = require('path');
const app = express();

// Serve static files (e.g., your compiled React app)
app.use(express.static(path.join(__dirname, 'build')));

// Handle all other routes by serving the main HTML file
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Start the server
const port = process.env.PORT || 3001;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
