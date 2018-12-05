def run():
    with open('input5', 'r') as f:
        ret = []
        now = None
        pre = None
        L = 0
        while(1):
            now = f.read(1)  # unicode :: str type
            if now == '':
                # hits EOF
                break
            if L == 0:
                ret.append(now)
                L += 1
                continue
            pre = ret.pop()
            if abs(ord(pre) - ord(now)) == 32:
                L -= 1
                continue  # polarization destruct
            ret.append(pre)
            ret.append(now)
            L += 1

        print(len(ret))
        print(ret)


def countWithoutA(target):
    print(chr(target))
    z = chr(target)
    Z = chr(target - 32)

    with open('input5', 'r') as f:
        ret = []
        now = None
        pre = None
        L = 0
        while(1):
            now = f.read(1)  # unicode :: str type
            if now == z or now == Z:
                continue
            if now == '\n':
                # hits EOF
                break
            if L == 0:
                ret.append(now)
                L += 1
                continue
            pre = ret.pop()
            if abs(ord(pre) - ord(now)) == 32:
                L -= 1
                continue  # polarization destruct
            ret.append(pre)
            ret.append(now)
            L += 1

        print(ret)
        return L

def run1():
    start = 'a'
    report = [countWithoutA(target) for target in range(ord(start), ord(start)+26)]
    print(report)
    print(min(report))

run1()
