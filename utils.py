def generate_array(min_val, max_val, size):
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]

def arr_error_window():
    import tkinter as tk
    # Describes the purpose of the script:
    global root
    root = tk.Tk()
    root.geometry("650x300")
    root.title(f"Array Error")
    
    label = tk.Label(root, text=f"Error: You cannot create an array with under two elements.", font=('Arial', 16, 'bold'))
    label.pack(padx=0, pady=125)

def sorting_error_window():
    import tkinter as tk
    # Describes the purpose of the script:
    global root
    root = tk.Tk()
    root.geometry("650x300")
    root.title(f"Sorting Error")
    
    label = tk.Label(root, text=f"Error: You cannot modify the graph while sorting.", font=('Arial', 16, 'bold'))
    label.pack(padx=0, pady=125)
