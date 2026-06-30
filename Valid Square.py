class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def get_dist_sq(pa, pb):
 
            return (pa[0] - pb[0])**2 + (pa[1] - pb[1])**2
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(get_dist_sq(points[i], points[j]))
        dist_set = set(distances)
        return len(dist_set) == 2 and 0 not in dist_set
    
