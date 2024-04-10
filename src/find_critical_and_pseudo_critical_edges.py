class FindCriticalAndPseudoCriticalEdges:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        # do normal MST algorithm

        # first occurence of connecting a new node -> add to critical edges

        # second occurence of connecting a node with same weight -> move from critical edge to pseudo-critical edges
