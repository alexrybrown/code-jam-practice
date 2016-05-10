def main():
    # First line of input will be the number of cases
    cases = int(input())
    for i in range(1, cases + 1):
        number = int(input())
        # Check to see if the number is anything but 0
        if number:
            # Make a list with the numbers to find utilizing the indices as the numbers
            # Each index will be 0 if not found and 1 if found
            numbers_found = [0 for _ in range(0, 10)]
            # Keep track of the iterations through the while loop and the current number
            count = 0
            current_number = 0
            # There will be ten occurrences of 1 when all the numbers have been found
            while numbers_found.count(1) != 10:
                count += 1
                # On the first iteration through we want the actual number and after that we will set current number
                check_number = current_number and current_number or number
                result = str(check_number)
                # Using our check_number as a temporary variable, find all of the digits in it and set the value
                # in the list to 1
                while check_number:
                    numbers_found[check_number % 10] = 1
                    check_number = int(check_number/10)
                # Multiply the number by the iteration we are on plus one
                current_number = number * (count + 1)
        else:
            result = 'INSOMNIA'
        print('Case #{i}: {result}'.format(**locals()))

if __name__ == '__main__':
    main()
