import pprint

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[x:" + str(self.x) + ", y:" + str(self.y) + "]"

    def __unicode__(self):
        return "[x:" + str(self.x) + ", y:" + str(self.y) + "]"

    def __repr__(self):
        return "[x:" + str(self.x) + ", y:" + str(self.y) + "]"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class ClosestPair:
    def find_closest_pair(self, points: []) -> (Point, Point):
        points_array = np.array(points)
        p_x = points_array[np.argsort([point.x for point in points_array], kind='mergesort')]
        p_y = points_array[np.argsort([point.y for point in points_array], kind='mergesort')]
        return self.closest_pair(p_x, p_y)

    def closest_pair(self, p_x: [], p_y: []) -> (Point, Point):
        if len(p_x) + len(p_y) <= 3:
            return self.brute_force(p_x, p_y)
        half_size = int(len(p_x)/2)
        q_x = p_x[0:half_size]
        q_y = p_y[0:half_size]
        r_x = p_x[half_size:-1]
        r_y = p_y[half_size:-1]
        left_pair = self.closest_pair(q_x, q_y)
        right_pair = self.closest_pair(r_x, r_y)
        delta = np.min([self.distance(left_pair), self.distance(right_pair)])
        split_pair = self.closest_split_pair(p_x, p_y, delta)
        pair_arg = np.argmin([self.distance(left_pair), self.distance(right_pair), self.distance(split_pair)])
        return [left_pair, right_pair, split_pair][pair_arg]

    def closest_split_pair(self, p_x: [], p_y: [], delta):
        x_bar = p_x[-1].x
        s_y = np.array([point for point in p_y if x_bar - delta <= point.x <= x_bar + delta])
        best = delta
        best_pair = None
        for i in range(1, len(s_y) - 1):
            for j in range(1, min(7, len(s_y) - i)):
                p = s_y[i]
                q = s_y[i+j]
                if self.distance((p, q)) < best:
                    best_pair = (p, q)
        return best_pair

    def brute_force(self, p_x: [], p_y: []) -> (Point, Point):
        min_dist = float("inf")
        best_pair = None
        for i in range(len(p_x)):
            for j in range(i + 1, len(p_y)):
                if self.dist((p_x[i], p_y[j])) < min_dist:
                    best_pair = p_x[i], p_y[j]
        return best_pair

    def distance(self, pair: (Point, Point)):
        if pair is None:
            return float("inf")
        point1, point2 = pair
        return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**(1/2)


