import json
import random

class Country(): 

    @property
    def getRandomCountryData(self):
        data = random.choice(self.countries)
        country = data['name']

        if len(data['states']) == 0:
            state = data['name']
            city = data['name']
        else:
            state_data = random.choice(data['states'])
            state = state_data['name']
            city = state if len(state_data['cities']) == 0 else random.choice(state_data['cities'])['name']

        return data['name'], data['phone_code'], state, city