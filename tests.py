from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random
from django.utils.translation import gettext


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Demographic,
               {
                   "age": random.randint(15, 90),
                   "gender": random.randint(0, 1),
                   "student": random.randint(0, 1),
                   "student_level": random.randint(0, 2),
                   "student_discipline": gettext("Economics"),
                   "sport": random.randint(0, 1),
                   "experience": random.randint(0, 1)
               })
        yield Submission(pages.End, check_html=False)
