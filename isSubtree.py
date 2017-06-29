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

def isIdentical(t,s):
    if t is None and s is None:
        return True
    if (t is None) != (s is None):
        return False
    return (t.value == s.value) and isIdentical(t.left, s.left) and isIdentical(t.right, s.right)

def isSubtree(t,s):
    x,y,z = False, False, False
    x = isIdentical(t, s)
    if t and not x:
        if not s and (not t.left or not t.right):
            return True
        if t.left:
            y = isSubtree(t.left, s)
        if t.right:
            z = isSubtree(t.right, s)
        return x or y or z
    return x


import unittest
class DoTests(unittest.TestCase):
    def test_trees(self):
        t1 = {
            "value": 5,
            "left": {
                "value": 10,
                "left": {
                    "value": 4,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                    },
                    "right": {
                        "value": 2,
                        "left": None,
                        "right": None
                    }
                },
                "right": {
                    "value": 6,
                    "left": None,
                    "right": {
                        "value": -1,
                        "left": None,
                        "right": None
                    }
                }
            },
            "right": {
                "value": 7,
                "left": None,
                "right": None
            }
        }
        s1 =  {
            "value": 10,
            "left": {
                "value": 4,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 2,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 6,
                "left": None,
                "right": {
                    "value": -1,
                    "left": None,
                    "right": None
                }
            }
        }
        t2 = {
            "value": 5,
            "left": {
                "value": 10,
                "left": {
                    "value": 4,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                    },
                    "right": {
                        "value": 2,
                        "left": None,
                        "right": None
                    }
                },
                "right": {
                    "value": 6,
                    "left": {
                        "value": -1,
                        "left": None,
                        "right": None
                    },
                    "right": None
                }
            },
            "right": {
                "value": 7,
                "left": None,
                "right": None
            }
        }
        s2 =  {
            "value": 10,
            "left": {
                "value": 4,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 2,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 6,
                "left": None,
                "right": {
                    "value": -1,
                    "left": None,
                    "right": None
                }
            }
        }
        t3 = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        }

        s3 = {
            "value": 2,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": None
            }
        self.assertTrue(isSubtree(buildtree(t1), buildtree(s1)))
        self.assertFalse(isSubtree(buildtree(t2), buildtree(s2)))
        self.assertFalse(isSubtree(buildtree(t3), buildtree(s3)))

if __name__ == "__main__":
    unittest.main()

