def find_pattern_bBob(text):
    count = 0  # Initiate the counter for matches

    # Iterate through the text by index

    for i in range(len(text)):

        # Check if the current character is a 'b'

        if text[i] == 'b':

            try:

                # Given that the current character is a 'b' look ahead in the text and check if the substring ends with 'Bob'

                if text[i:].endswith('Bob'):
                    count += 1  # Update the counter if the pattern is found

            except IndexError:

                # If looking ahead goes beyond the text, just continue to the next iteration

                continue

    return count  # Return the total count of matches