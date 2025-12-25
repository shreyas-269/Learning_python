#Skips that particular iteration(that particular value of i.)

for i in range(5,105,5):
    if i==55:
        print("55 is a bad number, skipping it.")
        continue
    print(i)

