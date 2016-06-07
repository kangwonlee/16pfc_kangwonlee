# -*- coding: utf8 -*-
balance_won = 0 # 현금카드 잔고


# 현금 카드로 할 수 있는 것: 입금, 춞금, 잔고 확인

def deposit(amount_won):
    """
    Deposit some amout of mony into cash card
    :param amount_won:
    :return:
    """
    # deposit 함수 안의 balance_won 이
    # 전역변수임을 표시
    global balance_won

    # 입금하면 잔고가 증가한다
    balance_won += amount_won
