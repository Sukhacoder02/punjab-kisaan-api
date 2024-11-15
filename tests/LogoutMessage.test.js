import React from 'react';
import { render, screen } from '@testing-library/react';
import LogoutMessage from '../components/LogoutMessage';

describe('LogoutMessage component', () => {
    test('testLogoutMessage', () => {
        // Arrange
        const successMessage = "You have successfully logged out.";

        // Act
        render(<LogoutMessage message={successMessage} />);

        // Assert
        expect(screen.getByText(successMessage)).toBeInTheDocument();
    });
});
