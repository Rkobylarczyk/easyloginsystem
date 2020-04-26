zarejestrowany = input("Czy jesteś zarejestrowany? ")

if zarejestrowany == "nie":
    print("Załóż konto")

if zarejestrowany == "tak":
    login = input("Podaj mi swój login: ")
    haslo = input("Podaj mi swoje hasło ")

    with open("passy.txt", "r") as passyfile:
        if (login + "," + haslo + "\n") in passyfile.readlines():
            print("Siema, wbijaj")
        else:
            print("Wyjazd")


else:
    login = input("Jaki chcesz mieć login? ")
    print("Twoim loginem będzie: ", login, ".")

    haslo = input("Jakie chcesz miec haslo? ")

    file = open("passy.txt", "a")
    file.write(login)
    file.write(",")
    file.write(haslo)
    file.write("\n")
    file.close()

    print("Dzięki ryju, zarejestrowałeś się.")

zarejestrowany = input("Czy jesteś zarejestrowany? ")

if zarejestrowany == "nie":
    login = input("Podaj mi swój login: ")
    haslo = input("Podaj mi swoje hasło ")

    with open("passy.txt", "r") as passyfile:
        if (login + "," + haslo + "\n") in passyfile.readlines():
            print("Siema, wbijaj")
        else:
            print("Wyjazd")

if zarejestrowany == "tak":
    login = input("Podaj mi swój login: ")
    haslo = input("Podaj mi swoje hasło ")

    with open("passy.txt", "r") as passyfile:
        if (login + "," + haslo + "\n") in passyfile.readlines():
            print("Siema, wbijaj")
        else:
            print("Wyjazd")