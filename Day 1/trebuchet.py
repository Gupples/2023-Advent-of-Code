# Creator: Jared Davey
# Description: This program will read a file. For each line in the file, it 
#   will store the first and last numerical character in an array, calculate
#   the sum of those numbers, and then display the sum.

def main():
    filename = input("Enter the calibration file name. ")
    try:
        with open(filename, 'r') as file:
            values = []
            for line in file:
                number_first = '_'
                number_last = "_"
                for character in line:
                    if character.isnumeric():
                        if number_first == "_":
                            number_first = character
                        number_last = character
                    value_string = number_first + number_last
                values.append(int(value_string))
            print(sum(values))
    except:
        print(f"File '{filename}' could not be read.")

if __name__ == "__main__":
    main()