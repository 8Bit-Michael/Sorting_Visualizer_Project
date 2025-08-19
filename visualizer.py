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
        # Ensure color_array has enough elements.
        color = color_array[i] if i < len(color_array) else 'black'
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)
    canvas.update()

def get_color_array(length, status='compare', active_indices=None):
    if active_indices is None:
        active_indices = []

    color_array = ['black'] * length

    if status == 'compare':
        for i in active_indices:
            color_array[i] = 'red'
        return color_array

    elif status == 'sorted':
        for i in range(length):
            color_array[i] = 'green'
        return color_array

    elif status == 'unsorted':
        # Unsorted, just return all black.
        return color_array

    else:
        # Fallback for unknown status.
        return color_array
