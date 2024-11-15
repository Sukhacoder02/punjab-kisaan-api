import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { invalidateSession } from '../services/authService';
import LogoutButton from '../components/LogoutButton';
import LogoutMessage from '../components/LogoutMessage';

const LogoutContainer = () => {
    const [logoutSuccess, setLogoutSuccess] = useState(false);
    const history = useHistory();

    const handleLogout = async () => {
        try {
            // Clear user data from local storage or session storage
            localStorage.removeItem('user');
            sessionStorage.removeItem('user');
            
            // Call the API to invalidate the session
            await invalidateSession();
        } catch (error) {
            console.error('Error logging out:', error);
            // Optionally, handle error (e.g., show a message to the user)
        }
    };

    const redirectUser = () => {
        // Redirect the user to the login page
        history.push('/login');
    };

    const logoutUser = async () => {
        await handleLogout();
        redirectUser();
        setLogoutSuccess(true);
    };
    
    return (
        <div>
            <LogoutButton onClick={logoutUser} />
            {logoutSuccess && <LogoutMessage />}
        </div>
    );
};

export default LogoutContainer;
