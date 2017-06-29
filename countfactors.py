def primeFactor(n):
    x = []
    while n % 2 == 0:
        n = n / 2
        x.append(2)

    if n != 3:
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                n = n / i
                x.append(i)
    else:
        x.append(3)
    return x

def solution(n):
    if n == 1:
        return 1

    cnt = 2 #for 1 and itself
    for i in range(2,  int(n ** 0.5) + 1):
        if n % i ==0:
            if i * i == n: #for squares like 4*4 = 16
                cnt +=1
            else:
                cnt +=2 #for the pair of x*y eg 2*12 = 24

    return cnt

def main():
    testcases = [24,16,9,1,2,3,5,8,99]
    expected = [8,5, 3, 1,2,2,2,4,6]
    for i in range(len(testcases)):
        tc = testcases[i]
        sol = solution(tc)
        print("result:", tc, sol, sol == expected[i])

if __name__ == '__main__':
    main()
    
