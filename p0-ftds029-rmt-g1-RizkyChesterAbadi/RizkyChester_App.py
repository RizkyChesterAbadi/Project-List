# Graded Chalenge 1
# Nama    : Rizky Chester Abadi
# Batch   : RMT-29

# Program ini dibuat untuk memungkinkan user/penggunanya untuk menambah, menghapus, dan melihat barang di keranjang belanja mereka.
# Tiap barang memiliki informasi nama barang dan harganya. 
# User juga bisa melihat total harga belanjanya


#class Barang/Item yang akan ditambahkan ke keranjang/Cart, memiliki parameter name dan price
class CartItem:         
    def __init__(self,name,price):
        self.name = name
        self.price = price

#Class keranjang
class ShoppingCart:    
    def __init__(self):
        # attribute untuk menyimpan item didalamnya berupa List
        self.CartItems = []
    
    # define method(s)/menjabarkan cara menambahkan barang ke ShoppingCart/keranjang
    def add_item(self,CartItem):
    # cara untuk menambah barang/item yang akan ditambahkan
        self.CartItems.append(CartItem)
    
    def remove_item(self, CartItem_name):
    # cara untuk menghapus/meremove barang/ItemCart dari ShoppingCart
        self.CartItems = [CartItem for CartItem in self.CartItems if CartItem.name != CartItem_name]

    def total_price(self):
    # Cara menghitum total harga barang yang dimasukkan kedalam Shoppingcart
        return sum(CartItem.price for CartItem in self.CartItems)
    
    def view_ShoppingCart(self):
    # cara untuk menampilkan barang/CartItem yang telah ditambahkan ke ShoppingCart
        if not self.CartItems:
            print("Shoping Cart Kosong melompong")
        else:
            print ("Keranjang belanjaan berisi: ")
            for CartItem in self.CartItems:
                print (f"{CartItem.name}: Rp{CartItem.price}")

    # Membuat object untuk memanggil class ShoppingCart
ShoppingCart = ShoppingCart()

# While loop untuk interaksi dengan user dengan membuat 5 pilihan 
while True:
        print("\nPilih Menu:")
        print("1. Menambah barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang di Keranjang")
        print("4. Lihat Total Belanja")
        print("5. exit")

        choice = input ("Masukkan pilihan (1/2/3/4/5): ")
        # Jika User memilih pilihan 1 yakni menambah barang ke ShoppingCart dan harga barang
        if choice == "1":
            name = input("Masukkan Nama Barang: ")
            price = float(input("Masukkan Harga barang: "))
            ShoppingCart.add_item(CartItem(name,price))
            print("Barang telah ditambahkan dalam Keranjang")

        # Jika User memilih pilihan 2 yakni menghapus barang ke ShoppingCart
        elif choice == "2":
            name = input("Masukkan nama Barang yang ingin dihapus: ")
            ShoppingCart.remove_item(name)
            print("Barang telah dihapus dari keranjang belanja")
        # Jika user memilih pilihan 3 untuk menampilkan barang/CartItem apa saja yang telah ditambahkan ke ShoppingCart
        elif choice == "3":
            ShoppingCart.view_ShoppingCart()
        # Jika user memilih pilihan 4 untuk melihat total belanjaan
        elif choice == "4":
            print(f"Total harga Belanjaan: Rp{ShoppingCart.total_price()}")
        # Jika user memilih pilihan 5
        elif choice == "5":
            print("Terima Kasih, Semoga datang kembali")
            # Break untuk looping 
            break
        
        # selain itu
        else:
            print("Pilihan tidak ada dalam daftar, Silahkan memilih kembali")



        
    
    




