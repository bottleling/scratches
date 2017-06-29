

# def solution(M, A):
#     cnt = 0
#     sofar = 0
#     prev = A[0]
#     for a in A:
#         if a != prev:
#             prev = a
#             sofar +=1
#         else:
#             cnt += (sofar + 1)*sofar/2
#             sofar = 0
#     cnt += (sofar + 1) * sofar / 2
#     res = min( cnt + len(A) ,1000000000)
#     return res
def count_distinct_slices(M, A):
    N = len(A)
    last = 0
    result = 0
    s = [-1] * (M + 1)

    for i, a in enumerate(A):
        if s[a] >= last:
            result += (i - last) * (i - last + 1) / 2
            last = s[a] + 1
            result -= (i - last) * (i - last + 1) / 2
            if result > 1e9:
                return int(1e9)

        s[a] = i

    result += (N - last) * (N - last + 1) / 2
    if result > 1e9:
        return int(1e9)
    return result

def solution(M, A):
    cnt = 0
    sofar = [-1]*(M+1) #stores the index of the last time we saw an integer M and below
    start = 0 #the  beginning of our interval
    for i in range(len(A)):
        val = A[i]
        if sofar[val] >= start:
            n = i - start #number of elements in our interval
            cnt +=   (n+1) * n/2 #number of combinations for that interval
            start =  sofar[val] +1
            n = i - start
            cnt -=   (n+1) * n/2
        sofar[val] = i #we saw val at this position

    n = len(A)-start #this runs if the last number in the array isn't a duplicate
    cnt+= (n+1) * n/2
    return min( cnt ,1000000000)

def main():
    testcases = [ (6,[3,4,5,5,2]),(4,[1,2,3]),(5,[0,0,1,3,4,5,0]) ]
    expected = [9, 6, 21]
    #for i in range(len(testcases)):
    i=2
    tc = testcases[i]
    sol = solution(tc[0],tc[1])
    print("result:", tc, sol, sol == expected[i])

if __name__ == '__main__':
    main()
    
