from typing import Union

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    Currency)
from otree.currency import Currency

doc = """
用于2018-10-24班级实验的囚徒困境博弈
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_test'
    players_per_group = 2
    num_rounds = 100

    instructions_template = 'prisoner_test/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    decision = models.StringField(
        choices=['合作', '不合作'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix = {
            '合作':
                {
                    '合作': Constants.both_cooperate_payoff,
                    '不合作': Constants.betrayed_payoff
                },
            '不合作':
                {
                    '合作': Constants.betray_payoff,
                    '不合作': Constants.both_defect_payoff
                }
        }
        self.payoff = payoff_matrix[self.decision][self.other_player().decision]
        self.cumulative_payoff = sum([p.payoff for p in self.in_all_rounds()])
        # # 历史记录 未实现！！
        # self.history_list = []
        # history_information = []
        # history_information.append(self.round_number)
        # history_information.append(self.get_others_in_group())
        # history_information.append(self.decision)
        # history_information.append(self.other_player().decision)
        # self.history_list.append(history_information)
        #
        # for i in self.round_number:
        #     if self.history_list[i-1][0] is self.other_player():
        #         meet = True
        #
    # history_list = models.StringField()

    name = models.StringField(label='你的名字')
    number = models.IntegerField(label='你的学号')
    # 计算收益和
    cumulative_payoff = models.CurrencyField()


#












