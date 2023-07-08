
const UserServices = require('../services/user.service');

const registerNewUser = async (req, res) => {
  const { phone, password, email } = req.body;
  try {
    const user = await UserServices.registerNewUser(phone, password, email);
    res.status(201).json({ message: 'User registered successfully', user });
  } catch (error) {
    res.status(400).json({ message: 'Error!', error: error.message });
  }
};

const loginUser = async (req, res) => {
  const { phone, password } = req.body;
  try {
    const token = await UserServices.loginUser(phone, password);
    res.status(200).json({ message: 'Login Successful', token });
  } catch (error) {
    res.status(400).json({ message: 'Error', error: error.message });
  }
}
const forgotPassword = async (req, res) => {
  const { email, phone, otp } = req.body;
  try {
    await UserServices.sendEmail(email, phone, otp);
    res.json({
      message: 'Email sent successfully'
    })
  } catch (error) {
    res.status(400).json({ message: 'Error', error: error.message });
  }
};

module.exports = { registerNewUser, loginUser, forgotPassword };
