import tkinter as tk
import config
import utils
import visualizer
import random

def arr_value(val):
    print(f"Array value: {val}")

def speed_value(val):
    print(f"Speed value: {val}")

def create_main_window():
    
    # Describes the purpose of the script:
    global root
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Sorting Visualizer")
    
    label = tk.Label(root, text="Sorting Visualizer", font=('Arial', 16))
    label.pack(padx=20, pady=20)

    bubble_sort_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Bubble sort",
    highlightthickness=2,
    highlightcolor="White",
    width=30,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )

    bubble_sort_button.place(x=10, y=110)

    merge_sort_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Merge sort",
    highlightthickness=2,
    highlightcolor="White",
    width=30,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )
    bubble_sort_button.configure(command=start_sorting)

    merge_sort_button.place(x=10, y=210)

    quick_sort_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Quick sort",
    highlightthickness=2,
    highlightcolor="White",
    width=30,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )

    quick_sort_button.place(x=10, y=310)

    start_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Start",
    highlightthickness=2,
    highlightcolor="White",
    width=7,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )

    start_button.place(x=10, y=380)

    gen_array_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Generate array",
    highlightthickness=2,
    highlightcolor="White",
    width=16,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )

    gen_array_button.place(x=120, y=380)
    gen_array_button.configure(command=on_generate_array_click)

    global arr_slider
    arr_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=arr_value)
    arr_slider.pack()
    arr_text = tk.Label(root, text="Array Size", font=('Arial', 12))
    arr_text.place(x=20, y=430)
    arr_slider.place(x=10, y=450)

    global speed_slider
    speed_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=speed_value)
    speed_slider.pack()
    speed_text = tk.Label(root, text="Speed", font=('Arial', 12))
    speed_text.place(x=170, y=430)
    speed_slider.place(x=160, y=450)

    # Runs the script:
    root.mainloop()

def on_generate_array_click():
    array_length = arr_slider.get()
    array = utils.generate_array(0, 100, array_length)
    # The start, the maximum value, and the length of the array.
    canvas = tk.Canvas(root, width=400, height=250, bg='white')
    canvas.place(x=400, y=100)
    visualizer.draw_array(canvas, array, ['black'] * array_length)
    return array

def start_sorting(): # Use later to implement different sorting algorithms.
    import algorithms
    array = on_generate_array_click()
    canvas = tk.Canvas(root, width=400, height=250, bg='white')
    canvas.place(x=400, y=100)
    speed = speed_slider.get() / 100
    sorted_array = algorithms.bubble_sort(array, canvas, speed)
    visualizer.draw_array(canvas, sorted_array, ['black'] * len(sorted_array))

create_main_window()
create_main_window()
