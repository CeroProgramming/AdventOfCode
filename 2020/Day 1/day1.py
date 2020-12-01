#!/usr/bin/python3

from sys import argv

def load_file() -> list:
    with open(argv[1]) as f:
        return f.readlines()

def search_numbers(numbers: list, searched: int) -> list:
    number_of_entries = int(argv[2])
    list_pointers = lp = list()
    for i in range(number_of_entries):
        lp.append(i)

    while True:  # I assert that there is a solution to the problem
        values = [numbers[i] for i in lp]
        if sum(values) == searched:
            return values
        for i in range(len(lp)-1, -1, -1):
            if lp[i] != len(numbers) - (len(lp) - i): 
                lp[i] += 1
                for j in range(i+1, len(lp), 1):
                    lp[j] = lp[i] + j - i
                break

def prod(numbers: list) -> int:
    p = 1
    for n in numbers:
        p *= n
    return p
        
if __name__ == '__main__':
    if len(argv) < 3:
        raise AssertionError("Not enough parameters passed")
    
    lines = load_file()
    
    numbers = [int(line) for line in lines if int(line) < 2000]
    numbers.sort()

    values = search_numbers(numbers, 2020)
    
    print(prod(values)) 
