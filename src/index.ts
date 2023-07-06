import express, { Request, Response } from 'express';
import dotenv from 'dotenv';
import v1Router from './routes';
dotenv.config();

const PORT = process.env.PORT || 1313;
const app = express();
app.use(express.json());

app.use('/api/v1', v1Router);

app.get('/', (req: Request, res: Response) => {
  res.send('Hello World!');
});

app.listen(PORT, () => {
  console.log(`Server is running on  http://localhost:${PORT}`);
});
