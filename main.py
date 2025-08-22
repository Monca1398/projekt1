# main.py
# Projekt 2: Textový analyzátor

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# Tři předpřipravené texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
]

SEPARATOR = "-" * 40

username = input("username: ")
password = input("password: ")

# //// Kontrola, zda jméno i heslo odpovídají správné dvojici ////
if USERS.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

# //// Pokud je přihlášení úspěšné ////
print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(SEPARATOR)

# //// Výběr textu ////
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

# //// Kontrola, zda vstup je číslo ////
if not choice.isdigit():
    print("Invalid input, terminating the program..")
    exit()

# //// Převedení vstupu na index (od 0) ////
index = int(choice) - 1

# //// Kontrola, zda index spadá do rozsahu textů ////
if index not in range(len(TEXTS)):
    print("Number out of range, terminating the program..")
    exit()

text = TEXTS[index]

# //// Rozdělení textu na slova + odstranění čárek a teček ////
words = [w.strip(".,") for w in text.split()]

# //// Výpočet základních statistik ////
num_words = len(words)                            # celkový počet slov
titlecase_words = sum(1 for w in words if w.istitle())  # slova začínající velkým písmenem
# !!! for w in words → pro každé slovo v seznamu words !!!
uppercase_words = sum(1 for w in words if w.isupper())  # slova psaná VELKÝMI písmeny
lowercase_words = sum(1 for w in words if w.islower())  # slova psaná malými písmeny
numeric_strings = [w for w in words if w.isdigit()]     # číselné řetězce
sum_numbers = sum(int(n) for n in numeric_strings)      # součet čísel

# //// Výpis statistik ////
print(SEPARATOR)
print(f"There are {num_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")

# //// Sloupcový graf ////
print(SEPARATOR)
print(f"{'LEN':>3}|{'OCCURRENCES':^20}|NR.")
print(SEPARATOR)

# //// Slovník: délka slova -> počet výskytů ////
lengths = {}
for w in words:
    lengths[len(w)] = lengths.get(len(w), 0) + 1

# //// Výpis grafu (seřazený podle délky slova) ////
for length in sorted(lengths):
    stars = "*" * lengths[length]
    print(f"{length:>3}|{stars:<20}|{lengths[length]}")
