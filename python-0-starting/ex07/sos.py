import sys


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',  ' ': '/'
}


def main():
    morse_code = ""
    error_message = "AssertionError: the arguments are bad"
    if len(sys.argv) != 2:
        morse_code = error_message
    else:
        try:
            s = str(sys.argv[1])
            # print(s.upper())
            for c in s.upper():
                morse_code += morse_code_dict[c]
        except KeyError:
            morse_code = error_message
    print(morse_code)


if __name__ == "__main__":
    main()
