def towerOfHanoi(n, source, destination, auxiliry):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination)
        return

    towerOfHanoi(n-1, source, auxiliry, destination)

    print("Move disk", n, "from source ", source, " to destination ", destination)
    towerOfHanoi(n-1, auxiliry, destination,source)

n = 4
towerOfHanoi(n,"A","B","C")
