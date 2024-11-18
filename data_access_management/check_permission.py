import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_user_permission(user_id, data_id):
    """
    This function checks if the user has permission to access the requested data.
    
    Args:
        user_id (str): The ID of the user requesting access.
        data_id (str): The ID of the data being accessed.
    
    Returns:
        bool: True if the user has permission, False otherwise.
    """
    try:
        user_roles = get_user_roles(user_id)
        data_permissions = get_data_permissions(data_id)

        if not user_roles or not data_permissions:
            logger.debug(f"User roles: {user_roles}, Data permissions: {data_permissions}")
            return False
        
        for role in user_roles:
            if role in data_permissions:
                return True
        
        return False

    except Exception as e:
        logger.error(f"Error checking user permissions: {e}")
        return False

def get_user_roles(user_id):
    """
    Retrieve the roles for a given user.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        list: A list of roles associated with the user.
    """
    # This function should interface with the database or authorization service to get user roles
    # Example implementation; replace with actual data source access
    try:
        # Mocked data for the purpose of this example
        user_roles_mapping = {
            "user_1": ["admin", "editor"],
            "user_2": ["viewer"],
            "user_3": ["editor", "viewer"]
        }

        return user_roles_mapping.get(user_id, [])
    except KeyError:
        logger.error(f"No roles found for user_id: {user_id}")
        return []

def get_data_permissions(data_id):
    """
    Retrieve the permissions associated with a given data.
    
    Args:
        data_id (str): The ID of the data.
    
    Returns:
        list: A list of roles that are allowed to access the data.
    """
    # This function should interface with the database or authorization service to get data permissions
    # Example implementation; replace with actual data source access
    try:
        # Mocked data for the purpose of this example
        data_permissions_mapping = {
            "data_1": ["admin", "editor"],
            "data_2": ["viewer"],
            "data_3": ["admin"]
        }

        return data_permissions_mapping.get(data_id, [])
    except KeyError:
        logger.error(f"No permissions found for data_id: {data_id}")
        return []

def enforce_permissions(user_id, data_id):
    """
    This function enforces the access permissions and allows or denies access based on the check result.
    
    Args:
        user_id (str): The ID of the user requesting access.
        data_id (str): The ID of the data being accessed.
    
    Returns:
        bool: True if access is allowed, False otherwise.
    """
    has_permission = check_user_permission(user_id, data_id)
    
    if has_permission:
        logger.info(f"Access granted for user {user_id} to data {data_id}")
        return True
    else:
        logger.warning(f"Access denied for user {user_id} to data {data_id}")
        return False
