
const UserServices = require('../services/user.service');

const registerNewUser = async (req, res) => {
  const { phone, password } = req.body;
  try {
    const user = await UserServices.registerNewUser(phone, password);
    res.statusCode(201).json({ user });
  } catch (error) {
    res.statusCode(400).json({ error: error.message });
  }
};

module.exports = { registerNewUser };
