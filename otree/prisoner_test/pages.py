from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    timeout_seconds = 100
    timer_text = '将在以下时间后自动继续下一页'
    def is_displayed(self):
        return self.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = 100
    timer_text = '请在剩余时间内完成选择，若未选择视为选择合作'
    def before_next_page(self):
        if self.timeout_happened:
            me = self.player
            me.decision = '合作'

class ResultsWaitPage(WaitPage):
    template_name = 'prisoner_test/WaitPage.html'
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
    body_text = '另一位参与者正在选择……'
    title_text = '请稍等'

class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
        }
    timeout_seconds = 30
    timer_text = '将在以下时间后自动继续下一回合'

class Information(Page):
    '''player's information'''
    form_model = 'player'
    form_fields = ['name', 'number']
    def is_displayed(self):
        return self.round_number == 1

# class regroup_WaitPage(WaitPage): #未实现
#     template_name = 'regroup_WaitPage'
#     group_by_arrival_time = True
#     wait_for_all_groups = True
#     title_text = '即将重新分组'
#     body_text = '你将一位参与者分为一组'


page_sequence = [
    Introduction,
    Information,
    Decision,
    ResultsWaitPage,
    Results,
    # regroup_WaitPage
]
