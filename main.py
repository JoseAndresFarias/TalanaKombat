from src.game import Game


player1 = Player('Tonyn Stallone')
player2 = Player('Arnaldor Shuatseneguer')

text = player1.take_turn('AADSDP', player2)
print(text)
text = player1.take_turn('AADSDK', player2)
print(player2.is_alive)