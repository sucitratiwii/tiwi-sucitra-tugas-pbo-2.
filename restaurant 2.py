# ============================================================
# SOAL
# Berdasarkan program dari Latihan/Tugas sebelumnya (class Restaurant),
# lanjutkan dengan menambahkan jumlah pelanggan yang dilayani.
#
# 1. Tambahkan atribut bernama number_served dengan nilai default 0.
# 2. Buat instance bernama restaurant dari kelas ini.
# 3. Cetak jumlah pelanggan yang telah dilayani oleh restoran.
# 4. Ubah nilai number_served lalu cetak kembali.
# 5. Tambahkan metode set_number_served() untuk mengatur jumlah pelanggan.
# 6. Panggil metode tersebut dengan nilai baru lalu tampilkan hasilnya.
# 7. Tambahkan metode increment_number_served() untuk menambah jumlah pelanggan.
# 8. Panggil metode tersebut dengan angka yang mewakili jumlah pelanggan
#    yang dilayani dalam satu hari.
# ============================================================


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # atribut jumlah pelanggan yang dilayani

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

    # metode untuk mengatur jumlah pelanggan
    def set_number_served(self, number):
        self.number_served = number

    # metode untuk menambah jumlah pelanggan
    def increment_number_served(self, additional):
        self.number_served += additional


# Restaurant 1
restaurant = Restaurant('Sugiharti', 'Indonesia')

print(f"The restaurant name is {restaurant.restaurant_name}.")
print(f"This restaurant provides {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()

# Menampilkan jumlah pelanggan yang telah dilayani
print("Number of customers served:", restaurant.number_served)

# Mengubah nilai number_served
restaurant.number_served = 20
print("Updated number of customers served:", restaurant.number_served)

# Menggunakan metode set_number_served()
restaurant.set_number_served(50)
print("Customers served after set_number_served():", restaurant.number_served)

# Menambah jumlah pelanggan yang dilayani
restaurant.increment_number_served(30)
print("Customers served after increment:", restaurant.number_served)