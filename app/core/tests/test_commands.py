"""
Test custom Django management command.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test command"""

    def test_wait_for_db_ready(self, patched_check):
        """Tests waiting for database if database ready"""

        patched_check.return_value = True 

        call_command('wait_dor_db')

        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting Operational error"""

        patched_check.side_effect = [Psycopg2OpError] * 2 + [OperationalError] * 3 + [True] 
        # The first two times we call the mocked method. We want it to raise the pcycopg2 error, so it raises the error.
        # The next three times we raise operational eroor.
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(database=['default'])
        