import aes_cipher, rsa_cipher

def main():
    print("-------------------------------------------------\n"
          "If you wanna use AES, try this format of input:  \n"
          "filename.* A --> encryption by AES cipher\n"
          "filename.* -A --> decryption by AES cipher\n"
          "-------------------------------------------------\n"
          "If you wanna use RSA, try this format of input:  \n"
          "filename.* R --> encryption by RSA cipher\n"
          "filename.* -R --> decryption by RSA cipher\n"
          "-------------------------------------------------")
    try:
        your_file, method = [i for i in input("\nEnter the command:").split()]
        if len(method) == 1:
            if method[0] == "A":
                aes_cipher.aes_enc(your_file)
            elif method[0] == "R":
                rsa_cipher.rsa_enc(your_file)
            else:
                print("idi naher")
        elif len(method) == 2:
            if method[1] == "A":
                aes_cipher.aes_dec(your_file)
            elif method[1] == "R":
                rsa_cipher.rsa_dec(your_file)
            else:
                print("idi naher")
        else:
            print("I have no idea what you want")

    except ValueError:
        print("Some troubles with your input, try again please")


if __name__ == '__main__':
    main()