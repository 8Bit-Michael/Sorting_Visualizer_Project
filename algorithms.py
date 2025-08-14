def bubble_sort(arr, canvas, speed):
    import time
    import visualizer
    for i in range(len(arr)-1, 0, -1):
        # For each iteration through the unsorted parts of the array:
        for j in range(i):
           # For each element in that iteration:
           if arr[j] > arr[j+1]: # If the value of the current element is greater than the next element.
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap the elements.
                time.sleep(speed) # Make sure speed is an integer.
                visualizer.draw_array(canvas, arr, ['red' if x == j or x == j+1 else 'black' for x in range(len(arr))])
                # If the current element is being compared to another element, color them red, otherwise black.
        visualizer.draw_array(canvas, arr, ['black'] * len(arr))
        # After each pass, the largest element is at the end of the array.
    print("Sorted array:", arr) # Print the sorted array for debugging purposes.
    return arr
    # Return the sorted array.

import main
array = main.on_generate_array_click()
