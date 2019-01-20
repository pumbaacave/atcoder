
s = int(input())
temp = []
temp.append(s)
former = s
idx = 1

while True:
    idx += 1
    later = former / 2 if former % 2 == 0 else former * 3 + 1

    if later in temp:
        print(idx)
        break
    temp.append(later)
    former = later

