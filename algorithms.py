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
        
# Only does one iteration, but does work effectively:

def quick_sort(array, low, high, speed, canvas):
    import time
    import visualizer 

    if len(array) <= 1:
        return array
        
    else:
        min = 0
        high = []
        low = []
        while min < len(high) and min < len(low):
            pivot = array.pop() # Delete the value at the end of the sequence and assign it to a variable called pivot.
            
            for i in array:
                if i > pivot:
                    high.append(i)
                    time.sleep(speed)
                    color_array = [
                        'green' if x == i else ('red' if x == pivot else 'black')
                        for x in range(len(array))
                    ]
                    visualizer.draw_array(canvas, array, color_array)
                else:
                    low.append(i)
                    color_array = [
                        'green' if x == i else ('red' if x == pivot else 'black')
                        for x in range(len(array))
                    ]
                    visualizer.draw_array(canvas, array, color_array)
    # All the code gets skipped and the array is immedietly run.
    print('Sorted array:', array)
    return array
    
import main
array = main.on_generate_array_click()
