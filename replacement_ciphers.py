## the ciphers of SIMPLE REPLACEMENT

## cipher of CAESAR
def caesar(stroka):
    encrypted_string = ""
    for i in stroka.split():
        for j in i:
            if j == j.upper():
                if ord(j) >= 88:
                    j = chr(65 + (ord(j) + 3) % 91)
                    encrypted_string += j
                else:
                    j = chr((ord(j) + 3) % 91)
                    encrypted_string += j
            else:
                if ord(j) >= 120:
                    j = chr(97 + (ord(j) + 3) % 123)
                    encrypted_string += j
                else:
                    j = chr((ord(j) + 3) % 123)
                    encrypted_string += j
        encrypted_string += " "
    return " CAESAR METHOD:\n {} ---> {}".format(stroka, encrypted_string)

## cipher of ATBASH
def at_bash(stroka):
    encrypted_string = ""
    for i in stroka.split():
        for j in i:
            if j == j.upper():
                j = chr(90 - ord(j) + 65)
                encrypted_string += j
            else:
                j = chr(122 - ord(j) + 97)
                encrypted_string += j
        encrypted_string += " "
    return " ATBASH METHOD:\n {} ---> {}".format(stroka, encrypted_string)


def main():
    print("SIMPLE REPLACEMENTS:")
    print(at_bash("You spin me right round"), "\n")
    print(caesar("You spin me right round"))

if __name__ == "__main__":
    main()