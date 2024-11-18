# support/features.py

import os
from authentication.login import authenticate_user, login_error_message

def access_support_features(username, password):
    """
    This function will grant access to the support features upon successful login.
    
    :param username: str
    :param password: str
    :return: str
    """
    try:
        user_authenticated = authenticate_user(username, password)
        if user_authenticated:
            # Here we would normally grant access to secured support features.
            return "Access Granted. Welcome to the support features."
        else:
            return login_error_message()
    except Exception as e:
        # Log the exception here, in real-world applications you would use a logger
        print(f"An error occurred: {e}")
        return "An error occurred while attempting to access support features."

# Example test cases (to be moved to appropriate test files)
if __name__ == "__main__":
    # Mock the authenticate_user function for testing purposes
    def mock_authenticate_user(username, password):
        return username == "validuser" and password == "validpassword"
    
    authenticate_user = mock_authenticate_user
    def mock_login_error_message():
        return "Invalid credentials. Please try again."
    
    login_error_message = mock_login_error_message

    # Test with valid credentials
    print(access_support_features("validuser", "validpassword"))    # Should return "Access Granted. Welcome to the support features."

    # Test with invalid credentials
    print(access_support_features("invaliduser", "invalidpassword")) # Should return "Invalid credentials. Please try again."
