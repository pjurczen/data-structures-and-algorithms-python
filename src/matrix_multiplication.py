import numpy as np


class MatrixMultiplication:

    def multiply(self, x, y):
        n = len(x)
        if n == 1:
            return x * y
        half_n = int(n/2)
        a = x[0:half_n, 0:half_n]
        b = x[0:half_n, half_n:n]
        c = x[half_n:n, 0:half_n]
        d = x[half_n:n, half_n:n]

        e = y[0:half_n, 0:half_n]
        f = y[0:half_n, half_n:n]
        g = y[half_n:n, 0:half_n]
        h = y[half_n:n, half_n:n]

        p1 = self.multiply(a, f - h)
        p2 = self.multiply(a + b, h)
        p3 = self.multiply(c + d, e)
        p4 = self.multiply(d, g - e)
        p5 = self.multiply(a + d, e + h)
        p6 = self.multiply(b - d, g + h)
        p7 = self.multiply(a - c, e + f)

        left_upper = p5 + p4 - p2 + p6
        right_upper = p1 + p2
        horizontal_upper = np.hstack((left_upper, right_upper))
        left_lower = p3 + p4
        right_lower = p1 + p5 - p3 - p7
        horizontal_lower = np.hstack((left_lower, right_lower))

        return np.vstack((horizontal_upper, horizontal_lower))
