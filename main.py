import os
import time

def clear_screen():
    if os.name == 'nt': # Windows
        _ = os.system('cls')
    else: # MacOS/Linux
        _ = os.system('clear')

def print_array_with_pointer(array, pointer_index):
    display_str = "Array: ["
    for i, val in enumerate(array):
        if i == pointer_index:
            display_str += f" >{val}< "
        else:
            display_str += f" {val} "
        if i < len(array) - 1:
            display_str += ","
    display_str += "]"
    print(display_str)


def linear_search_interactive(array, target):
    found = False
    for i in range(len(array)):
        clear_screen()
        print(f"--- Searching for: {target} ---")
        print_array_with_pointer(array, i)
        print(f"\nStep {i + 1}:")
        print(f"Comparing target '{target}' with element at index {i}, which is '{array[i]}'.")

        time.sleep(0.5)

        if array[i] == target:
            print("\nResult: Match found!")
            print(f"Data '{target}' found at index {i}.")
            found = True
            break
        else:
            print(f"\nResult: Not a match.")
            input("Press Enter to check the next element...")
            
    if not found:
        clear_screen()
        print(f"--- Search Complete ---")
        print(f"Array: {array}")
        print(f"Target: {target}")
        print(f"\nSorry, the data '{target}' was not found in the array after checking all elements.")
        return -1
        
    return i


if __name__ == "__main__":
    clear_screen()
    print("--- Interactive Linear Search Program ---")
    print("The program will pause at each step of the search.")

    input_str = input("\nEnter a list of numbers, separated by commas: ")
    try:
        user_array = [int(num.strip()) for num in input_str.split(',')]
    except ValueError:
        print("Error: Please enter a valid list of numbers.")
        exit()

    try:
        search_value = int(input("Enter the number you want to search for: "))
    except ValueError:
        print("Error: Please enter a valid number to search for.")
        exit()
        
    print("\nStarting the search. Press Enter to move through the steps.")
    time.sleep(2)

    linear_search_interactive(user_array, search_value)
    
    print("\n--- Program Finished ---")

