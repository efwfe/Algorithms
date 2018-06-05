# _*_coding:utf-8_*_
"""
现有不限数量的面额分别为1元，2元，5元，10元的货币，如果要用这些货币组合成x元，
求一共有多少种组合方式？请说出这类问题在算法中被称为什么问题并用代码实现
"""


coins = [1, 2, 5, 10]

array = []


def solution_digui(price, result):
    if price < 1:
        return result
    if price == 1:
        array.append(result + [1])

        return result + [1]
    if price == 2:
        result = result + [1]
        solution_digui(price - 1, result)
        array.append(result + [2])

        return result + [2]
    if price == 5:
        result = result + [1]
        solution_digui(price - 1, result)
        result = result + [2]
        solution_digui(price - 2, result)
        array.append(result + [5])

        return result + [5]
    if price == 10:
        result = result + [1]
        solution_digui(price - 1, result)
        result = result + [2]
        solution_digui(price - 2, result)
        result = result + [5]
        solution_digui(price - 5, result)
        array.append(result + [10])

        return result + [10]

    solution_digui(price-1,result+[1])
    solution_digui(price-2,result+[2])
    solution_digui(price-5,result+[5])
    solution_digui(price-10,result+[10])

solution_digui(10, [])
print(array)