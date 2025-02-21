# Code sourced from: https://github.com/benyaminsalimi/Iranian-national-code-generator/blob/master/ir_national_code.py
# This is an open source project for generating and validating Iranian national identification codes
#__author__ = 'Benyamin Salimi <Benyamin.Salimi@gmail.com>'

import re
import random
from src.utils.loadData import load_data

class ir_national_code(object):
    def __init__(self):
        # city_codes.json from https://github.com/fandogh/codemeli/docs
        self.city_codes = load_data("src/data/city_codes.json")

    # validate the national code
    # https://gist.github.com/ebraminio/5292017
    def validator(self, input):
        if not re.search(r'^\d{10}$', input):
            return False
        check = int(input[9])
        s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
        return (s < 2 and check == s) or (s >= 2 and check + s == 11)


    # return national code by state name
    def by_state(self, target_state):
        for city_code in self.city_codes:
            if target_state in self.city_codes[city_code]:
                x = random.randint(10000000, 19999999)
                code = str(city_code + str(x)[1:])
                city = self.city_codes[city_code]

                return code , city
            
        return "not a valid state" , None

    # return national code by state name
    def by_citycode(self, citycode):
        for city_code in self.city_codes:
            if city_code == citycode:
                x = random.randint(10000000, 19999999)
                code = str(citycode + str(x)[1:])
                city = self.city_codes[city_code]
                return code , city

        return "not a valid city code" , None
    
    def randomCode(self):
        
        city_code = random.choice(list(self.city_codes.keys()))
        city = self.city_codes[city_code]
        x = random.randint(10000000, 19999999)
        code = str(city_code + str(x)[1:])
        return code , city
    
    def get_city_codes_data(self):
        return self.city_codes