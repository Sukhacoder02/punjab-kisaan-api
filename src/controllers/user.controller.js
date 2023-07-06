
const UserServices = require('../services/user.service');

const registerNewUser = async (req, res) => {
  const { phone, password } = req.body;
  try {
    const user = await UserServices.registerNewUser(phone, password);
    res.status(201).json({ user });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

const loginUser = async (req, res) => {
  const { phone, password } = req.body;
  try {
    const token = await UserServices.loginUser(phone, password);
    res.status(200).json({ token });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
}

module.exports = { registerNewUser, loginUser };
