class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax1 - ax2) * (ay1 - ay2)
        area_b = (bx1 - bx2) * (by1 - by2)

        left = max(ax1, bx1)
        right = min(ax2, bx2)
        bottom = max(ay1, by1)
        top = min(ay2, by2)

        overlap_h = max(0, top - bottom)
        overlap_w = max(0, right - left)
        return area_a + area_b - (overlap_h * overlap_w)