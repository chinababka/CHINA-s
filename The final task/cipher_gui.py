from tkinter import *

def caesar_enc(stroka, k):
    k = int(k)
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
    return itog(encrypted_string)

def itog(k):
    x = StringVar()
    x.set(k)
    encryption_output = Label(text="THE RESULT")
    encryption_output.pack()
    encryption_text = Entry(bd=3, font=16, textvariable=x)
    encryption_text.pack(fill=X, padx=10)


def main():
    root = Tk()
    root.geometry("700x350")
    root.title("THE CAESAR CIPHER")

    main_input = Label(text="THE TEXT TO ENCRYPT")
    main_input.pack()
    main_text = Entry(bd=3, font=16)
    main_text.pack(fill=X, padx=10)

    key_input = Label(text="KEY")
    key_input.pack()
    key_text = Entry(bd=3, font=16, width=2)
    key_text.pack()

    run = Button(text='RUN TO START', background="#CC9", padx=20, pady=10, width=10, command=lambda: caesar_enc(main_text.get(), key_text.get()))
    run.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()