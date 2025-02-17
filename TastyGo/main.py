import user
import random
import delivery

def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    tel = input("Enter your phone number: ")
    adress = input("Enter your adress: ")
    code = random.randint(1000, 9999)
    
    total_price = 0
    products = []
    while True:
        product = input("აირჩიეთ პროდუქტი: 'სნიკერსი', 'ტვიქსი', 'მარსი' (ან '0' გასასვლელად): ")
        
        if product.lower() == "0":
            print(f"პროცესი დასრულდა. საერთო ფასი: {total_price} ლარი")
            break 

        price = 0
        
        match product:
            case 'სნიკერსი':
                # რაოდენობის დამატება
                # price უნდა იყოს ტოლი price გამრავლებული რაოდენობაზე
                price = 5 
            case 'ტვიქსი':
                # რაოდენობის დამატება
                # price უნდა იყოს ტოლი price გამრავლებული რაოდენობაზე
                price = 4
            case 'მარსი':
                # რაოდენობის დამატება
                # price უნდა იყოს ტოლი price გამრავლებული რაოდენობაზე
                price = 3
            case _:
                print("არასწორი პროდუქტი, გთხოვთ აირჩიოთ სწორად.")
                continue  

        total_price += price 
        products.append(product)
         
        print(f"თქვენ აირჩიეთ {product}, ფასი: {price} ლარი")
    
    print(products)
    
    user.user(name, surname, tel, adress, code)
    delivery.delivery("irakli", "gvari", name, surname, adress, code, products, total_price)
    
    
main()