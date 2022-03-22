X_REPEAT=30
Y_REPREAT=1000

for y in range(Y_REPREAT):
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()