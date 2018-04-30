## the ciphers of SIMPLE REPLACEMENT

## cipher of CAESAR
def caesar_enc(stroka, k):
    encrypted_string = ""
    for i in stroka.split():
        for j in i:
            if j == j.upper():
                if ord(j) >= (91 - k):
                    j = chr(65 + (ord(j) + k) % 91)
                    encrypted_string += j
                else:
                    j = chr((ord(j) + k) % 91)
                    encrypted_string += j
            else:
                if ord(j) >= (123 - k):
                    j = chr(97 + (ord(j) + k) % 123)
                    encrypted_string += j
                else:
                    j = chr((ord(j) + k) % 123)
                    encrypted_string += j
        encrypted_string += " "
    return caesar_dec(stroka, encrypted_string, k)


def caesar_dec(stroka, encrypted_string, k):
    decrypted_string = ""
    for i in encrypted_string.split():
        for j in i:
            if j == j.upper():
                if ord(j) <= (65 + k - 1):
                    j = chr(91 - (k - (ord(j) % 65)))
                    decrypted_string += j
                else:
                    j = chr((ord(j) - k) % 90)
                    decrypted_string += j
            else:
                if ord(j) <= (97 + k - 1):
                    j = chr(123 - (k - (ord(j) % 97)))
                    decrypted_string += j
                else:
                    j = chr((ord(j) - k) % 120)
                    decrypted_string += j
        decrypted_string += " "
    return " CAESAR METHOD:\n {0} --encrypting to--> {1} --decrypting to--> {2}".format(stroka, encrypted_string,
                                                                                        decrypted_string)

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
    return " ATBASH METHOD:\n {} --encrypting to--> {}".format(stroka, encrypted_string)


def main():
    print("SIMPLE REPLACEMENTS:")
    print(at_bash("You spin me right round"), "\n")
    key = int(input("Enter the key: "))
    print(caesar_enc("You spin me right round", key))

if __name__ == "__main__":
    main()