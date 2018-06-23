import os

from prettyconf import Configuration


config = Configuration(starting_path=os.path.basename(__file__))


# BR Santa Catarina
BR_SC_USERNAME = config('SANTA_SC_USERNAME')
BR_SC_PASSWORD = config('SANTA_SC_PASSWORD')
