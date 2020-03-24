class Rectangle:
    @staticmethod
    def decompose(lngth, wdth):
        if lngth == wdth:
            return [lngth], [None]

        rects_ = [f"({lngth}*{wdth})"]

        squares_ = [wdth]
        new_lngth = lngth - wdth
        dim = (new_lngth, wdth) if new_lngth > wdth else (wdth, new_lngth)

        squares, rects = Rectangle.decompose(*dim)
        squares_.extend(squares)
        rects_.extend(rects)

        return squares_, rects_

    @staticmethod
    def rect_into_rects(lngth, wdth):
        #Put your code here.
        if lngth == wdth:
            return [lngth], [None]
        lngth, wdth = (lngth, wdth) if lngth > wdth else (wdth, lngth)

        squares, rects = Rectangle.decompose(lngth, wdth)

        rects.pop()
        squares.pop()
        squares_occurrence = [(square, squares.count(square)) for square in set(squares) if squares.count(square) > 1]

        for square_occurrence in squares_occurrence:
            for number_occurrence in range(square_occurrence[1], 1, -1):
                repeat_times = square_occurrence[1] - number_occurrence + 1
                repeated_occurrence = [f"({square_occurrence[0]*number_occurrence}*{square_occurrence[0]})"]
                rects.extend(repeated_occurrence*repeat_times)
        return rects


def finish_test():
    def test13x5():
        sol = ["(10*5)", "(13*5)", "(8*5)", "(5*3)", "(3*2)", "(2*1)"]
        ans = Rectangle.rect_into_rects(13, 5)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test22x6():
        sol = ["(12*6)", "(18*6)", "(22*6)", "(12*6)", "(16*6)", "(10*6)", "(6*4)", "(4*2)"]
        ans = Rectangle.rect_into_rects(22, 6)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test8x5():
        sol = ["(8*5)", "(5*3)", "(3*2)", "(2*1)"]
        ans = Rectangle.rect_into_rects(8, 5)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test20x8():
        sol = ["(16*8)", "(20*8)", "(12*8)", "(8*4)"]
        ans = Rectangle.rect_into_rects(20, 8)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test4x3():
        sol = ["(4*3)", "(2*1)", "(3*1)", "(2*1)"]
        ans = Rectangle.rect_into_rects(4, 3)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test7x5():
        sol = ["(7*5)", "(4*2)", "(5*2)", "(3*2)", "(2*1)"]
        ans = Rectangle.rect_into_rects(7, 5)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test6x4():
        sol = ["(6*4)", "(4*2)"]
        ans = Rectangle.rect_into_rects(6, 4)
        sol.sort()
        ans.sort()
        assert ans == sol

    def test15x4():
        sol = ["(8*4)", "(12*4)", "(15*4)", "(8*4)", "(11*4)", "(7*4)", "(4*3)", "(2*1)", "(3*1)", "(2*1)"]
        ans = Rectangle.rect_into_rects(15, 4)
        sol.sort()
        ans.sort()
        assert ans == sol

    test13x5()
    test22x6()
    test8x5()
    test20x8()
    test4x3()
    test7x5()
    test6x4()
    test15x4()


def test_rect_decompose(sides, sol):
    squares, rects = Rectangle.decompose(*sides)
    # print(rects)
    assert squares == sol


if __name__ == '__main__':
    test_rect_decompose((13, 5), [5, 5, 3, 2, 1, 1])
    test_rect_decompose((22, 6), [6, 6, 6, 4, 2, 2])
    test_rect_decompose((20, 8), [8, 8, 4, 4])

    Rectangle.rect_into_rects(13, 5)
    Rectangle.rect_into_rects(22, 6)

    finish_test()



