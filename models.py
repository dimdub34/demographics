from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.utils.translation import ugettext


author = 'Dimitri DUBOIS'

doc = """
A simple demographic questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        label=ugettext('What is your age?'),
        min=13, max=125)

    gender = models.IntegerField(
        choices=[(0, ugettext('Female')), (1, ugettext('Male'))],
        label=ugettext('What is your gender?'),
        widget=widgets.RadioSelectHorizontal)

    student = models.IntegerField(
        choices=[(0, ugettext('No')), (1, ugettext('Yes'))],
        label=ugettext("Are you a student?"),
        widget=widgets.RadioSelectHorizontal)

    student_level = models.IntegerField(
        choices=[(0, ugettext('Bachelor')), (1, ugettext('Master')),
                 (2, ugettext('PhD')), (3, ugettext('Not in the list'))],
        blank=True)

    student_discipline = models.StringField(
        choices=[
            ugettext("Administration"), ugettext("Archeology"), ugettext("Biology"),
            ugettext("Buisiness school"), ugettext("Chemistry"),
            ugettext("Computer science"), ugettext("Economics"),
            ugettext("Education"), ugettext("Law"), ugettext("Management"),
            ugettext("Nursing school"), ugettext("Engineer"), ugettext("Geography"),
            ugettext("History"), ugettext("Lettres"), ugettext("Mathematics"),
            ugettext("Medicine"), ugettext("Music"), ugettext("Pharmacy"),
            ugettext("Philosophy"), ugettext("Physics"), ugettext("Politics"),
            ugettext("Sociology"), ugettext("Sport"), ugettext("Not in the list")
        ],
        label=ugettext("What are you studying?"), blank=True)

    sport = models.IntegerField(
        choices=[(0, ugettext('No')), (1, ugettext('Yes'))],
        label=ugettext("Do you pratice (regularly) some sport?"),
        widget=widgets.RadioSelectHorizontal)

    experience = models.IntegerField(
        choices=[(0, ugettext('No')), (1, ugettext('Yes'))],
        label=ugettext("Have you ever participated in an experiment?"),
        widget=widgets.RadioSelectHorizontal)
