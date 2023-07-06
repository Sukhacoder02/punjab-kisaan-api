const jwt = require('jsonwebtoken');
const JWT_SECRET = process.env.JWT_SECRET || 'secret';

const generateToken = async (user) => {
  const payload = {
    date: Date(),
    phone: user.phone
  };
  const token = await jwt.sign(payload, JWT_SECRET, {
    expiresIn: '7d'
  });
  return token;
}

const verifyToken = async (token) => {
  const decoded = await jwt.verify(token, JWT_SECRET);
  if (!decoded) return null;
  return decoded;
}

const JWTUtils = { generateToken, verifyToken };
module.exports = JWTUtils;