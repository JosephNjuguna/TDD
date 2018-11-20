import unittest
from shopping_cart import ShoppingCart,Shop


class TestClass(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.shop = Shop()

    def test_add_items(self):
        add_item = self.cart.add_item('lambo',3, 10)
        itemstotal = self.cart.total
        self.assertEqual(30, itemstotal, msg="the total is not correct")
        self.assertEqual(self.cart.items['lambo'], 3, msg = 'quantity of items not correct')

    def test_cart_property_initialization(self):
        accesing_cart_attributes = self.cart.total
        accesing_item_attributes = self.cart.items
        self.assertEqual(0, accesing_cart_attributes, msg = 'the total is not 0 zero')
        self.assertIsInstance(accesing_item_attributes,dict, msg = 'items is not a dictionary')

if __name__ == '__main__':
    unittest.main()
