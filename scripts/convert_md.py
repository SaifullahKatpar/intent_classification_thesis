import pickle
import re

# from config import PARSED_PKL, RASA_FILE

ENTITY_RE = r'([A-Z]+):([^ ]+)'
RASA_ENTITY_RE = r'[\2](\1)'

entity = re.compile(ENTITY_RE)

with open("parsed.pkl", 'rb') as file:
    intents = pickle.load(file)
    with open("training_data_v2.md", 'w') as rasa:
        for intent in intents:
            rasa.write(f'## intent:{intent}\n')
            for utterance in intents[intent]:
                utterance = entity.sub(RASA_ENTITY_RE, utterance)
                utterance = utterance.replace('_', ' ')
                rasa.write(f'- {utterance}\n')
