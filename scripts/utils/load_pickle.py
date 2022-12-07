import pickle
import re

# from config import PARSED_PKL, RASA_FILE

ENTITY_RE = r'[A-Z]+:'
RASA_ENTITY_RE = r''

entity = re.compile(ENTITY_RE)

with open("PARSED.pkl", 'rb') as file:
    intents = pickle.load(file)
    with open("./data/intent-data.csv", 'w') as rasa:
        for intent in intents:
            for utterance in intents[intent]:
                utterance = entity.sub(RASA_ENTITY_RE, utterance)
                utterance = utterance.replace('_', ' ')
                rasa.write(utterance+","+intent+"\n")