// services/authService.js

// Import necessary modules
import axios from 'axios';

// Define the base URL for the authentication API
const API_BASE_URL = 'https://your-api-endpoint.com/auth';

// Function to invalidate the user's session
export const invalidateSession = async () => {
    try {
        // Make an API call to invalidate the session
        const response = await axios.post(`${API_BASE_URL}/logout`);
        
        // Check if the response status indicates a successful operation
        if (response.status === 200) {
            return {
                success: true,
                message: 'Session invalidated successfully.'
            };
        } else {
            return {
                success: false,
                message: 'Failed to invalidate session. Please try again.'
            };
        }
    } catch (error) {
        // Handle any errors during the API call
        console.error('Error invalidating session:', error);
        
        // Return an error response
        return {
            success: false,
            message: 'An error occurred while invalidating the session.'
        };
    }
};
