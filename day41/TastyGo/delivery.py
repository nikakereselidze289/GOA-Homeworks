def delivery(name, surname, user_name, user_surname, user_adress, user_code, products, total_price):
    print(f"თქვენი შეკვეთა მზადაა და მოაქვს {name} {surname}-ს")
    
    
    # კურიერის მიტანის დრო
    
    
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        delivery_code = int(input("გთხოვთ შეიყვანოთ შეკვეთის კოდი: "))
        
        if int(user_code) == delivery_code:
            print(f"შეკვეთა მიწოდებულია {user_name} {user_surname}-ს\nმისამართზე: {user_adress}")
            print(f"თქვენი პროდუქცია {products}\nგადახდილი თანხა: {total_price}ლარი")
            break 
        
        else:
            attempts += 1
            print(f"შეკვეთის კოდი არასწორია! სცადეთ ხელახლა. {max_attempts - attempts} დარჩენილი ცდა")
            
            if attempts == max_attempts:
                print("თქვენი სამი ცდა ამოიწურა! შეკვეთის მიწოდება გაუქმდა!")
                break  