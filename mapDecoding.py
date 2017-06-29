def mapDecoding(message):
    message = message.rstrip("0")
    if len(message) <=1:
        return len(message)
    ways = [0 for i in range(len(message))]
    ways[0] = 1 # you could decode the first digit only one way

    if int(message[0:2]) > 26:
        ways[1] = 1 if message[1] != "0" else 0 #this digit at position 1 is >2. It won't be used as a double digit.
    else:
        ways[1] = 2 if message[1] != "0" else 0 # this digit at position 1 will probably used twice. we exclude 10 and 20 because we'll count them in the for loop

    for i in range(2, len(ways)):
        if message[i] != "0": #we're not sure whether this is a valid 2 digit player yet, if it were '01-09' then it wouldnt be valid
            ways[i] += ways[i-1] #you could form all the ways that you previously formed, that were one digit fewer in length

        #check whether this digit is a valid 2 digit player
        if 10 <= int(message[i-1:i+1]) <= 26:
            ways[i] += ways[i-2] # you could append these two digits to all the permutations of strings that were two digits fewer in length
    return ways[len(message)-1]



import unittest
class DoTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(mapDecoding(""), 0)
    def test_continuous(self):
        self.assertEqual(mapDecoding("123"), 3)
    def test_invalid(self):
        self.assertEqual(mapDecoding("301"), 0)
if __name__ == "__main__":
    unittest.main()

