from day_1 import solutions_first_part, solutions_second_part, read_input

YEAR = 2020


if __name__ == '__main__':
    input_data = tuple(read_input())

    print('The first answer:', solutions_first_part(input_data, YEAR))
    print('The second answer:', solutions_second_part(input_data, YEAR))
