import unittest
from unittest.mock import patch, MagicMock
from password_recovery.send_reset_email import request_password_reset

class TestSendResetEmail(unittest.TestCase):
    
    @patch('password_recovery.send_reset_email.validate_email_address')
    @patch('password_recovery.send_reset_email.generate_reset_token')
    @patch('password_recovery.send_reset_email.send_email')
    def test_request_password_reset_valid_email(self, mock_send_email, mock_generate_token, mock_validate_email):
        # Sample data
        email = "user@example.com"
        
        # Mock the return values for external dependencies
        mock_validate_email.return_value = True
        mock_generate_token.return_value = "sample_reset_token"
        mock_send_email.return_value = None

        # Call the function under test
        response = request_password_reset(email)
        
        # Check that validate_email_address was called once with the correct email
        mock_validate_email.assert_called_once_with(email)
        
        # Check that generate_reset_token was called once
        mock_generate_token.assert_called_once()
        
        # Check that send_email was called once with the correct arguments
        mock_send_email.assert_called_once_with(email, "sample_reset_token")
        
        # Check the response is as expected
        self.assertTrue(response['success'])
        self.assertEqual(response['message'], 'Password reset email sent successfully.')

if __name__ == '__main__':
    unittest.main()
