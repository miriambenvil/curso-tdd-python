## Goal
Develop a program to manage the transactions of a bank account.

The transactions are: deposit money into the account, and withdraw from the account. 

We need to be able to print into the console the result.

## Requirement
You cannot change the signature of the public interface (the class AccountService).

## Code

```python
class AccountService:
  def deposit(self, amount):

  def withdraw(self, amount):
    pass

  def print_statement(self):
    pass

```

##Acceptance test

```python
@Test
public void should_print_statement_containing_all_transactions() {
  account.deposit(1000);
  account.withdraw(100);
  account.deposit(500);

  account.printStatement();

  verify(console).printLine("DATE | AMOUNT | BALANCE");
  verify(console).printLine("10/04/2014 | 500 | 1400");
  verify(console).printLine("02/04/2014 | -100 | 900");
  verify(console).printLine("01/04/2014 | 1000 | 1000");
}
```

## Tip
Start writing the acceptance test but then move to unit tests, and at the end focus again on the acceptance test.


## Tools

[unittest.mock](https://docs.python.org/3.8/library/unittest.mock.html)

### Example of spying an interaction

```python
from unittest.mock import Mock

collaborator = Mock()
collaborator.command()
collaborator.command.assert_called()
collaborator.command(5)
collaborator.command.assert_called_with(5)
```

### Example of stubbing an interaction

```python
import unittest
from unittest.mock import Mock

attrs = {'command.return_value': 'ok'}
collaborator = Mock(**attrs)
actual = collaborator.command()
self.assertEqual('ok', actual)
```
