from typing import List

def read_integers() -> List[int]:
    l = input()
    s = l.split(",")
    i = []

    for w in s:
        i.append(int(w))
    
    return i

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
