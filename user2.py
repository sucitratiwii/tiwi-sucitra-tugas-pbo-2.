# ============================================================
# SOAL
# 2. Berdasarkan program dari Latihan/Tugas sebelumnya (class User),
# lanjutkan dengan menambahkan atribut bernama login_attempts ke
# kelas User.
#
# Tulis metode bernama increment_login_attempts() yang menambah
# nilai login_attempts sebesar 1.
#
# Tulis metode lain bernama reset_login_attempts() yang mengatur
# ulang nilai login_attempts menjadi 0.
#
# Buat instance dari kelas User dan panggil
# increment_login_attempts() beberapa kali.
#
# Cetak nilai login_attempts untuk memastikan nilainya telah
# ditambah dengan benar, lalu panggil reset_login_attempts().
#
# Cetak login_attempts lagi untuk memastikan nilainya telah
# diatur ulang menjadi 0.
# ============================================================


class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts = 0  # atribut jumlah percobaan login

    def describe_user(self):
        print(f"Full name : {self.first_name} {self.last_name}")
        print(f"Age       : {self.age}")
        print(f"Gender    : {self.gender}")
        print(f"Email     : {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

    # metode untuk menambah jumlah percobaan login
    def increment_login_attempts(self):
        self.login_attempts += 1

    # metode untuk mereset jumlah percobaan login
    def reset_login_attempts(self):
        self.login_attempts = 0


# User 1
user1 = User('Rina', 'Putri', 21, 'Female', 'rina@email.com')

print(f"First name is {user1.first_name}.")
print(f"Last name is {user1.last_name}.")
user1.describe_user()
user1.greet_user()
print()

# Menambah percobaan login beberapa kali
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Menampilkan jumlah percobaan login
print("Login attempts:", user1.login_attempts)

# Mengatur ulang percobaan login
user1.reset_login_attempts()

# Menampilkan kembali setelah direset
print("Login attempts after reset:", user1.login_attempts)