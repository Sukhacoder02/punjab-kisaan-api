// pages/LoginPage.js

import React from 'react';
import { useHistory } from 'react-router-dom';
import { Button } from '@material-ui/core';

const LoginPage = () => {
  const history = useHistory();

  const displayLoginPage = () => {  
    // Sample Implementation for rendering the login UI. Can be customized further
    return (
      <div className="login-page">
        <h1>Login</h1>
        <form>
          <input
            type="text"
            placeholder="Enter your username"
            name="username"
            required
          />
          <input
            type="password"
            placeholder="Enter your password"
            name="password"
            required
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
          >
            Login
          </Button>
        </form>
      </div>
    )
  };

  return displayLoginPage();
};

export default LoginPage;
