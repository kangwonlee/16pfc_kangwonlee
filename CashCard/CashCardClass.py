# -*- coding: utf8 -*-
# http://eclass.kpu.ac.kr/ilos/pf/course/lecture_material_view_form.acl?ARTL_NUM=376324&SCH_KEY=&SCH_VALUE=&display=10&start=1


class SimpleCashCard:
    """
    SimpleCashCard class
    deposit, withdraw, and check_balance methods
    """

    def __init__(self):
        print("SimpleCashCard __init__()")  # 함수 호출 표식
        # 클래스 생성자 (컨스트럭터)
        # 멤버 변수 초기화
        # 각 카드 별로 따로 잔고를 기록한다
        self.balance_won = 0

    # 메소드 methods :
    # 객체에 전달된 어떤 신호에 응답하는 역할을 한다
    def deposit(self, amount_won):
        """
        입금
        :param amount_won: 입금 액수
        :return:
        """
        print("SimpleCashCard deposit()")  # 함수 호출 표식
        # 입금하면 잔고가 증가한다
        self.balance_won += amount_won
