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
