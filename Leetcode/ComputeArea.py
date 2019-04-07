class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C -A) * (D -B) + (G-E)*(H-F)
        w, h = 0, 0
        if B > F:
            A,B,C,D,E,F,G,H = E,F,G,H,A,B,C,D
        if A <= E:
            if C < E:
                pass
            elif E <= C <= G:
                w = C - E
                if D < F:
                    pass
                elif F <= D <= H:
                    h = D - F
                elif H < D:
                    h = H - F
            elif C > G:
                w = G - E
                if D < F:
                    pass
                elif F <= D <= H:
                    h = D - F
                elif H < D:
                    h = H - F
        else:
            if G < A:
                pass
            elif A <= G <= C:
                w = G - A
                if D <= F:
                    pass
                elif F < D <= H:
                    h = D - F
                elif H < D:
                    h = H - F
            elif C < G:
                w = C - A
                if D < F:
                    pass
                elif F <= D <= H:
                    h = D - F
                elif H < D:
                    h = H - F
        print(total, w, h)
        return total - w * h
