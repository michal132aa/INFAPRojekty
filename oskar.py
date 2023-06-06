import tkinter as tk

class AlgorithmShowcaseGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Algorithm Showcase")
        
        # Create GUI elements
        self.label = tk.Label(master, text="Select an algorithm:")
        self.label.pack()

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("")

        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, "NWD", "Szyfr Ceara", "Sortowanie babelkowe")
        self.algorithm_menu.pack()

        self.run_button = tk.Button(master, text="Run", command=self.run_algorithm)
        self.run_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def run_algorithm(self):
        algorithm = self.algorithm_var.get()
        result = self.execute_algorithm(algorithm)
        self.result_label.configure(text=f"Result: {result}")

    def execute_algorithm(self, algorithm):
        # Implement your algorithm logic here
        # This is just a placeholder
        if algorithm == "NWD":
            return "Result 1"
        elif algorithm == "Szyfr Ceara":
            return "Result 2"
        elif algorithm == "Sortowanie babelkowe":
            return "Result 3"
        else:
            return "Invalid algorithm selection"

class AlgorithmShowcaseGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Algorithm Showcase")
        
        # Create GUI elements
        self.label = tk.Label(master, text="Select an algorithm:")
        self.label.pack()

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("")

        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, "NWD", "Szyfr Ceara", "Sortowanie babelkowe")
        self.algorithm_menu.pack()

        self.run_button = tk.Button(master, text="Run", command=self.run_algorithm)
        self.run_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def run_algorithm(self):
        algorithm = self.algorithm_var.get()
        result = self.execute_algorithm(algorithm)
        self.result_label.configure(text=f"Result: {result}")

    def execute_algorithm(self, algorithm):
        # Implement your algorithm logic here
        # This is just a placeholder
        if algorithm == "NWD":
            return "Result 1"
        elif algorithm == "Szyfr Ceara":
            return "Result 2"
        elif algorithm == "Sortowanie babelkowe":
            return "Result 3"
        else:
            return "Invalid algorithm selection"


def znajdz_nwd(a, b):
    """
    Funkcja znajdująca największy wspólny dzielnik (NWD) dla dwóch liczb.
    :param a: Pierwsza liczba
    :param b: Druga liczba
    :return: Największy wspólny dzielnik
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def szyfruj(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                przesuniecie_mod = ord('A')
            else:
                przesuniecie_mod = ord('a')
            przesuniecie_znak = (ord(znak) - przesuniecie_mod + przesuniecie) % 26 + przesuniecie_mod
            zaszyfrowany_tekst += chr(przesuniecie_znak)
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst


def deszyfruj(tekst, przesuniecie):
    return szyfruj(tekst, -przesuniecie)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Flagę, która wskazuje, czy były dokonane zamiany w obecnej iteracji swapped = False
        swapped = False

        # Iterujemy po liście, porównując i zamieniając sąsiednie elementy for j in range(n - 1 - i):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 
        # Jeśli w tej iteracji nie było zamian, lista jest już posortowana if not swapped:
        if not swapped:
            break
    return arr


if __name__ == '__main__':
    # TODO: Wprowadź dwie liczby dla których chcesz obliczyć NWD
    root = tk.Tk()
    app = AlgorithmShowcaseGUI(root)
    root.mainloop()    
    liczba_a = 24
    liczba_b = 36
    wynik = znajdz_nwd(liczba_a, liczba_b)
    print(f"Największy wspólny dzielnik dla {liczba_a} i {liczba_b} to: {wynik}")
