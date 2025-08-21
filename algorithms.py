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
                color_array = [
                    'green' if x > i else ('red' if x == j or x == j+1 else 'black')
                    for x in range(len(arr))
                ]
                visualizer.draw_array(canvas, arr, color_array)

    print("Sorted array:", arr) # Print the sorted array for debugging purposes.
    return arr
    # Return the sorted array.

def merge_sort(array, start, end, canvas, speed):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid, canvas, speed)
        merge_sort(array, mid + 1, end, canvas, speed)
        merge(array, start, mid, end, canvas, speed)
        
        # After all recursive calls and merging are done, print and return the sorted array.
        if start == 0 and end == len(array) - 1:
            print("Sorted array:", array)
            return array
            
def merge(array, start, mid, end, canvas, speed):
    import time
    import visualizer

    left = array[start:mid+1] # Left is the left half of the array.
    right = array[mid+1:end+1] # Right is the right half of the array.

    i = j = 0 # i and j are both leftmost elements.
    k = start

    while i < len(left) and j < len(right): # While there are still elements in both lists:
        if left[i] <= right[j]: # If the leftmost right element is more than the leftmost left element:
            array[k] = left[i] # Add the element to the merged array.
            # Animation:
            time.sleep(speed)
            color_array = [
            # The bar at index k is colored green (currently being merged), bars at index i or j+1 are colored red, all others are black.
            'green' if x == k else ('red' if x == i or x == j+1 else 'black')
            for x in range(len(array))
            ]
            visualizer.draw_array(canvas, array, color_array)
            i += 1
        else: # If the leftmost left element is more than the leftmost right element:
            array[k] = right[j]
            time.sleep(speed)
            color_array = [
                # The bar at index k is colored green (currently being merged), bars at index i or j+1 are colored red, all others are black.
                'green' if x == k else ('red' if x == i or x == j+1 else 'black')
                for x in range(len(array))
            ]
            visualizer.draw_array(canvas, array, color_array)
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        time.sleep(speed)
        color_array = [
                # The bar at index k is colored green (currently being merged), bars at index i or j+1 are colored red, all others are black.
                'green' if x == k else ('red' if x == i or x == j+1 else 'black')
                for x in range(len(array))
            ]
        visualizer.draw_array(canvas, array, color_array)
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        time.sleep(speed)
        color_array = [
            'green' if x == k else 'black'
            for x in range(len(array))
        ]
        visualizer.draw_array(canvas, array, color_array)
        j += 1
        k += 1
        
def quick_sort(array, low, high, canvas, speed):
    if low < high:
        pi = partition(array, low, high, canvas, speed)
        quick_sort(array, low, pi - 1, canvas, speed)
        quick_sort(array, pi + 1, high, canvas, speed)
    # After sorting, print and return the sorted array if it's the top-level call:
    if low == 0 and high == len(array) - 1: # In the end the element with the highest value the index
        print("Sorted array:", array)       # should be the length of the array minus one and the
        return array                        # lowest value should be index 0.                  

def partition(array, low, high, canvas, speed):
    import time
    import visualizer

    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            time.sleep(speed)
            color_array = [
                'green' if x == i or x == j else ('red' if x == high else 'black')
                for x in range(len(array))
            ]
            visualizer.draw_array(canvas, array, color_array)
    array[i + 1], array[high] = array[high], array[i + 1]
    time.sleep(speed)
    color_array = [
        'green' if x == i + 1 or x == high else 'black'
        for x in range(len(array))
    ]
    visualizer.draw_array(canvas, array, color_array)
    return i + 1

import main
array = main.on_generate_array_click()
