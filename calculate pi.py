import random


def get_pi(n: int) -> float:
    """
    :param n: number of points
    :return: pi
    """
    points_inside = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # print(radii, ' ', end='')
        if (x ** 2 + y ** 2) <= 1:
            points_inside += 1

    return 4*points_inside / n


if __name__ == '__main__':
    print(get_pi(100))
    print(get_pi(1000))
    print(get_pi(10000))
    print(get_pi(100000))
