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
