import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import LogoutButton from '../components/LogoutButton';

// Mock the handleLogout function
const mockHandleLogout = jest.fn();

describe('LogoutButton', () => {

  test('renders the LogoutButton component correctly', () => {
    const { getByRole } = render(<LogoutButton handleLogout={mockHandleLogout} />);
    const button = getByRole('button', { name: /logout/i });
    
    expect(button).toBeInTheDocument();
  });

  test('calls handleLogout function when clicked', () => {
    const { getByRole } = render(<LogoutButton handleLogout={mockHandleLogout} />);
    const button = getByRole('button', { name: /logout/i });
    
    fireEvent.click(button);

    expect(mockHandleLogout).toHaveBeenCalledTimes(1);
  });
});
