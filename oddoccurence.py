def solution(arr):
   return reduce(lambda x,y: x^y, arr) #a^b^c^a^d^c^b = a^a^b^b^c^c^d # bit xor
def main():
    testcases = [[3,4,7,4,9,9,3]]
    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()