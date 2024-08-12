from agents.normalization import description_normalization
from agents.compatibility import description_preprocessing

from agents.compatibility import description_compatibility
from agents.compatibility import application_compatibility

from agents.compatibility import application_compatibility_eco
from agents.compatibility import description_compatibility_eco

from agents.customization import resume_template
from agents.customization import resume_customization

from agents.customization import email_template
from agents.customization import email_customization

from agents.customization import letter_template
from agents.customization import letter_customization

from configs.questions import application_questions
from configs.questions import description_questions
from configs.categories import category_keymap


class Agents:
    def __init__(self):
        self.description_normalization = description_normalization
        self.description_preprocessing = description_preprocessing
        self.description_compatibility = description_compatibility
        self.description_compatibility_eco = description_compatibility_eco

        self.application_compatibility = application_compatibility
        self.application_compatibility_eco = application_compatibility_eco

        self.resume_template = resume_template
        self.resume_customization = resume_customization

        self.email_template = email_template
        self.email_customization = email_customization

        self.letter_template = letter_template
        self.letter_customization = letter_customization

        self.application_questions = application_questions
        self.description_questions = description_questions
        self.category_keymap = category_keymap
