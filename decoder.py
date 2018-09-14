# Phil Dominguez

CHAR_BIT_LEN = 8
CHAR_PRINT_MAX = 100
PREAMBLE = 'CAPTIVATION'
LEN_PREAMBLE = len(PREAMBLE)

def main():
    binary = ''
    char_print_count = 0
    cur_preamble_binary = ''
    preamble_found = False
    preamble_index = 0

    while True:
        # Read input stream forever
        binary += input()
        more_chars = True

        while more_chars:
            char_binary = binary[:CHAR_BIT_LEN]

            if len(char_binary) < CHAR_BIT_LEN:
                # Not enough remaining bits to read a full char; keep for next input
                more_chars = False
            else:
                letter = chr(int(char_binary, 2))

                if preamble_found:
                    # We saw the full preamble, keep printing
                    print(letter)
                    binary = binary[CHAR_BIT_LEN:]
                    char_print_count += 1

                    if char_print_count == CHAR_PRINT_MAX:
                        preamble_found = False
                        char_print_count = 0
                elif letter == PREAMBLE[preamble_index]:
                    # Found the next char in the preamble
                    preamble_index += 1
                    binary = binary[CHAR_BIT_LEN:]
                    cur_preamble_binary += char_binary

                    if preamble_index == LEN_PREAMBLE:
                        # Full preamble found
                        preamble_index = 0
                        preamble_found = True
                        cur_preamble_binary = ''
                else:
                    if cur_preamble_binary:
                        # This means there was a preamble false start, so we have to go
                        # back to process one bit at a time
                        binary = cur_preamble_binary + binary
                        cur_preamble_binary = ''

                    preamble_index = 0
                    binary = binary[1:]

if __name__ == "__main__":
    main()
