class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def buildtree(treedict):
    if treedict is None:
        return None
    keys = treedict.keys()
    tree = Tree(treedict["value"])
    tree.left = None
    tree.right = None
    if "left" in keys:
        tree.left = buildtree(treedict["left"])
    if "right" in keys:
        tree.right = buildtree(treedict["right"])
    return tree


def hasPathWithGivenSum(t, s):

    print(traverse(t,s))

def isLeaf(t):
    return t.left is None and t.right is None
def traverse(t, rem):
    if t is not None:
        x = rem - t.value
        if x == 0 and isLeaf(t):
            return True
        a = traverse(t.left, x)
        b = traverse(t.right, x)
        return a or b
    else:
        return rem ==0




def getSum(t):
    sleft = 0
    sright = 0
    if not t.left is None:
        sleft = getSum(t.left)
    if not t.right is None:
        sright = getSum(t.right)
    print ("t.value %d sleft %d sright %d" % (t.value, sleft, sright) )
    return t.value + sleft + sright

def main():

    d1= {
        "value": 4,
        "left": {
            "value": 1,
            "left": {
                "value": -2,
                "left": None
                ,
                "right": {
                    "value": 3,
                    "left": None
                    ,
                    "right": None

                }
            },
            "right": None

        },
        "right": {
            "value": 3,
            "left": {
                "value": 1,
                "left": None
                ,
                "right": None

            },
            "right": {
                "value": 2,
                "left": {
                    "value": -2,
                    "left": None
                    ,
                    "right": None

                },
                "right": {
                    "value": -3,
                    "left": None
                    ,
                    "right": None

                }
            }
        }
    }

    test1 = buildtree(d1)
    hasPathWithGivenSum(test1, 7)
if __name__ == '__main__':
    main()
