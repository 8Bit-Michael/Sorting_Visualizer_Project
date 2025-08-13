def draw_array(canvas, array, color_array):
    canvas.delete("all")
    if len(array) == 0:
        return
    bar_width = 400 / len(array)
    for i, value in enumerate(array):
        x0 = i * bar_width # Left edge of the bar.
        y0 = 250 - (value * 250 / max(array)) # Height of the bar.
        x1 = x0 + bar_width # Right edge of the bar.
        y1 = 250 # Bottom edge of the bar.
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    canvas.update()
           
