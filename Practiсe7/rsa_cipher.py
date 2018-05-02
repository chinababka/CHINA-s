def rsa_enc(file_to_encrypt):
    import rsa, os, re

    with open("pub_key.txt", "w") as pub, open("priv_key.txt", "w") as priv:
        pub_k, priv_k = rsa.newkeys(1024)
        pub.write(str(pub_k))
        priv.write(str(priv_k))
    with open(file_to_encrypt, "rb") as victim, open("pub_key.txt", "r") as pub_k, \
            open(file_to_encrypt + ".crp", "wb") as new:
        pub_k = pub_k.read()
        e = re.findall(r"\((\d+)", pub_k)[0]
        n = re.findall(r"(\d+)\)", pub_k)[0]
        new.write(rsa.encrypt(victim.read(), rsa.PublicKey(int(e), int(n))))
        os.remove(file_to_encrypt)


def rsa_dec(file_to_decrypt):
    import rsa, re, os
    with open(file_to_decrypt, "rb") as old, open("priv_key.txt", "r") as priv_k, \
            open(file_to_decrypt[:file_to_decrypt.rfind(".")], "w") as notvictim:
        priv_k = priv_k.read()
        e = re.findall("\((\d+)", priv_k)[0]
        n = re.findall("\, (\d+)", priv_k)[0]
        d = re.findall("\, (\d+)", priv_k)[1]
        p = re.findall("\, (\d+)", priv_k)[2]
        q = re.findall("\, (\d+)\)", priv_k)[0]
        notvictim.write(str(rsa.decrypt(old.read(), rsa.PrivateKey(int(e), int(n), int(d), int(p), int(q)))))
        os.remove(file_to_decrypt)
        os.remove("priv_key.txt")
        os.remove("pub_key.txt")
