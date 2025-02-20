def delivery(name, surname, user_name, user_surname, user_address, user_code, products, total_price):  
    """  
    ფუნქცია უზრუნველყოფს შეკვეთის მიწოდების პროცესს მომხმარებლისთვის.  
    
    :param name: კურიერის სახელი  
    :param surname: კურიერის გვარი  
    :param user_name: მომხმარებლის სახელი  
    :param user_surname: მომხმარებლის გვარი  
    :param user_address: მომხმარებლის მიწოდების მისამართი  
    :param user_code: შეკვეთის სწორი კოდი  
    :param products: შეკვეთილი პროდუქტების სია  
    :param total_price: მიწოდებული პროდუქციის
    """  
    
    print(f"თქვენი შეკვეთა მზადაა და მოაქვს {name} {surname}-ს")  # მომხმარებელს აცნობებს, რომ შეკვეთა მზადაა  

    max_attempts = 3  # მაქსიმალური ცდების რაოდენობა  
    attempts = 0  # საწყისი ცდების რაოდენობა  

    while attempts < max_attempts:  # სანამ ცდების რაოდენობა ნაკლებია მაქსიმუმამდე  
        try:  
            delivery_code = int(input("გთხოვთ შეიყვანოთ შეკვეთის კოდი: "))  # მომხმარებლის მიერ კოდის შეყვანა  
        except ValueError:  # შესაბამისი ტიპის შეცდომა, თუ მომხმარებელი ვერ აკმაყოფილებს `int` ტიპს  
            print("არასწორი ფორმატი! გთხოვთ, შეიყვანოთ ციფრები.")  
            continue  # კიდევ ერთხელ სცადოს მომხმარებელი  

        if int(user_code) == delivery_code:  # თუ введенный კოდი შესაბამისობს  
            print(f"შეკვეთა მიწოდებულია {user_name} {user_surname}-ს\nმისამართზე: {user_address}")  # წარმატების შეტყობინება  
            print(f"თქვენი პროდუქცია: {', '.join(products)}\nგადახდილი თანხა: {total_price} ლარი")  # პროდუქციის და გადასახადის ინფორმაცია  
            break  # შეასრულებს ფუნქციას  

        else:  
            attempts += 1  # გაზრდის ცდების რაოდენობას  
            remaining_attempts = max_attempts - attempts  # დარჩენილი ცდების რაოდენობა  
            print(f"შეკვეთის კოდი არასწორია! სცადეთ ხელახლა. {remaining_attempts} დარჩენილი ცდა")  # შეტყობინება  

            if attempts == max_attempts:  # როცა ცდები ამოიწურება  
                print("თქვენი სამი ცდა ამოიწურა! შეკვეთის მიწოდება გაუქმდა!")  # შეტყობინება შეკვეთის გაუქმებაზე