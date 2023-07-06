const { Router } = require('express');
const UserController = require('../controllers/user.controller');
const v1Router = Router();

v1Router.get('/health-check', (req, res) => {
  res.send('Server healthy');
});

v1Router.post('/users/register', UserController.registerNewUser);

module.exports = v1Router;
