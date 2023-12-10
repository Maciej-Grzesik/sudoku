import random

def generuj_sudoku():
    # Tworzenie pustej tablicy 9x9 (81-elementowej listy)
    sudoku = [0] * 81

    # Wypełnienie losowymi liczbami w losowych miejscach
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(liczby)

    for i in range(20):  # Ilość wpisanych liczb (można dostosować)
        losowe_index = random.randint(0, 80)
        if sudoku[losowe_index] == 0:
            sudoku[losowe_index] = liczby[i % 9]

    return sudoku

# Przykładowe użycie funkcji
sudoku = generuj_sudoku()
print(sudoku)