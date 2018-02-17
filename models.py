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

    nationality = models.StringField(
        label=ugettext("What nationality are you?"),
        choices=[
            'Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan',
            'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian',
            'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian',
            'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean',
            'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian',
            'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese',
            'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean',
            'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian',
            'Comoran', 'Congolese', 'Costa Rican', 'Croatian', 'Cuban',
            'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch',
            'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian',
            'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian',
            'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian',
            'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan',
            'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian',
            'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian',
            'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian',
            'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani',
            'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian',
            'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner',
            'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian',
            'Malaysian', 'Maldivian', 'Malian', 'Maltese', 'Marshallese',
            'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan',
            'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana',
            'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'New Zealander',
            'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean',
            'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan',
            'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian',
            'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan',
            'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean',
            'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois',
            'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian',
            'Solomon Islander', 'Somali', 'South African', 'South Korean',
            'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish',
            'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai',
            'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian',
            'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan',
            'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite',
            'Zambian', 'Zimbabwean'])

    age = models.IntegerField(
        label=ugettext('How old are you?'),
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
