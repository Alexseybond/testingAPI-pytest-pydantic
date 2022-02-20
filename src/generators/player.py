from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        """
        :return:
        Врзвращаем экземпляр класса чтобы можно было поверх набросить еще сет и выходило так:
        если статус "активный" то делаем следующее, если "нет", то проверять смысла дальше нет.
        """
        self.result['account_status'] = status

        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance

        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.result['set_avatar'] = avatar

        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result['localize'] = {
                "en": PlayerLocalization('en_US').bild(),
                "ru": PlayerLocalization('ru_RU').bild()
        }

        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {"en": generator.bild()}

        return self

    def build(self):

        return self.result

