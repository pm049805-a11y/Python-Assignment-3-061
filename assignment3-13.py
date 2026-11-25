s = input("Enter a string: ")
ch = input("Enter character: ")

if s.startswith(ch) and s.endswith(ch):
    print("String starts and ends with", ch)
else:
    print("Condition not satisfied")
