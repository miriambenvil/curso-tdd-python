import unittest


def list_to_100():
    list_100 = []
    for i in range(1, 101):
        list_100.append(fizzbuzz(i))
    return list_100


def fizzbuzz(number):
    number_str = str(number)
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif "3" in number_str and "5" in number_str:
        return "FizzBuzz"
    elif "3" in number_str:
        return "Fizz"
    elif "5" in number_str:
        return "Buzz"
    else:
        return number


def get_list_position(my_list, position):
    return my_list[position-1]


class FizzBuzzTest(unittest.TestCase):
    def test_length_list(self):
        result = list_to_100()
        self.assertEqual(len(result), 100)

    def test_multiple_of_3(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 3), "Fizz")
        self.assertEqual(get_list_position(result, 96), "Fizz")

    def test_multiple_of_5(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 5), "Buzz")
        self.assertEqual(get_list_position(result, 100), "Buzz")

    def test_multiple_of_3_and_5(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 15), "FizzBuzz")
        self.assertEqual(get_list_position(result, 60), "FizzBuzz")

    def test_has_3(self):
        result = list_to_100()
        # self.assertNotEqual(get_list_position(result, 30), "Fizz")
        self.assertEqual(get_list_position(result, 13), "Fizz")
        self.assertEqual(get_list_position(result, 31), "Fizz")

    def test_has_5(self):
        result = list_to_100()
        # self.assertNotEqual(get_list_position(result, 15), "Buzz")
        self.assertEqual(get_list_position(result, 52), "Buzz")
        self.assertEqual(get_list_position(result, 58), "Buzz")

    def test_has_3_and_5(self):
        result = list_to_100()
        # self.assertNotEqual(get_list_position(result, 35), "FizzBuzz")
        self.assertEqual(get_list_position(result, 53), "FizzBuzz")

    def test_priority_requirements(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 35), "Buzz")
        self.assertEqual(get_list_position(result, 30), "FizzBuzz")

    def test_first_element(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 1), 1)

    def test_last_element(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 100), "Buzz")

    def test_random_number_elements(self):
        result = list_to_100()
        self.assertEqual(get_list_position(result, 71), 71)
        self.assertEqual(get_list_position(result, 92), 92)
