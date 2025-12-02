
class InvalidTelevisionData(Exception):
    pass

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0
 
    def get_data(self):
        try:
            self.model_number = int(input("Enter Model Number (up to 4 digits): "))
            self.screen_size = float(input("Enter Screen Size (in inches): "))
            self.price = float(input("Enter Price (in Rs): "))

            if self.model_number > 9999:
                raise InvalidTelevisionData("Model number must not exceed 4 digits.")
            if self.screen_size < 12 or self.screen_size > 70:
                raise InvalidTelevisionData("Screen size must be between 12 and 70 inches.")
            if self.price < 0 or self.price > 5000:
                raise InvalidTelevisionData("Price must be between 0 and 5000 Rs.")

        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.")
            self.reset_data()
        except InvalidTelevisionData as e:
            print(f"Error: {e}")
            self.reset_data()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.reset_data()
  
    def reset_data(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0
 
    def display(self):
        print("\n--- Television Details ---")
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Price: Rs. {self.price}")

tv = Television()
tv.get_data()
tv.display()


