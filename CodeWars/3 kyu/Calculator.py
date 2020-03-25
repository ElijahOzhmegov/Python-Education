class Calculator(object):
    act_as_flt = {'+': float.__add__, '-': float.__sub__, '*': float.__mul__, '/': float.__truediv__}

    @staticmethod
    def primal_calculation(left: float, opr, right: float):
        result = Calculator.act_as_flt[opr](left, right)
        return result

    @staticmethod
    def purify_from_included_brackets(brackets: dict):
        brackets_list = sorted(list(brackets.items()))
        opening = [kv[0] for kv in brackets_list]
        closing = [kv[1] for kv in brackets_list]

        closed = closing[0]
        pure = brackets.copy()

        for i, key in enumerate(opening[1:]):
            if key < closed:
                pure.pop(key)
            else:
                closed = closing[i+1]

        return pure

    @staticmethod
    def extract_brackets_expression(string: str):
        istart = []
        d = {}
        for i, c in enumerate(string):
            if c == '(':
                istart.append(i)
            if c == ')':
                try:
                    d[istart.pop()] = i
                except IndexError:
                    print('Too many closing brackets!')
                    return None

        if istart:
            print('Too many opening brackets!')
            return None

        return d

    @staticmethod
    def find_next_operation(string: list, find_high):
        high = ('*', '/')
        low = ('+', '-')
        op = high if find_high else low
        try:
            mul = string.index(op[0])
        except ValueError:
            mul = None

        try:
            div = string.index(op[1])
        except ValueError:
            div = None

        if mul and div:
            return mul if mul < div else div
        if mul:
            return mul
        if div:
            return div
        return None

    @staticmethod
    def perform_operations(string: list, high_priority=True):
        string_ = string

        while True:
            ii = Calculator.find_next_operation(string_, high_priority)
            if ii is None: break

            left, oper, right = string_[ii-1:ii+2]
            string_.remove(left)
            string_.remove(oper)
            string_.remove(right)

            local_result = Calculator.primal_calculation(float(left), oper, float(right))
            string_.insert(ii - 1, str(local_result))

        return string_

    @staticmethod
    def evaluate(string: str):
        string_ = string

        brackets_dict = Calculator.extract_brackets_expression(string)
        if brackets_dict:
            for it in sorted(brackets_dict, reverse=True):
                left, right = it, brackets_dict[it]
                value_in_brackets = Calculator.evaluate(string[left + 1:right])
                string_ = string[:left] + str(value_in_brackets) + string[right + 1:]

        numbers_and_operations = string_.split(' ')
        numbers_and_operations = Calculator.perform_operations(numbers_and_operations)
        numbers_and_operations = Calculator.perform_operations(numbers_and_operations, high_priority=False)

        if len(numbers_and_operations) == 1:
            return float(numbers_and_operations[0])
        return numbers_and_operations


