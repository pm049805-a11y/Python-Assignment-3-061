s = input("Enter a string: ")

for ch in s:
    if s.index(ch) == s.rfind(ch):
        print(ch, "=", s.count(ch))
