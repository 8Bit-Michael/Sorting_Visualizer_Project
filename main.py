def arr_value(val):
    print(f"Array value: {val}")

def speed_value(val):
    print(f"Speed value: {val}")

def create_main_window():
    import tkinter as tk
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
    bubble_sort_button.configure(command=bubble_sort_vis)

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
    merge_sort_button.configure(command=merge_sort_vis)

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
    quick_sort_button.configure(command=quick_sort_vis)

    quick_sort_button.place(x=10, y=310)

    gen_array_button = tk.Button(
    root, 
    background="black", 
    foreground="white", 
    activebackground="Blue", 
    text="Generate array",
    highlightthickness=2,
    highlightcolor="White",
    width=15,
    height=1,
    border=0,
    cursor='hand1',
    font=('Arial', 16, 'bold')
    )
    gen_array_button.configure(command=on_generate_array_click)

    gen_array_button.place(x=10, y=370)

    global custom_array_box
    custom_array_box = tk.Text(
    root, 
    width = 23,
    height = 2.4
    )
    custom_arr_title = tk.Label(root, text='Custom array', font=('Arial', 11))
    custom_arr_title.place(x=260, y=350)
    
    custom_array_box.place(x=220, y=373)

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

# array_length will be retrieved inside functions after arr_slider is created.

def on_generate_array_click():
    import tkinter as tk
    import visualizer
    import utils
    array_length = arr_slider.get()
    if array_length < 2:
        utils.arr_error_window()
    else:
        array = utils.generate_array(0, 100, array_length)
        # The start, the maximum value, and the length of the array.
        canvas = tk.Canvas(root, width=400, height=250, bg='white')
        canvas.place(x=400, y=100)
        color_array = visualizer.get_color_array(array_length, status='unsorted', active_indices=[])
        visualizer.draw_array(canvas, array, color_array)
        return array
def bubble_sort_vis():
    import tkinter as tk
    import visualizer
    import algorithms
    array = on_generate_array_click()
    canvas = tk.Canvas(root, width=400, height=250, bg='white')
    canvas.place(x=400, y=100)
    speed = speed_slider.get() / 100
    array_length = arr_slider.get()
    if array_length > 2:
        sorted_array = algorithms.bubble_sort(array, canvas, speed)
        visualizer.draw_array(canvas, sorted_array, ['black'] * len(sorted_array))
    else:
        raise ValueError("The array should have two or more elements.")
def merge_sort_vis():
    import tkinter as tk
    import visualizer
    import algorithms
    import utils
    array = on_generate_array_click()
    canvas = tk.Canvas(root, width=400, height=250, bg='white')
    canvas.place(x=400, y=100)
    speed = speed_slider.get() / 100
    array_length = arr_slider.get()
    if array_length > 2:
        sorted_array = algorithms.merge_sort(array, 0, len(array) - 1, canvas, speed)
        visualizer.draw_array(canvas, sorted_array, ['black'] * len(sorted_array))
    else:
        raise ValueError("The array should have two or more elements.")
def quick_sort_vis():
    import tkinter as tk
    import visualizer
    import algorithms
    array = on_generate_array_click()
    canvas = tk.Canvas(root, width=400, height=250, bg='white')
    canvas.place(x=400, y=100)
    speed = speed_slider.get() / 100
    array_length = arr_slider.get()
    # Note: quick_sort only returns the sorted array at the top-level call.
    if array_length > 2:
        sorted_array = algorithms.quick_sort(array, 0, len(array) - 1, canvas, speed)
        if sorted_array is None:   
            sorted_array = array
        visualizer.draw_array(canvas, sorted_array, ['black'] * len(sorted_array))
    elif array_length < 2:
        visualizer.draw_array(canvas, sorted_array, ['black'] * len(sorted_array))
    else:
        raise ValueError("The array should have two or more elements.")

create_main_window()
