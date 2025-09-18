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


def main() -> None:
    """Main function to convert input string to Morse code."""
    morse_code = ""
    error_message = "AssertionError: the arguments are bad"
    if len(sys.argv) != 2:
        morse_code = error_message
    else:
        try:
            s = str(sys.argv[1])
            for c in s.upper():
                morse_code += morse_code_dict[c]
                morse_code += ' '
        except KeyError:
            morse_code = error_message
        morse_code = morse_code.strip()
    print(morse_code)


if __name__ == "__main__":
    main()
