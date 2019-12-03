from django.test import TestCase
from catalog.models import BoardGame, VideoGame

# Create your tests here.
#Board Game
class BoardGameTest(TestCase):
    @classmethod    
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        BoardGame.objects.create(name='Monopoly', summary='Make dat cash', price='30.00', players='2-5')
        pass
    
    def test_name_label(self):
        boardGame = BoardGame.objects.get(id=1)
        field_label = boardGame._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
    
    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)
    
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)


"""class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
    
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
    
    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)
    
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""
