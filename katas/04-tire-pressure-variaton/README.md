# Tire Pressure Monitoring System Variation

## Goal
Be able to test `Alarm`'s `check` function without changing the method signature.

1. Test the code using test doubles created by you.

2. Test the code using test doubles created with a library.

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

## Learnings
How to build a Spy and a Stub manually.

How to use a library to generate the test doubles.

## References

Based on an exercise from [Luca Minudel](https://twitter.com/lukadotnet?lang=en) 's:
[TDD with Mock Objects And Design Principles exercises](https://github.com/lucaminudel/TDDwithMockObjectsAndDesignPrinciples)
