import math

def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if a == 0.0 and b != 0.0:
        if -c / b >= 0.0:
            root = math.sqrt(-c/b)
            if root != 0.0:
                result.append(-root)
                result.append(root)
            else:
                result.append(abs(root))
    elif a == 0.0 and b == 0.0:
        if c == 0.0:
            print('Бесконечное множество корней')
            exit(1)
        else:
            print('Нет корней')
            exit(1)
    elif D == 0.0:
        if -b / (2.0 * a) > 0.0:
            root = math.sqrt(-b / (2.0 * a))
            if root != 0.0:
                result.append(root)
                result.append(-root)
            else:
                result.append(abs(root))
    elif D > 0.0:
        if (-b + math.sqrt(D)) / (2.0 * a) > 0.0:
            root1 = math.sqrt((-b + math.sqrt(D)) / (2.0 * a))
            if root1 != 0.0:
                result.append(root1)
                result.append(-root1)
            else:
                result.append(abs(root1))
        if (-b - math.sqrt(D)) / (2.0 * a) > 0.0:
            root2 = math.sqrt((-b - math.sqrt(D)) / (2.0 * a))
            if root2 != 0.0:
                result.append(root2)
                result.append(-root2)
            else:
                result.append(abs(root2))
    return result
