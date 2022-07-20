import pyperclip

print("Шифр Цезаря")

print("Вы хотите зашфровать(1) или расшифровать(2)?")
a = input(">")

print("Введите ключ шифрования (0 - 32):")
b = input(">")

if a == "1":
    print("Введите сообщение,которое нужно необходимо зашфровать:")
    mess = input(">")
    mess = mess.lower()
    #Цикл подсчета букв в предложение 
    d = 0
    for c in mess:
            d += 1
    alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    i = 0
    result = ""
    while i < d:
        nstr = alf.find(mess[i])
        mstr = nstr + int(b)
        if mstr > 32:
            mstr = 0
        bstr = alf[mstr]
        i += 1
        result += bstr
    print("Результат:")
    print(result)
    pyperclip.copy(result)
    print("Зашифровнное предложение скопированно в буфер обмена!")

elif a == "2":
    print("Введите сообщение,которое нужно необходимо расшифровать:")
    mess = input(">")
    mess = mess.lower()
    #Цикл подсчета букв в предложение 
    d = 0
    for c in mess:
            d += 1

    alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    i = 0
    result = ""
    while i < d:
        nstr = alf.find(mess[i])
        mstr = nstr - int(b)
        bstr = alf[mstr]
        i += 1
        result += bstr
    print("Результат:")
    print(result)
    pyperclip.copy(result)
    print("Зашифровнное предложение скопированно в буфер обмена!")
