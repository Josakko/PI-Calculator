file = "pi100k.txt"
file_calced = "pi100kcalced.txt"

pi = open(file, "r").read()
pi_calced = open(file_calced, "r").read()

if pi == pi_calced:
    print("calculated pi is correct")

print(len(pi))
print(len(pi_calced))