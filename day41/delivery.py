import time
import tkinter as tk
from threading import Lock
def delivery(name, surname, user_name, user_surname, user_address, user_code, products, total_price):  
    """  
    Handles the delivery process and verifies the order code.  
    """  
    print(f"\n🚚 შეკვეთა მზადაა! კურიერი {name} {surname} გზაშია და 40 წუთში მოგიტანთ! 🛵\n")  
    max_attempts = 3  # Maximum attempts for entering the correct code  
    attempts = 0  
    user_code = int(user_code)  # Ensure user_code is an integer before loop  

    while attempts < max_attempts:  
        try:  
            delivery_code = int(input("📦 გთხოვთ, შეიყვანოთ შეკვეთის კოდი: "))  
        except ValueError:  
            print("❌ არასწორი ფორმატი! გთხოვთ, შეიყვანოთ მხოლოდ ციფრები.")  
            continue  

        if delivery_code == user_code:  # Correct comparison  
            print("\n✅ შეკვეთა წარმატებით მიეწოდათ!\n")
            print("=" * 40)
            print(f"👤 მომხმარებელი: {user_name} {user_surname}")
            print(f"📍 მიწოდების მისამართი: {user_address}")
            print("=" * 40)

            print("\n📦 თქვენმა შეკვეთამ მოიცვა:\n")
            for index, item in enumerate(products, start=1):
                print(f"🔹 {index}. {item['quantity']} x {item['product']} - {item['product_type']} ({item['price']} ლარი)")

            print(f"\n💰 საერთო თანხა: {total_price} ლარი")
            print("=" * 40)
            return  # **Stops execution immediately after successful verification**

        else:  
            attempts += 1  
            remaining_attempts = max_attempts - attempts  
            print(f"❌ არასწორი კოდი! გთხოვთ სცადოთ კვლავ. (დარჩა {remaining_attempts} ცდა)")  

    print("\n🚫 სამწუხაროდ, თქვენ ამოწურეთ ცდების რაოდენობა! შეკვეთის მიწოდება გაუქმდა.\n")  