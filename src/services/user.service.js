const HashingUtils = require('../../utils/Hashing');
const db = require('../database/models');

const registerNewUser = async (phone, password) => {
  // check if the phone number is already registered
  const foundUser = await db.user.findOne({
    where: {
      phone
    }
  });
  if (foundUser) {
    throw new Error('User already Exists');
  }
  // create a new user
  // generate a hash of the password
  const hashedPassword = await HashingUtils.encryptPassword(password);

  const newUser = await db.user.create({
    phone,
    password: hashedPassword,
  });
  return newUser;
};

module.exports = { registerNewUser };
