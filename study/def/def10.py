def outer2(tax):
    """

    :param tax:
    :return:
    """
    def inner2(su, dan):
        """

        :param su:
        :param dan:
        :return:
        """
        amount = su * dan * tax
        return amount
    return inner2 # outer2는 inner2 함수의 주소를 반환, 클로저!

# 1분기에는 수량 * 단가에 tax를 0.1 부과
q1 = outer2(0.1)
print('result1 : ', q1(5, 10000))
print('result2 : ', q1(10, 20000))

# 2분기에는 수량*단가에 tax 0.5
q2 = outer2(0.05)
print('result3 : ', q2(5, 10000))
print('result4 : ', q2(10, 20000))

