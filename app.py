import random
response = "Y"
response = input("Do you want to roll a dice? (Answer Y/N): ")
while response == "Y":
    num = random.randint(1,6)
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  O  ]")
        print("[     ]")
        print("[-----]")
    elif num == 2:
        print("[-----]")
        print("[     ]")
        print("[O   O]")
        print("[     ]")
        print("[-----]")
    elif num == 3:
        print("[-----]")
        print("[O    ]")
        print("[  O  ]")
        print("[    O]")
        print("[-----]")
    elif num == 4:
        print("[-----]")
        print("[O   O]")
        print("[     ]")
        print("[O   O]")
        print("[-----]")
    elif num == 5:
        print("[-----]")
        print("[O   O]")
        print("[  O  ]")
        print("[O   O]")
        print("[-----]")
    elif num == 6:
        print("[-----]")
        print("[O   O]")
        print("[O   O]")
        print("[O   O]")
        print("[-----]")
    response = input("Do you want to roll another dice? (Answer Y/N): ")