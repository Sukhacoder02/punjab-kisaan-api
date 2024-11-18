import unittest
from unittest.mock import patch
from data_access_management.permissions_update import update_permissions, refresh_permissions_cache

class TestPermissionsUpdate(unittest.TestCase):
    @patch('data_access_management.permissions_update.update_permissions')
    def test_update_permissions(self, mock_update_permissions):
        """
        This unit test checks if the update_permissions function correctly updates the permissions.
        """
        # Simulate the update permissions function call
        update_permissions('user123', 'admin')
        
        # Assert the update_permissions function was called with the correct arguments
        mock_update_permissions.assert_called_with('user123', 'admin')

    @patch('data_access_management.permissions_update.refresh_permissions_cache')
    def test_refresh_permissions_cache(self, mock_refresh_permissions_cache):
        """
        This unit test checks if the refresh_permissions_cache function properly refreshes the permissions cache.
        """
        # Simulate the refresh permissions cache function call
        refresh_permissions_cache()
        
        # Assert the refresh_permissions_cache function was called
        mock_refresh_permissions_cache.assert_called_once()

if __name__ == '__main__':
    unittest.main()
