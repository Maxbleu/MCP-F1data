import unittest
from unittest.mock import MagicMock
import sys
import os

# Mock dependencies
mock_fastmcp = MagicMock()
sys.modules['fastmcp'] = mock_fastmcp
sys.modules['fastmcp.server'] = MagicMock()
sys.modules['fastmcp.server.auth'] = MagicMock()
sys.modules['pydantic'] = MagicMock()
sys.modules['fastapi'] = MagicMock()
sys.modules['requests'] = MagicMock()
sys.modules['fastf1'] = MagicMock()
sys.modules['pandas'] = MagicMock()
sys.modules['numpy'] = MagicMock()

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_f1data.tools.race_tools import RaceTools

class TestRaceTools(unittest.TestCase):
    def test_class_exists(self):
        self.assertTrue(hasattr(RaceTools, 'get_free_practice_1_by_id'))
        self.assertTrue(hasattr(RaceTools, 'get_warming_up_by_id')) # One of the missing ones
        self.assertTrue(hasattr(RaceTools, '__register_mcp_tools__'))

    def test_register_tools(self):
        mcp_mock = MagicMock()
        RaceTools.__register_mcp_tools__(mcp_mock)
        # Check if tools were registered. 
        # The number of calls to mcp_mock.tool should match the number of decorated functions.
        # We have many tools, let's just check it was called.
        self.assertTrue(mcp_mock.tool.called)
        
        # Verify specific missing tools were registered
        # This is a bit tricky with mocks, but we can check if the tool names are in the calls
        tool_names = [call.kwargs['name'] for call in mcp_mock.tool.call_args_list]
        self.assertIn('get_warming_up_by_id', tool_names)
        self.assertIn('get_pit_stop_by_id', tool_names)
        self.assertIn('get_driver_standing_by_id', tool_names)

if __name__ == '__main__':
    unittest.main()
