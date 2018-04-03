class steganography(object):

    def read(self):
        try:
            namefile = input("Enter the file name: ")
            with open(namefile, "rb") as r:
                byte = r.read(1)
                k = 0
                while byte:
                    try:
                        byte = r.read(1).decode("utf-8")
                    except:
                        continue
                    print(byte, end = "")
                    k += 1
        except FileNotFoundError:
            print("The file: ", str(namefile), " is not defined!")
            raise SystemExit
        else:
            print("Number of bytes in the ", str(namefile), " is ", str(k))

    def write(self):
        try:
            namefile = input("Enter the file name: ")
            with open(namefile, "ab") as file:
                text = input("Write down the text: ")
                file.write(text.encode("utf-8"))
        except FileNotFoundError:
            print("File: ", str(namefile), " is not defined!")
            raise SystemExit
        else:
            print("The file: ", str(namefile), " has been successfully overwritten!")


p = steganography()
p.write()
p.read()