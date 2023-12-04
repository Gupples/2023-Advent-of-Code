Steps for solving the problem:
1. Import and read a file.
2. Create two variables (number_first and number_last) and an array for storing the calibration values (values[]).
3. Walk through each line in the file. The first found number gets stored in both number_first and number_last. Any number found after that will get stored as number_last.
4. At the end of the line, create a string that has two characters; the first being number_first, the second being number_second. Convert that string to an int, and then append onto the values array.
5. After each line in the file is read and the values stored, print the sum of the values of the array. This is the solution for the day's puzzle.

Efficiency: O(n^2 (for each line in a file, and for each character in a line.))