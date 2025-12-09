import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

# Mock fastmcp before importing modules that depend on it
mock_fastmcp = MagicMock()
sys.modules['fastmcp'] = mock_fastmcp
sys.modules['fastmcp.server'] = MagicMock()
sys.modules['fastmcp.server.auth'] = MagicMock()

# Mock pydantic
mock_pydantic = MagicMock()
# Mock Field to return the default value or just a mock
mock_pydantic.Field = MagicMock(return_value=None)
sys.modules['pydantic'] = mock_pydantic

# Mock fastf1
sys.modules['fastf1'] = MagicMock()
sys.modules['pandas'] = MagicMock()
sys.modules['numpy'] = MagicMock()
sys.modules['fastapi'] = MagicMock()
sys.modules['requests'] = MagicMock()

# Add the project root to the path so we can import mcp_f1data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_f1data.tools.execution_tools import ExecutionTools

class TestExecutionTools(unittest.TestCase):
    
    @patch('mcp_f1data.utils.request_utils.requests')
    def test_execute_code_simple_math(self, mock_requests):
        # Test simple python code execution
        code = "result = 1 + 1"
        result = ExecutionTools.execute_code(code)
        self.assertEqual(result, "2")

    @patch('mcp_f1data.utils.request_utils.requests')
    def test_execute_code_driver_search(self, mock_requests):
        # Mock the API response for post
        mock_response = MagicMock()
        mock_response.json.return_value = [{"driverId": "hamilton", "givenName": "Lewis", "familyName": "Hamilton"}]
        mock_response.raise_for_status.return_value = None
        mock_requests.post.return_value = mock_response

        # Test calling a tool function
        code = """
result = DriverTools.search_driver("Hamilton")
"""
        result = ExecutionTools.execute_code(code)
        
        # Verify the result is what we expect (string representation of the list)
        expected_result = str([{"driverId": "hamilton", "givenName": "Lewis", "familyName": "Hamilton"}])
        self.assertEqual(result, expected_result)

    @patch('mcp_f1data.utils.request_utils.requests')
    def test_execute_code_direct_function_call(self, mock_requests):
        # Mock the API response for post (search_driver uses post)
        mock_response = MagicMock()
        mock_response.json.return_value = {"season": "2023"}
        mock_requests.post.return_value = mock_response
        
        # Also mock get just in case
        mock_requests.get.return_value = mock_response

        # Test calling a function directly (exposed in env)
        # Note: search_driver uses POST.
        code = """
result = search_driver("Verstappen")
"""
        result = ExecutionTools.execute_code(code)
        self.assertEqual(result, str({"season": "2023"}))

if __name__ == '__main__':
    unittest.main()
