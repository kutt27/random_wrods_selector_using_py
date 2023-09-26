import tkinter as tk
import random
import data_arrays  # Importing the data_arrays module
import gui  # Importing the gui module

def generate_random_text():
    random_item1 = random.choice(data_arrays.array1)
    random_item2 = random.choice(data_arrays.array2)
    generated_text = f"Random Text: {random_item1} - {random_item2}"
    gui.result_label.config(text=generated_text)

def main():
    gui.main()  # Call the main() function from the gui module

if __name__ == "__main__":
    main()
