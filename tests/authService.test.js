import { invalidateSession } from '../services/authService';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';

// Set up mock adapter for axios
const mock = new MockAdapter(axios);

describe('AuthService', () => {
  describe('invalidateSession', () => {
    it("should make a successful API call to invalidate the user's session", async () => {
      // Arrange
      const expectedResponse = { success: true };
      mock.onPost('/api/logout').reply(200, expectedResponse);
      
      // Act
      const response = await invalidateSession();
      
      // Assert
      expect(response.data).toEqual(expectedResponse);
    });

    it('should throw an error if the API call fails', async () => {
      // Arrange
      mock.onPost('/api/logout').reply(500);
      
      // Act & Assert
      await expect(invalidateSession()).rejects.toThrow('Request failed with status code 500');
    });
  });
});
