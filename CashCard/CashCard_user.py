# -*- coding: utf8 -*-
# http://eclass.kpu.ac.kr/ilos/pf/course/lecture_material_view_form.acl?ARTL_NUM=376324&SCH_KEY=&SCH_VALUE=&display=10&start=1
# 현금카드 모듈을 불러들임
import CashCard as CashCard_module


def chk_bal(message, account):
    """
    Print message and value
    :param message:
    :param account:
    :return:
    """
    print("%s : %d" % (message, account.check_balance()))

# 아래의 내용은 이 .py 파일이 import 될 때는 실행되지 않음
if '__main__' == __name__:
    # 현금 카드 모듈의 잔액 확인
    chk_bal("CashCard_module 잔액확인", CashCard_module)
    # 현금 카드에 10000원 입금
    print("10000원 입금")

    # CashCard.py 모듈 안의 deposit() 함수를 호출
    # CashCard.py 모듈 안의 balance_won 값이 증가
    CashCard_module.deposit(10000)

    # CashCard.py 모듈 안의 check_balance() 함수를 호출
    #   CashCard.py 모듈 안의 balance_won 값을 반환
    chk_bal("입금 후 잔고 확인", CashCard_module)

    print("1000원 출금")
    # CashCard.py 모듈 안의 withdraw() 함수를 호출
    # CashCard.py 모듈 안의 balance_won 값이 감소
    CashCard_module.withdraw(1000)

    # CashCard.py 모듈 안의 check_balance() 함수를 호출
    #   CashCard.py 모듈 안의 balance_won 값을 반환
    chk_bal("출금 후 잔고 확인", CashCard_module)
