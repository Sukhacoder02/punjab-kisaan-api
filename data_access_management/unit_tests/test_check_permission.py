# File: data_access_management/unit_tests/test_check_permission.py

import unittest
from data_access_management.check_permission import check_user_permission, enforce_permissions

class TestCheckPermission(unittest.TestCase):

    def setUp(self):
        # Setting up test data
        self.user_roles = {
            'user1': ['admin', 'editor'],
            'user2': ['viewer'],
            'user3': ['editor', 'viewer']
        }
        
        self.data_permissions = {
            'report1': ['admin', 'editor'],
            'report2': ['viewer'],
            'report3': ['admin']
        }
    
    def mock_get_user_roles(self, user_id):
        # Mock function for get_user_roles
        return self.user_roles.get(user_id, [])

    def mock_get_data_permissions(self, data_id):
        # Mock function for get_data_permissions
        return self.data_permissions.get(data_id, [])
    
    def test_check_user_permission(self):
        # Mocking the functions
        check_user_permission.get_user_roles = self.mock_get_user_roles
        check_user_permission.get_data_permissions = self.mock_get_data_permissions
        
        # Test cases: (user_id, data_id, expected_permission)
        test_cases = [
            ('user1', 'report1', True),
            ('user1', 'report2', False),
            ('user2', 'report2', True),
            ('user2', 'report3', False),
            ('user3', 'report3', False)
        ]
        
        for user_id, data_id, expected in test_cases:
            with self.subTest(user_id=user_id, data_id=data_id, expected=expected):
                self.assertEqual(check_user_permission(user_id, data_id), expected)
    
    def test_enforce_permissions(self):
        # Mocking the functions
        enforce_permissions.get_user_roles = self.mock_get_user_roles
        enforce_permissions.get_data_permissions = self.mock_get_data_permissions
        
        # Define a mock action function
        def mock_action(*args, **kwargs):
            return "Action executed"
        
        # Test cases: (user_id, data_id, should_raise_exception)
        test_cases = [
            ('user1', 'report1', False),
            ('user1', 'report2', True),
            ('user2', 'report2', False),
            ('user2', 'report3', True),
            ('user3', 'report3', True)
        ]
        
        for user_id, data_id, should_raise_exception in test_cases:
            with self.subTest(user_id=user_id, data_id=data_id, should_raise_exception=should_raise_exception):
                if should_raise_exception:
                    with self.assertRaises(PermissionError):
                        enforce_permissions(user_id, data_id, mock_action)
                else:
                    self.assertEqual(enforce_permissions(user_id, data_id, mock_action), "Action executed")

if __name__ == '__main__':
    unittest.main()
