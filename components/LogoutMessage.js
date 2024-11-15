import React from 'react';
import PropTypes from 'prop-types';

const LogoutMessage = ({ message }) => {
  return (
    <div className="logout-message">
      {message}
    </div>
  );
};

LogoutMessage.propTypes = {
  message: PropTypes.string
};

LogoutMessage.defaultProps = {
  message: 'You have successfully logged out.'
};

export default LogoutMessage;
