from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.translation import ugettext


class Demographic(Page):
    form_model = "player"
    form_fields = ["age", "gender", "student", "student_level",
                   "student_discipline", "sport", "experience"]

    def error_message(self, values):
        if values["student"] and (values["student_level"] is None or
        values["student_discipline"] is None):
            return ugettext("If you are a student you must select "
                           "your level of study and the displine "
                           "you are studying")


class End(Page):
    pass


page_sequence = [Demographic, End]
