
def findChampion(n: int, edges: list[list[int]]) -> int:
    """
    Find the champin in massive
    This is my solution
    """
    champions = set()
    loosers = set()
    if n == 1:
        return 0

    for i in edges:
        champions.add(i[0])
        loosers.add(i[1])

    test_len = champions | loosers
    if int(len(test_len)) < int(n):
        return -1
    champions1 = champions.difference(loosers)

    return next(iter(champions1), None) if len(champions1) == 1 else -1


def best_findChampion(n: int, edges: list[list[int]]) -> int:
        """
        The best solution on LeetCode
        """
        m = [0] * n
        for from_node, to_node in edges:
            m[to_node] += 1

        return m.index(0) if m.count(0) == 1 else -1


def test_findChampion() -> int:

    n1 = 3
    edges1 = [[0,1],[1,2]]
    if findChampion(n1, edges1) == 0:
        print("TEST 1 PASS")
    else:
        print("TEST 1 FAIL")
    
    n2 = 4
    edges2 = [[0,2],[1,3],[1,2]]
    if findChampion(n2, edges2) == -1:
        print("TEST 2 PASS")
    else:
        print("TEST 2 FAIL")

    n3 = 1
    edges3 = []
    if findChampion(n3, edges3) == 0:
        print("TEST 3 PASS")
    else:
        print("TEST 3 FAIL")

    n4 = 3
    edges4 = [[0, 1]]
    if findChampion(n4, edges4) == -1:
        print("TEST 4 PASS")
    else:
        print("TEST 4 FAIL")
    
    n5 = 4
    edges5 = [[0, 1], [2, 0], [2, 1]]
    if findChampion(n5, edges5) == -1:
        print("TEST 5 PASS")
    else:
        print("TEST 5 FAIL")

test_findChampion()