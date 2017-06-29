def solution(arr):
    if len(arr) == 1:
        return abs(2*arr[0])
    arr = sorted(arr)
    if arr[-1] <=0:
        return abs(2*arr[-1])
    elif arr[0] >=0:
        return abs(2*arr[0])

    forward = 0
    backward = len(arr)-1
    minimum = 2*1000000000+1
    while forward  <= backward:
        s = arr[forward] + arr[backward]
        minimum = min(minimum, abs(s))
        if minimum ==0:
            return 0
        if s < 0: #s is negative meaning forward is too negative
            forward += 1
        elif s > 0: # s is positive meaning backward is too positive
            backward -= 1
    return minimum

def main():
    testcases = [[-1,3,-4,5,1,-6,2,1]]
    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()