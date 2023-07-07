const express = require('express');
const dotenv = require('dotenv');
const userRouter = require('./routes/user.routes');
dotenv.config();

const PORT = process.env.PORT || 1313;
const app = express();
app.use(express.json());

app.use('/api/v1', userRouter);

app.listen(PORT, () => {
  console.log(`Server is running on  http://localhost:${PORT}`);
});
