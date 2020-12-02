#!/usr/bin/python3

def load_file(filename: str) -> list:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def convert_lines(lines: list) -> list:
    return [line.replace(':', '').split(' ') for line in lines]

def check_value_set(value_set: list, task: int) -> bool:
    minimal = int(value_set[0].split('-')[0])
    maximal = int(value_set[0].split('-')[1])

    searched = value_set[1]
    password = value_set[2]

    if task == 1:
        count = 0
        for letter in password:
            count += int(letter == searched)
    
        return count >= minimal and count <= maximal
    else:
        first_letter = password[minimal-1]
        second_letter = password[maximal-1]
        return (first_letter == searched and second_letter != searched) or (first_letter != searched and second_letter == searched)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Solve the day 2 puzzle.')
    parser.add_argument('--input', '-i', type=str, 
                    help='Puzzle input file.')
    parser.add_argument('--task', '-t', type=int, choices=range(1, 3), default=1,
                    help='Select task 1 or 2.') 
    args = parser.parse_args()
    
    lines = load_file(args.input)
    values_list = convert_lines(lines)
    valid_count = 0
    for value_set in values_list:
        valid_count += int(check_value_set(value_set, args.task))

    print(valid_count)


