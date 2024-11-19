import re
from datetime import datetime, timedelta
from uuid import uuid4

# Assumed external utility functions for the tasks specified
def find_user_by_token(reset_token):
    # Function to find user by reset token
    pass

def hash_password(password):
    # Function to hash the password
    pass

def save_new_password(user_id, hashed_password):
    # Function to save new password for the user
    pass

def log_password_reset(user_id, timestamp):
    # Function to log the password reset event
    pass

def validate_password(password):
    """
    Validate the new password based on certain criteria.
    Criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase characters
    - Contains at least one numerical digit
    - Contains at least one special character
    """
    if (len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) 
        or not re.search("[0-9]", password) or not re.search("[@#$%^&+=]", password)):
        return False
    return True

def update_password(reset_token, new_password):
    """
    This function will allow the user to set a new password after the reset link is validated.
    
    Args:
    reset_token (str): The token received for password reset verification.
    new_password (str): The new password provided by the user.
    
    Returns:
    dict: Result of the password update process.
    """
    # Validate the password follows the security guidelines
    if not validate_password(new_password):
        return {'status': 'error', 'message': 'Password does not meet the security criteria.'}
    
    # Find the user by reset token
    user = find_user_by_token(reset_token)
    
    if not user:
        return {'status': 'error', 'message': 'Invalid or expired password reset token.'}
    
    # Hash the new password
    hashed_password = hash_password(new_password)
    
    if not hashed_password:
        return {'status': 'error', 'message': 'Failed to hash the new password.'}
    
    # Save the new password for the user
    if not save_new_password(user['id'], hashed_password):
        return {'status': 'error', 'message': 'Failed to save the new password.'}
    
    # Log the password reset event
    timestamp = datetime.now().isoformat()
    log_password_reset(user['id'], timestamp)
    
    return {'status': 'success', 'message': 'Password has been updated successfully.'}
