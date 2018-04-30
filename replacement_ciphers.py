## the ciphers of SIMPLE REPLACEMENT

## cipher of CAESAR
def caesar_enc(stroka):
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
    return caesar_dec(stroka, encrypted_string)

def caesar_dec(stroka, encrypted_string):
    decrypted_string = ""
    for i in encrypted_string.split():
        for j in i:
            if j == j.upper():
                if ord(j) <= 67:
                    j = chr(91 - (3 - (ord(j) % 65)))
                    decrypted_string += j
                else:
                    j = chr((ord(j) - 3) % 90)
                    decrypted_string += j
            else:
                if ord(j) <= 99:
                    j = chr(123 - (3 - (ord(j) % 97)))
                    decrypted_string += j
                else:
                    j = chr((ord(j) - 3) % 120)
                    decrypted_string += j
        decrypted_string += " "
    return " CAESAR METHOD:\n {0} --encrypting to--> {1} --decrypting to--> {2}".format(stroka, encrypted_string, decrypted_string)

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
    print(caesar_enc("You spin me right round"))

if __name__ == "__main__":
    main()