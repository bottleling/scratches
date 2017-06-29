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

## Non-recursive
def isTreeSymmetric_nonrec(t):
    if t == None:
        return True
    storage = []
    storage.append((t.left, t.right))
    while storage:
        a, b = storage.pop()

        if (a == None and b != None) or (a != None and b == None):
            return False
        if not (a == None and b == None):
            if a.value != b.value:
                return False
            storage.append((a.left, b.right))
            storage.append((a.right, b.left))

    return True

def isLeaf(a):
    return a.left is None and a.right is None

def isTreeSymmetric(t):
    if isLeaf(t):
        return True
    return isMirror(t.left, t.right)

def isMirror(a,b):
    if a is None and b is None:
        return True
    elif (a is None) != (b is None)  :
        return False
    if a.value != b.value:
        return False
    return isMirror(a.left, b.right) and isMirror(a.right, b.left)

def main():

    d1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
    }

    d2 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

    d3 =  {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
    # test1 = buildtree(d1)
    # print(isTreeSymmetric(test1))
    test2 = buildtree(d2)
    print(isTreeSymmetric(test2))
    test3 = buildtree(d3)
    print(isTreeSymmetric(test3))
if __name__ == '__main__':
    main()



