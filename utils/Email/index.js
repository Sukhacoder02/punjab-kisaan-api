const nodemailer = require('nodemailer');


const transporter = nodemailer.createTransport({
  host: 'smtp.mailgun.org',
  port: 587,
  auth: {
    user: process.env.MAIL_ID,
    pass: process.env.MAIL_PASS
  },
});

const sendEmail = async (recepientEmail, otp) => {
  const mailOptions = {
    from: 'punjab@kisaan.com',
    to: recepientEmail,
    subject: 'Password Reset',
    html: `<html>
             <body>
               <h2>Password Recovery</h2>
               <p>Use this OTP to reset your password. OTP is valid for 1 minute</p>
               <h3>${otp}</h3>
             </body>
           </html>`
  };
  const result = await transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      throw error;
    } else {
      return info;
    }
  });
  return result;
};

const EmailServices = { sendEmail };
module.exports = EmailServices;