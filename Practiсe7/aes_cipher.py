def aes_enc(file):
    import pyAesCrypt, os
    password = input("->Password:")
    bufferSize = 64 * 1024
    try:
        pyAesCrypt.encryptFile(file, str(file + ".crp"), password, bufferSize)
        os.remove(file)
    except FileNotFoundError:
        print("->Sorry, the file %s is not found" % file)
    else:
        print("->The file %s has been successfully encrypted!" % file)


def aes_dec(file):
    import pyAesCrypt, os
    password = input("->Password:")
    bufferSize = 64 * 1024
    try:
        pyAesCrypt.decryptFile(file, file[:file.rfind(".")], password, bufferSize)
        os.remove(file)
    except FileNotFoundError:
        print("->Sorry, the file %s is not found" % file)
    except ValueError:
        print("->Wrong password! Try another one")
    else:
        print("->The file %s has been successfully decrypted!" % file)
