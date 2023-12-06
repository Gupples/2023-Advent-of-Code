# Creator: Jared Davey
# Description: This program will read a file. For each line in the file, it 
#   will store the first and last numerical character in an array, calculate
#   the sum of those numbers, and then display the sum. This version works with
#   jsons instead of .txt files.

def main():
    calibration_lines = read_file()
    if len(calibration_lines) > 0:
        calculate_values(calibration_lines)

def read_file():
    filename = input("Enter the calibration file name. ")
    try:
        with open(filename, 'r') as file:
            lines = []
            text = file.read()
            for line in text:
                lines.append(line)
            return lines
    except:
        print("Could not read the file.")
        return []
    
def calculate_values(lines):
    values = []
    for ine in lines:
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

if __name__ == "__main__":
    main()