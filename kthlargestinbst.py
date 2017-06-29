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

def inorder(t, count):
    if t.left is not None:
        left, count = inorder(t.left, count)
        if count == 0:
            return (left, 0)
    count = count - 1
    if count == 0:
        return (t.value, 0)
    if t.right is not None:
        right, count = inorder(t.right, count)
        if count == 0:
            return (right, 0)
    return (t.value, count)


def kthLargestInBST(t, k):
    if t is None:
        return 0
    return inorder(t, k)[0]




def testTrees():

    return (
    [( {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 5,
            "left": {
                "value": 4,
                "left": None,
                "right": None
            },
            "right": {
                "value": 6,
                "left": None,
                "right": None
            }
        }
    }, 3),
        ({
        "value": 1,
        "left": {
            "value": -1,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": 0,
                "left": None,
                "right": None
            }
        },
        "right": None
    },1),
        ({
        "value": 100,
        "left": None,
        "right": None
    },1),
        ({
        "value": 1,
        "left": {
            "value": 0,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },3)
    ])
def main():
    for t,k in testTrees()[1:]:
        tree = buildtree(t)
        print(kthLargestInBST(tree, k))


if __name__ == '__main__':
    main()

