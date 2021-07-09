import math
def polysum(n, s):
    def areaPolygon(n, s):
        area = (0.25*n*s**2)/math.tan(math.pi/n)
        return area
    def perimeterPolygon(n, s):
        perimeter = s*n
        return perimeter
    sumPolygon = areaPolygon(n,s) + perimeterPolygon(n,s)
    return round(sumPolygon, 3)

