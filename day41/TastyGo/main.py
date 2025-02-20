import user
import random
import delivery
import time
import tkinter as tk
import random
from threading import Lock
import tkinter as tk
import random
from threading import Lock


def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    tel = input("Enter your phone number: ")
    adress = input("Enter your adress: ")
    code = random.randint(1000, 9999)
    
    total_price = 0  # დასაწყისი საერთო ფასი
    products = []    # პროდუქტის ჩაწერის სია

    while True:
        product = input("აირჩიეთ პროდუქტი: 'Pizza', 'Burger', 'Pasta', 'Sushi', 'Salad', 'Cutlet' (ან '0' გასასვლელად): ").lower()
        
        if product == "0":
            print(f"პროცესი დასრულდა. საერთო ფასი: {total_price} ლარი")
            break 

        price = 0
        quantity = 0
        match product:
            case 'pizza':
                pizza_type = input("აირჩიეთ პიცის სახეობა: 'Margarita', 'Peperoni', 'Veggie': ").lower()
                match pizza_type:
                    case 'margarita':
                        price = 15
                    case 'peperoni':
                        price = 18
                    case 'veggie':
                        price = 17
                    case _:
                        print("არასწორი პიცის სახეობა.")
                        continue
            case 'burger':
                burger_type = input("აირჩიეთ ბურგერის სახეობა: 'Classic', 'Cheese', 'Chicken': ").lower()
                match burger_type:
                    case 'classic':
                        price = 12
                    case 'cheese':
                        price = 14
                    case 'chicken':
                        price = 15
                    case _:
                        print("არასწორი ბურგერის სახეობა.")
                        continue
            case 'pasta':
                pasta_type = input("აირჩიეთ პასტა: 'Spaghetti', 'Carbonara', 'Penne': ").lower()
                match pasta_type:
                    case 'spaghetti':
                        price = 18
                    case 'carbonara':
                        price = 20
                    case 'penne':
                        price = 17
                    case _:
                        print("არასწორი პასტა.")
                        continue
            case 'sushi':
                sushi_type = input("აირჩიეთ სუში: 'Set', 'Nigiri', 'Maki': ").lower()
                match sushi_type:
                    case 'set':
                        price = 25
                    case 'nigiri':
                        price = 12
                    case 'maki':
                        price = 15
                    case _:
                        print("არასწორი სუში.")
                        continue
            case 'salad':
                salad_type = input("აირჩიეთ სალათი: 'Chicken', 'Caesar', 'Vegetable': ").lower()
                match salad_type:
                    case 'chicken':
                        price = 12
                    case 'caesar':
                        price = 14
                    case 'vegetable':
                        price = 10
                    case _:
                        print("არასწორი სალათი.")
                        continue
            case 'cutlet':
                cutlet_type = input("აირჩიეთ კოტლეტის სახეობა: 'Chicken', 'Beef', 'Pork': ").lower()
                match cutlet_type:
                    case 'chicken':
                        price = 18
                    case 'beef':
                        price = 20
                    case 'pork':
                        price = 22
                    case _:
                        print("არასწორი კოტლეტი.")
                        continue
            case _:
                print("არასწორი პროდუქტი, გთხოვთ აირჩიოთ სწორად.")
                continue

        if price > 0:
            # რაოდენობის გამორჩევა
            try:
                quantity = int(input(f"მოდი, შეიყვანეთ რაოდენობა პროდუქტის '{product.capitalize()}'-ის: "))
                if quantity <= 0:
                    print("რაოდენობა უნდა იყოს დადებითი ციფრი.")
                    continue
            except ValueError:
                print("გთხოვთ, შეიყვანოთ სწორი რიცხვი.")
                continue

            total_price += price * quantity  # ფასის დამატება საერთო ფასში
            products.append(f"{quantity} {product.capitalize()} - {price * quantity} ლარი")
            print(f"თქვენ აირჩიეთ {quantity} {product.capitalize()} - {price * quantity} ლარი")

    # გამოტანა იმ პროდუქტების შესახებ, რომლებიც აირჩიეს
    print("\nთქვენ აირჩიეთ შემდეგი პროდუქტები:")
    for item in products:
        print(item)

    print(f"\nჯამური ფასი: {total_price} ლარი")

    user.user(name, surname, tel, adress, code)
    delivery.delivery("Irakli", "Gelashvili", name, surname, adress, code, products, total_price)
    
    
main()


print("="*40)
print("        შეკვეთა მზადაა, კურიერი მას მალე მოგიტანთ, არაუგვიანეს 40 წუთში. მანამდე შეგიძლიათ ტეტრისის თამაშით გაერთოთ:")

time.sleep(5)

print("ok")


# ვქმნით სიას რომელიც შეიცავს ყველა შესაძლო ტეტრონიმოს ფერს
COLORS = ['grey', 'green', 'yellow', 'cyan', 'blue', 'red', 'purple', 'white']

# ვიწყებთ მთავარ კოდს
class Tetris():
    # განვსაზღვრავთ სათამაშო მოედნის ადგილს
    FIELD_HEIGHT = 20  # სიმაღლე
    FIELD_WIDTH = 10    # სიგანე
    # განვსაზღვრავთ ქულებს
    SCORE_PER_ELIMINATED_LINES = (0, 40, 100, 300, 1200)

    # განვსასზვრავთ თავად ტეტრონიმოს ტიპებს(ტეტრისში ბლოკები რომლებიც ჩამოდიან არსებობს სულ 7 ვარიაცია:O,L,J,Z,S,I)
    TETROMINOS = [
        [(0, 0), (0, 1), (1, 0), (1,1)], # O
        [(0, 0), (0, 1), (1, 1), (2,1)], # L
        [(0, 1), (1, 1), (2, 1), (2,0)], # J 
        [(0, 1), (1, 0), (1, 1), (2,0)], # Z
        [(0, 1), (1, 0), (1, 1), (2,1)], # T
        [(0, 0), (1, 0), (1, 1), (2,1)], # S
        [(0, 1), (1, 1), (2, 1), (3,1)], # I
    ]
    
    def __init__(self):
        # სათამაშო მოედნის დაფა ინიციალიზაცია
        self.field = [[0 for c in range(Tetris.FIELD_WIDTH)] for r in range(Tetris.FIELD_HEIGHT)]
        self.score = 0
        self.level = 0
        self.total_lines_eliminated = 0
        self.game_over = False
        self.move_lock = Lock()  # ლოკი, რომ მოძრაობა იყოს სინგლური
        self.reset_tetromino()  # ახალი ტეტრონიმოს გენერაცია

    def reset_tetromino(self):
        # ახალი ტეტრონიმოს გენერაცია
        self.tetromino = random.choice(Tetris.TETROMINOS)[:]  # ახალი ტეტრონიმოს შერჩევა
        self.tetromino_color = random.randint(1, len(COLORS)-1)  # ფერის შერჩევა
        self.tetromino_offset = [-2, Tetris.FIELD_WIDTH//2]  # პოზიციის დაწყება
        # თუ ახალი ტეტრონიმო შეჯახდება მინდორში არსებული ბლოკებს, თამაში იწყება
        self.game_over = any(not self.is_cell_free(r, c) for (r, c) in self.get_tetromino_coords())
    
    def get_tetromino_coords(self):
        # დააბრუნებს კოორდინატებს ტეტრონიმოსთვის, გათვალისწინებულია საწყისი_offset
        return [(r+self.tetromino_offset[0], c + self.tetromino_offset[1]) for (r, c) in self.tetromino]

    def apply_tetromino(self):
        # ტეტრონიმოს გამოტანა და მოედნზე მისი განთავსება
        for (r, c) in self.get_tetromino_coords():
            self.field[r][c] = self.tetromino_color  # ფერის განახლება

        # მინდორში ცარიელი ხაზების მოცილება
        new_field = [row for row in self.field if any(tile == 0 for tile in row)]
        lines_eliminated = len(self.field)-len(new_field)  # თუ ხაზები ამოიწურა, მათი რაოდენობა
        self.total_lines_eliminated += lines_eliminated  # ნამდვილი ხაზების ამოცნობა
        self.field = [[0]*Tetris.FIELD_WIDTH for x in range(lines_eliminated)] + new_field  # ახალი მინდორი
        # ქულების განახლება
        self.score += Tetris.SCORE_PER_ELIMINATED_LINES[lines_eliminated] * (self.level + 1)
        self.level = self.total_lines_eliminated // 10  # დონე განახლდება
        self.reset_tetromino()  # ახალი ტეტრონიმოს გენერაცია

    def get_color(self, r, c):
        # დააბრუნებს ფერს თუ ცარიელია მინდორში ბლოკი
        return self.tetromino_color if (r, c) in self.get_tetromino_coords() else self.field[r][c]
    
    def is_cell_free(self, r, c):
        # შემოწმება არის თუ არა მინდორში შესაბამისი ღრუ ბლოკი
        return r < Tetris.FIELD_HEIGHT and 0 <= c < Tetris.FIELD_WIDTH and (r < 0 or self.field[r][c] == 0)
    
    def move(self, dr, dc):
        # მოძრაობა (dr - სიმაღლე, dc - სიგანე)
        with self.move_lock:
            if self.game_over:
                return

            if all(self.is_cell_free(r + dr, c + dc) for (r, c) in self.get_tetromino_coords()):
                # თუ ბლოკები არ იკვეთება, მაშინ გადავა ახალი პოზიციაზე
                self.tetromino_offset = [self.tetromino_offset[0] + dr, self.tetromino_offset[1] + dc]
            elif dr == 1 and dc == 0:
                # თუ ბლოკი ჩადის ქვემოთ, გამოვიყენებთ მეთოდს `apply_tetromino`
                self.game_over = any(r < 0 for (r, c) in self.get_tetromino_coords())
                if not self.game_over:
                    self.apply_tetromino()

    def rotate(self):
        # ტეტრონიმოს როტაცია
        with self.move_lock:
            if self.game_over:
                self.__init__()  # თუ თამაში დასრულდა, თამაშის დაწყება თავიდან
                return

            ys = [r for (r, c) in self.tetromino]
            xs = [c for (r, c) in self.tetromino]
            size = max(max(ys) - min(ys), max(xs)-min(xs))
            # როტირებული ტეტრონიმოს კოორდინატები
            rotated_tetromino = [(c, size-r) for (r, c) in self.tetromino]
            wallkick_offset = self.tetromino_offset[:]
            tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
            min_x = min(c for r, c in tetromino_coord)
            max_x = max(c for r, c in tetromino_coord)
            max_y = max(r for r, c in tetromino_coord)
            wallkick_offset[1] -= min(0, min_x)  # საზღვარი
            wallkick_offset[1] += min(0, Tetris.FIELD_WIDTH - (1 + max_x))  # საზღვარი
            wallkick_offset[0] += min(0, Tetris.FIELD_HEIGHT - (1 + max_y))  # საზღვარი

            tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
            if all(self.is_cell_free(r, c) for (r, c) in tetromino_coord):
                self.tetromino, self.tetromino_offset = rotated_tetromino, wallkick_offset

# მომხმარებლისთვის GUI შექმნა
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.tetris = Tetris()  # ტეტრისი ობიექტის შექმნა
        self.pack()
        self.create_widgets()  # UI ელემენტების შექმნა
        self.update_clock()  # საათის განახლება

    def update_clock(self):
        # დროის განახლება (ტეტრონიმოს მოძრაობა)
        self.tetris.move(1, 0)
        self.update()  
        self.master.after(int(1000*(0.66**self.tetris.level)), self.update_clock)  # დროის განახლება დონეზე

    def create_widgets(self):
        # UI კომპონენტების შექმნა
        PIECE_SIZE = 30
        self.canvas = tk.Canvas(self, height=PIECE_SIZE*self.tetris.FIELD_HEIGHT, 
                                width=PIECE_SIZE*self.tetris.FIELD_WIDTH, bg="black", bd=0)
        # კლავიატურის დაჭერა
        self.canvas.bind('<Left>', lambda _: (self.tetris.move(0, -1), self.update()))
        self.canvas.bind('<Right>', lambda _: (self.tetris.move(0, 1), self.update()))
        self.canvas.bind('<Down>', lambda _: (self.tetris.move(1, 0), self.update()))
        self.canvas.bind('<Up>', lambda _: (self.tetris.rotate(), self.update()))
        self.canvas.focus_set()
        # ცარიელი რექტანგულები თამაშის მოედნისთვის
        self.rectangles = [
            self.canvas.create_rectangle(c*PIECE_SIZE, r*PIECE_SIZE, (c+1)*PIECE_SIZE, (r+1)*PIECE_SIZE)
                for r in range(self.tetris.FIELD_HEIGHT) for c in range(self.tetris.FIELD_WIDTH)
        ]
        self.canvas.pack(side="left")
        # სტატუსი (ქულები და დონე)
        self.status_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24))
        self.status_msg.pack(side="top")
        # GAME OVER შეტყობინება
        self.game_over_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24), fg='red')
        self.game_over_msg.pack(side="top")
    
    def update(self):
        # განახლება UI-ზე
        for i, _id in enumerate(self.rectangles):
            color_num = self.tetris.get_color(i//self.tetris.FIELD_WIDTH, i % self.tetris.FIELD_WIDTH)
            self.canvas.itemconfig(_id, fill=COLORS[color_num])
    
        # სტატუსის განახლება (ქულები და დონე)
        self.status_msg['text'] = "Score: {}\nLevel: {}".format(self.tetris.score, self.tetris.level)
        # GAME OVER შეტყობინება
        self.game_over_msg['text'] = "GAME OVER.\nPress UP\nto reset" if self.tetris.game_over else ""

root = tk.Tk()
app = Application(master=root)
app.mainloop()