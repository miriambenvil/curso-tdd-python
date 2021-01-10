import unittest
from mycalendar import Calendar
from unittest.mock import Mock

from account_service import AccountService
from console import Console


class AcceptanceTest(unittest.TestCase):

    def test_print_statement_containing_all_transactions(self):
        console = Mock(spec=Console)

        attrs = {'current_date.return_value': ["01/04/2014",
                                               "02/04/2014",
                                               "10/04/2014"]}
        calendar = Mock(spec=Calendar, **attrs)
        account = AccountService(console, calendar)

        account.deposit(1000)
        account.withdraw(100)
        account.deposit(500)
        account.print_statement()

        console.print_line.assert_called_with("DATE | AMOUNT | BALANCE")
        console.print_line.assert_called_with("10/04/2014 | 500 | 1400")
        console.print_line.assert_called_with("02/04/2014 | -100 | 900")
        console.print_line.assert_called_with("01/04/2014 | 1000 | 1000")
