import pickle
import re

# from config import PARSED_PKL, RASA_FILE

ENTITY_RE = r'([A-Z]+):([^ ]+)'
RASA_ENTITY_RE = r'[\2](\1)'

entity = re.compile(ENTITY_RE)

with open("parsed.pkl", 'rb') as file:
    intents = pickle.load(file)
    with open("training_data_v2.yml", 'w') as rasa:
        rasa.write("version: "2.0" "\n\n")
        rasa.write("nlu:\n")
        for intent in intents:
            rasa.write(f'- intent:{intent}\n')            
            rasa.write(f'  examples: |\n')            
            for utterance in intents[intent]:
                utterance = entity.sub(RASA_ENTITY_RE, utterance)
                utterance = utterance.replace('_', ' ')
                rasa.write(f'    - {utterance}\n')
