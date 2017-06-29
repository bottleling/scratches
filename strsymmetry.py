import math
def solution(S):
    if len(S)%2 ==0 : #takes care of empty string and even length
        return -1
    if len(S) == 1:
        return 0
    n=int(len(S)/2)
    for i in range(n):
        print( S[i],S[-(i+1)])
        if S[i] != S[-(i+1)]:
            return -1

    return n
def main():
    testcases = ["racecar","level","none","rubber","nunel","ror", "", "raar"]

    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()