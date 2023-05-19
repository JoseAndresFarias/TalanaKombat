from src.game import TalanaKombat
import json

import config
tk = TalanaKombat()

json_file = open('game.json')

game = json.load(json_file)

result = tk.play(game)
print(result)