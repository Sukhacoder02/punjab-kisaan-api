const express = require('express');
const dotenv = require('dotenv');
const v1Router = require('./routes/v1.routes');
dotenv.config();

const PORT = process.env.PORT || 1313;
const app = express();
app.use(express.json());

app.use('/api/v1', v1Router);

app.listen(PORT, () => {
  console.log(`Server is running on  http://localhost:${PORT}`);
});
