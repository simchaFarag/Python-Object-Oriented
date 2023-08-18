import unittest
from io import StringIO
import sys
from Dog import Dog
from Cat import Cat
from Frog import Frog


class BaseTest(unittest.TestCase):

    def assert_printed_output(self, expected_output, func_to_test, *args):
        # Replace the stdout
        held_output = StringIO()
        sys.stdout = held_output

        func_to_test(*args)
        held_output.seek(0)
        output = held_output.read().strip()

        # Return back the original stdout
        held_output.close()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)


class TestDog(BaseTest):
    def test_dog(self):
        dog = Dog()
        self.assert_printed_output("wagging their tails", lambda : dog.say_hello())
        self.assert_printed_output("The dog is wagging their tails in usual", lambda : dog.say_hello(1))
        self.assert_printed_output("The dog  they will bark loudly when  feel comfortable being touched", lambda : dog.say_hello(2))
        self.assert_printed_output("whooping when they frightened and upset", lambda : dog.say_hello(3))
        self.assertEqual(4, dog.get_number_of_legs())
        self.assertEqual(True, dog.is_mammals())
        self.assertEqual(True, dog.is_carnivorous())


class TestCat(BaseTest):
    def test_cat(self):
        cat=Cat()
        self.assert_printed_output("meow", lambda : cat.say_hello())
        self.assert_printed_output("The cat is meow in usual", lambda : cat.say_hello(1))
        self.assert_printed_output("when they are in a good mood, they make a purr, purr sound", lambda :cat.say_hello(2))
        self.assert_printed_output("and when they are frightened, they make a hiss sound", lambda : cat.say_hello(3))
        self.assertEqual(4, cat.get_number_of_legs())
        self.assertEqual(True, cat.is_mammals())
        self.assertEqual(True, cat.is_carnivorous())



class TestFrog(BaseTest):
    def test_frog(self):
        frog=Frog()
        self.assert_printed_output("kwa", lambda : frog.say_hello())
        self.assert_printed_output("good mood, it will sing quack quack quack on the shore",lambda :frog.say_hello(1))
        self.assert_printed_output("and when frightened, it will plop into the water",lambda : frog.say_hello(2))
        self.assertEqual(False, frog.has_gills())
        self.assertEqual(True, frog.has_lays_eggs())
        self.assertEqual(2, frog.get_number_of_legs())


if __name__ == '__main__':
    unittest.main()


