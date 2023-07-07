const { Router } = require('express');
const UserController = require('../controllers/user.controller');
const userRouter = Router();

userRouter.get('/health-check', (req, res) => {
  res.send('Server healthy');
});

userRouter.post('/users/register', UserController.registerNewUser);
userRouter.post('/users/login', UserController.loginUser);

module.exports = userRouter;
