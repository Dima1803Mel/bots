import re

class CardCheck:
    @staticmethod
    def check_card_number(number):
        if re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$",number):
            return True
        else:
            return False

    @staticmethod
    def check_name(name):
        if re.match(r'^[A-Z]+\s[A-Z]+$',name):
            return True
        else:
            return False
