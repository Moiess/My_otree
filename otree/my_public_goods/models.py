from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'No name'

doc = """
这是一个公共物品博弈的小实验，你将在游戏开始时获得100点初始资金。
通过每回合贡献一定量的资金进入公共部分，所有人都可以在回合结束时
获得一定的收益，其数值等于(所有人的总贡献 * 2 / 人数)。通过总共
10回合的游戏，努力赚取更多的资金吧！
"""


class Constants(BaseConstants):
    name_in_url = '公共物品博弈'
    players_per_group = 3
    num_rounds = 10

    endowment = c(100)
    multiplier = 2

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    print('defined fields on the Group')


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
