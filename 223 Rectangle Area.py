class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areas = abs((ax1 - ax2) * (ay1 - ay2)) + abs((bx1 - bx2) * (by1 - by2))
        if not (ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1):
            return areas
        return areas - (abs(max(ax1, bx1) - min(ax2, bx2)) * abs(max(ay1, by1) - min(ay2, by2)))