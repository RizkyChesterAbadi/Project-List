# Graded Chalenge 1
# Nama    : Rizky Chester Abadi
# Batch   : RMT-29

# Program ini dibuat untuk menguji program belanja RizkyChesterApp.py


# mengimport File yang akan diuji
# Package untuk unit testing
import unittest
from RizkyChester_App import ShoppingCart, CartItem #import macam-macam class yang akan diuji


class TestShoppingCart(unittest.TestCase):
    # skenario dari tiap function di class ShoppingCart yang dijalankan dalam Test yang dilakukan

    def setUp(self): #men setUP/mengatur kondisi dijalankannya fungsi dalam test 
        self.ShoppingCart = ShoppingCart() 
        
    def test_add_item(self): #mendefinisikan fungsi skenario user  menambahkan barang di program ke keranjang
        item = CartItem("Apel", 3400) #menjelaskan variable item sebagai CartItem
        item = CartItem("Jeruk", 2100)
        self.ShoppingCart.add_item(item) 

        self.assertEqual(len(self.ShoppingCart.item),1) #menjalankan tes dengan assertEqual menguji apakah hasilnya sama
 
   
    def test_remove_item(self): #mendefinisikan fungsi skenario user  mengurangi barang di program ke keranjang
        item = CartItem("Apel", 3400)
        self.ShoppingCart.add_item(item)
        self.ShoppingCart.remove_item("Apel")

        self.assertEqual(len(self.ShoppingCart.item),2)

    def test_view_ShoppingCart(self):
        self.ShoppingCart.view_ShoppingCart(ShoppingCart())


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2,exit=False)

        
