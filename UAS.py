class Data:
    def __init__(self):
        self.records = []

    def add_record(self, name, age, email, favorite_food, favorite_drink, hobby):
        self.records.append({
            "Name": name, 
            "Age": age, 
            "Email": email, 
            "Favorite Food": favorite_food, 
            "Favorite Drink": favorite_drink, 
            "Hobby": hobby
        })

    def get_records(self):
        return self.records


class View:
    @staticmethod
    def display_menu():
        print("\n=== Menu ===")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Keluar")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_table(data):
        if not data:
            print("\nTidak ada data yang tersedia.")
            return

        print("\n=== Data ===")
        print(f"{'No.':<5}{'Name':<20}{'Age':<5}{'Email':<30}{'Favorite Food':<20}{'Favorite Drink':<20}{'Hobby':<20}")
        print("-" * 120)
        for idx, record in enumerate(data, start=1):
            print(f"{idx:<5}{record['Name']:<20}{record['Age']:<5}{record['Email']:<30}{record['Favorite Food']:<20}{record['Favorite Drink']:<20}{record['Hobby']:<20}")


class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def add_data(self):
        try:
            name = self.view.get_input("Masukkan nama: ").strip()
            if not name:
                raise ValueError("Nama tidak boleh kosong.")

            age = self.view.get_input("Masukkan usia: ").strip()
            if not age.isdigit():
                raise ValueError("Usia harus berupa angka.")

            email = self.view.get_input("Masukkan email: ").strip()
            if "@" not in email or "." not in email:
                raise ValueError("Email tidak valid.")

            favorite_food = self.view.get_input("Masukkan makanan kesukaan: ").strip()
            if not favorite_food:
                raise ValueError("Makanan kesukaan tidak boleh kosong.")

            favorite_drink = self.view.get_input("Masukkan minuman kesukaan: ").strip()
            if not favorite_drink:
                raise ValueError("Minuman kesukaan tidak boleh kosong.")

            hobby = self.view.get_input("Masukkan hobi: ").strip()
            if not hobby:
                raise ValueError("Hobi tidak boleh kosong.")

            self.data.add_record(name, int(age), email, favorite_food, favorite_drink, hobby)
            print("\nData berhasil ditambahkan!")

        except ValueError as e:
            print(f"\nError: {e}")

    def view_data(self):
        records = self.data.get_records()
        self.view.display_table(records)

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Pilih menu: ").strip()

            if choice == "1":
                self.add_data()
            elif choice == "2":
                self.view_data()
            elif choice == "3":
                print("\nProgram selesai. Terima kasih!")
                break
            else:
                print("\nPilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    app = Process()
    app.run()
   