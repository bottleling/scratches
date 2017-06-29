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


def findProfession(level, pos):
    if level == 1:
        return "Engineer"
    x = (pos+1)//2
    p = findProfession(level-1, x)
    if p == "Doctor":
        return "Doctor" if pos%2 == 1 else "Engineer" #if it's the first child (indexed starting from 1), it takes the parent's profession

    return "Engineer" if pos%2 == 1 else "Doctor"


def main():
    print(findProfession(8,100))

if __name__ == '__main__':
    main()

