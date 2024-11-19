# password_recovery/validate_reset_link.py

import jwt
from datetime import datetime
from some_database_module import get_user_by_token
from some_config_module import SECRET_KEY

def decode_reset_token(token):
    """
    Decodes the JWT reset token using the application's secret key.
    Returns the decoded payload if the token is valid, raises an error otherwise.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("The token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("The token is invalid.")

def check_token_expiry(decoded_token):
    """
    Checks whether the token is expired based on the 'exp' field in the decoded token.
    """
    exp_timestamp = decoded_token.get('exp')
    if not exp_timestamp:
        raise ValueError("The token does not contain an expiry timestamp.")
    if datetime.utcnow().timestamp() > exp_timestamp:
        raise ValueError("The token has expired.")

def find_user_by_token(decoded_token):
    """
    Retrieves the user associated with the reset token from the database.
    """
    user_id = decoded_token.get('sub')
    if not user_id:
        raise ValueError("The token does not contain a user id.")
    
    user = get_user_by_token(user_id)
    if not user:
        raise ValueError("No user found corresponding to the token.")
    return user

def validate_reset_link(reset_token):
    """
    Validates the reset link by decoding the token, checking its expiry,
    and confirming the user exists.
    """
    try:
        decoded_token = decode_reset_token(reset_token)
        check_token_expiry(decoded_token)
        user = find_user_by_token(decoded_token)
        return user
    except ValueError as e:
        print(f"Error validating reset link: {e}")
        return None
