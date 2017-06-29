
def solution1(arr): #fails
    cnt = arr[0]
    s = True
    prev = cnt
    for i in range(1,len(arr)):
        if arr[i] < 0  and arr[i] + cnt < 0 :
            prev = max(prev, cnt)
            cnt = arr[i]
        else:
            cnt += arr[i]
    return max(prev,cnt)

def solution(arr):
    maximum = 0
    sofar = 0
    m = max(arr)
    if m < 0:
        return m

    #at position i, if sum(A[i-j:i]) + A[i]  < 0, we don't add A[i]
    for a in arr:
        sofar = max (0, sofar + a)
        maximum = max(sofar, maximum)

    return maximum





def main():
    testcases = [[-10,100,-5,200], [3,2,-6,4,0],[0,0],[0,-1],[0,1],[10,-5,-6],[1,2,2]]
    expected = [295,5,0,0,1,10,5]
    for i in range(len(testcases)):
        tc = testcases[i]
        sol = solution(tc)
        print("result:", tc, sol, sol == expected[i])

if __name__ == '__main__':
    main()
    
