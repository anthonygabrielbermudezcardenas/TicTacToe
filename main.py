from class_Body import Body

while True:
    Body().run()

    user_input = "a"
    while user_input not in "ny":
        user_input = input("Quieres jugar de nuevo? (y/n)").lower()

    if user_input == "y":
        continue
    else:
        print("HASTA LA VISTA!!!")
        exit()