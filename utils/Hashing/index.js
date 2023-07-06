const bcrpyt = require('bcrypt');

const encryptPassword = async (passwordString) => {
  const salt = await bcrpyt.genSalt(10);
  const hashedPassword = await bcrpyt.hash(passwordString, salt);
  return hashedPassword;
};

const comparePassword = async (password, hashedPassword) => {
  const isMatch = await bcrpyt.compare(password, hashedPassword);
  return isMatch;
};

const HashingUtils = { encryptPassword, comparePassword };
module.exports = HashingUtils;