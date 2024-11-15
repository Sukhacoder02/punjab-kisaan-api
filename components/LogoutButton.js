// components/LogoutButton.js

import React from 'react';
import PropTypes from 'prop-types';

const LogoutButton = ({ handleLogout }) => {
  // Handler for the logout button click event
  const onLogoutClick = () => {
    try {
      handleLogout();
    } catch (error) {
      console.error('Logout failed: ', error);
    }
  };

  return (
    <button onClick={onLogoutClick} className="logout-button">
      Logout
    </button>
  );
};

LogoutButton.propTypes = {
  handleLogout: PropTypes.func.isRequired,
};

export default LogoutButton;
