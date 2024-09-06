from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from {algorithm} import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=3)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

ARRAY_LENGTH = 1000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 1000
    array = [randint(0, 100000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    # run_sorting_algorithm(algorithm="sorted", array=array)
    
    print(f"Testing all algorithms with {ARRAY_LENGTH} random ints:")
    run_sorting_algorithm(algorithm="insertionSort", array=array)
    run_sorting_algorithm(algorithm="selectionSort", array=array)
    run_sorting_algorithm(algorithm="bubbleSort", array=array)
    run_sorting_algorithm(algorithm="mergeSort", array=array)
    run_sorting_algorithm(algorithm="quickSort", array=array)
    run_sorting_algorithm(algorithm="timSort", array=array)
    run_sorting_algorithm(algorithm="minheapSort", array=array)
    run_sorting_algorithm(algorithm="maxheapSort", array=array)
    print()
    array = [randint(0, 100000) for i in range(ARRAY_LENGTH*10)]
    print(f"Testing all algorithms with {ARRAY_LENGTH*10} random ints:")
    run_sorting_algorithm(algorithm="insertionSort", array=array)
    run_sorting_algorithm(algorithm="selectionSort", array=array)
    run_sorting_algorithm(algorithm="bubbleSort", array=array)
    run_sorting_algorithm(algorithm="mergeSort", array=array)
    run_sorting_algorithm(algorithm="quickSort", array=array)
    run_sorting_algorithm(algorithm="timSort", array=array)
    run_sorting_algorithm(algorithm="minheapSort", array=array)
    run_sorting_algorithm(algorithm="maxheapSort", array=array)
    print()
    array = [i for i in range(ARRAY_LENGTH*10)]
    print(f"Testing all algorithms with {ARRAY_LENGTH*10} pre-sorted ints:")
    run_sorting_algorithm(algorithm="insertionSort", array=array)
    run_sorting_algorithm(algorithm="selectionSort", array=array)
    run_sorting_algorithm(algorithm="bubbleSort", array=array)
    run_sorting_algorithm(algorithm="mergeSort", array=array)
    run_sorting_algorithm(algorithm="quickSort", array=array)
    run_sorting_algorithm(algorithm="timSort", array=array)
    run_sorting_algorithm(algorithm="minheapSort", array=array)
    run_sorting_algorithm(algorithm="maxheapSort", array=array)
    print()
    array = [randint(0, 20) for i in range(ARRAY_LENGTH*10)]
    print(f"Testing all algorithms with {ARRAY_LENGTH*10} random ints from 0 to 20:")
    run_sorting_algorithm(algorithm="insertionSort", array=array)
    run_sorting_algorithm(algorithm="selectionSort", array=array)
    run_sorting_algorithm(algorithm="bubbleSort", array=array)
    run_sorting_algorithm(algorithm="mergeSort", array=array)
    run_sorting_algorithm(algorithm="quickSort", array=array)
    run_sorting_algorithm(algorithm="timSort", array=array)
    run_sorting_algorithm(algorithm="minheapSort", array=array)
    run_sorting_algorithm(algorithm="maxheapSort", array=array)

# Fra tidsmålinga så ser man at n^2 algoritmene er tregere enn n log n algoritmene, som forventet.
# Hvis lista er sortert så er bubble sort raskest fordi den trenger bare å gå over lista en gang for å se at den er sortert.
# Når det bare var tall mellom 0 og 20 så er alle algoritmene like raske, untatt quicksort, som blir mye tregere,
# hvis spredningen blir enda mindre så vil quicksort nå python sin max recursion depth

