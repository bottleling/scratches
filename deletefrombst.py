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
def builddict(tree):
    if tree is None:
        return None
    d = dict()
    d["value"] = tree.value
    d["left"] = builddict(tree.left)
    d["right"] = builddict(tree.right)
    return d


def maxValue(tree):
    if tree.right:
        r = maxValue(tree.right)
        return r
    return tree.value

def deleteFromBST_Singly(subtree, q):
    if not subtree:
        return None
    if q > subtree.value:
        subtree.right = deleteFromBST_Singly(subtree.right,q)
    elif q < subtree.value:
        subtree.left = deleteFromBST_Singly(subtree.left, q)
    else:
        if subtree.left:
            p = maxValue(subtree.left)
            subtree.value = p
            subtree.left = deleteFromBST_Singly(subtree.left, p)
        elif subtree.right:
            subtree.value = subtree.right.value
            subtree.left = subtree.right.left
            subtree.right = subtree.right.right
        else:
            return None
    return subtree

def deleteFromBST(t, queries):
    if not t:
        return None
    for q in queries:
        t = deleteFromBST_Singly(t, q)
    return t




import unittest
class DoTests(unittest.TestCase):
    def test_trees(self):
        t1 = {
            "value": 5,
            "left": {
                "value": 2,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 3,
                    "left": None,
                    "right": {"value": 4, "left":None, "right":None}
                }
            },
            "right": {
                "value": 6,
                "left": None,
                "right": {
                    "value": 8,
                    "left": {
                        "value": 7,
                        "left": None,
                        "right": None
                    },
                    "right": None
                }
            }
        }
        s1 = {
        "value": 3,
        "left": {
            "value": 2,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": None
        },
        "right": {
            "value": 8,
            "left": {
                "value": 7,
                "left": None,
                "right": None
            },
            "right": None
        }
    }
        self.assertDictEqual(builddict( deleteFromBST(buildtree(t1), [3]) ) , s1)
if __name__ == "__main__":
    unittest.main()

