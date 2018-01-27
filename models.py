from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.utils.translation import gettext


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
        verbose_name=gettext('What is your age?'),
        min=13, max=125)

    gender = models.IntegerField(
        choices=[(0, gettext('Female')), (1, gettext('Male'))],
        verbose_name=gettext('What is your gender?'),
        widget=widgets.RadioSelectHorizontal)

    student = models.IntegerField(
        choices=[(0, gettext('No')), (1, gettext('Yes'))],
        verbose_name=gettext("Are you a student?"),
        widget=widgets.RadioSelectHorizontal)

    student_level = models.IntegerField(
        choices=[(0, gettext('Bachelor')), (1, gettext('Master')),
                 (3, gettext('PhD')), (4, gettext('Not in the list'))],
        blank=True)

    student_discipline = models.StringField(
        choices=["Administration", "Archeology", "Biology", "Buisiness school",
                 "Chemistry", "Computer science", "Economics","Education",
                 "Law", "Management", "Nursing school", "Engineer",
                 "Geography", "History", "Lettres", "Mathematics", "Medicine",
                 "Music", "Pharmacy", "Philosophy", "Physics", "Politics",
                 "Sociology", "Sport", "Not in the list"],
        verbose_name=gettext("What are you studying?"), blank=True)

    sport = models.IntegerField(
        choices=[(0, gettext('No')), (1, gettext('Yes'))],
        verbose_name=gettext("Do you pratice (regularly) some sport?"),
        widget=widgets.RadioSelectHorizontal)

    experience = models.IntegerField(
        choices=[(0, gettext('No')), (1, gettext('Yes'))],
        verbose_name=gettext("Have you ever participated in an experiment?"),
        widget=widgets.RadioSelectHorizontal)
