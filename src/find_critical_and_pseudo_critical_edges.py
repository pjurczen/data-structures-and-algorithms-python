class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]
        return v

    def union(self, v1, v2) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class FindCriticalAndPseudoCriticalEdges:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        for i, e in enumerate(edges):
            e.append(i)
        # a, b, w, i
        edges.sort(key=lambda x: x[2])
        mst_cost = 0
        uf = UnionFind(n)
        for a, b, w, i in edges:
            if uf.union(a, b):
                mst_cost += w
        critical, pseudo = [], []
        for a1, b1, w1, i1 in edges:
            uf = UnionFind(n)
            curr_cost = 0
            for a2, b2, w2, i2 in edges:
                if i1 != i2 and uf.union(a2, b2):
                    curr_cost += w2
            if max(uf.rank) != n or curr_cost > mst_cost:
                critical.append(i1)
                continue
            uf = UnionFind(n)
            uf.union(a1, b1)
            curr_cost = w1
            for a3, b3, w3, i3 in edges:
                if uf.union(a3, b3):
                    curr_cost += w3
            if curr_cost == mst_cost:
                pseudo.append(i1)

        return [critical, pseudo]
