import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import LogoutContainer from '../containers/LogoutContainer';
import * as authService from '../services/authService';
import LoginPage from '../pages/LoginPage';
import * as Storage from '../utils/storage'; // assuming there's a storage utility for handling local/session storage

jest.mock('../services/authService');
jest.mock('../pages/LoginPage');
jest.mock('../utils/storage');

describe('LogoutContainer', () => {
    beforeEach(() => {
        authService.invalidateSession.mockClear();
        Storage.clearUserData.mockClear();
        LoginPage.displayLoginPage.mockClear();
    });

    test('testHandleLogout: correctly clears user data and calls invalidateSession', async () => {
        const { handleLogout } = render(<LogoutContainer />).container;

        // Trigger handleLogout function
        await handleLogout();

        // Check if the user data is cleared
        expect(Storage.clearUserData).toHaveBeenCalled();

        // Check if invalidateSession function is called
        expect(authService.invalidateSession).toHaveBeenCalled();
    });

    test('testRedirectUser: correctly redirects the user to the login page', () => {
        const { redirectUser } = render(<LogoutContainer />).container;

        // Trigger redirectUser function
        redirectUser();

        // Check if the user is redirected to the login page
        expect(LoginPage.displayLoginPage).toHaveBeenCalled();
    });

    test('testLogoutUser: correctly combines handleLogout and redirectUser functions, and triggers the display of the LogoutMessage component', async () => {
        const { logoutUser } = render(<LogoutContainer />).container;

        // Mock setState function to simulate setting state in the container
        const setState = jest.fn();
        React.useState = jest.fn(() => ["", setState]);

        // Trigger logoutUser function
        await logoutUser();

        // Check if handleLogout function is called
        expect(Storage.clearUserData).toHaveBeenCalled();
        expect(authService.invalidateSession).toHaveBeenCalled();

        // Check if redirectUser function is called
        expect(LoginPage.displayLoginPage).toHaveBeenCalled();

        // Check if state is updated to trigger the display of LogoutMessage
        expect(setState).toHaveBeenCalledWith(true);
    });
});
