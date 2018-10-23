from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1

class Contribute(Page):
    """Player: Choose how much to contribute"""


    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "请等待其他成员完成以继续"


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return {
            'total_earnings': self.group.total_contribution * Constants.multiplier,
        }

class Information(Page):
    """player's information"""
    form_model = 'player'
    form_fields = ['name', 'number']
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
    Introduction,
    Information,
    Contribute,
    ResultsWaitPage,
    Results
]
