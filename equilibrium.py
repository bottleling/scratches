def solution(arr):
    if len(arr) ==0:
        return -1
    if len(arr) == 1:
        return 0
    s = sum(arr)
    sleft = 0
    for i in range(len(arr)):
        sright = s - sleft - arr[i]
        if sleft == sright:
            return i
        sleft += arr[i]
    return -1

def main():
    testcases = [[-1,3,-4,5,1,-6,2,1]]
    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()