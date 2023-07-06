const HashingUtils = require('../../utils/Hashing');
const db = require('../database/models');
const JWTUtils = require('../../utils/JWT');

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

const loginUser = async (phone, password) => {
  // check if the user has registered or not
  const foundUser = await db.user.findOne({
    phone
  });
  if (!foundUser) {
    throw new Error('User not found');
  }
  // compare the password
  const isPasswordValid = await HashingUtils.comparePassword(password, foundUser.password);
  if (!isPasswordValid) {
    throw new Error('Invalid Password');
  }
  const token = JWTUtils.generateToken(foundUser);
  return token;
};

module.exports = { registerNewUser, loginUser };
