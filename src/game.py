from src.player import Player

class TalanaKombat:
    def __init__(self) -> None:
        self.player1 = None
        self.player2 = None
        
        # text = self.player1.take_turn('AAP', self.player2)
        # print(text)
        # text = self.player1.take_turn('AADSDK', self.player2)
        # print(self.player2.is_alive)

    def play(self, game: dict) -> str:

        
        self.player1 = Player('Tonyn Stallone')
        self.player2 = Player('Arnaldor Shuatseneguer')

        player1_movements = game["player1"]['movimientos']
        player1_attacks = game["player1"]['golpes']
        player2_movements = game["player2"]['movimientos']
        player2_attacks = game["player2"]['golpes']

        if len(player1_attacks) != len(player1_movements) \
                    or len(player2_movements) != len(player2_attacks)\
                    or len(player1_movements) != len(player2_movements):
            raise RuntimeError("Error in game size")

        total_turns = len(player1_movements)

        player1_turns = [
            player1_movements[i] + player1_attacks[i] for i in range(total_turns)
        ]
        player2_turns = [
           player2_movements[i] + player2_attacks[i] for i in range(total_turns)
        ]


        combat_description = ''
        for i in range(total_turns):
            # Find the order of attacks
            first_attacker, second_attacker = self.__get_order(
                player1_turns[i], player2_turns[i]
            )


            first_attacker_turn = player1_turns[i] if self.player1.name in first_attacker.name else player2_turns[i]
            second_attacker_turn = player2_turns[i] if self.player2.name in second_attacker.name else player1_turns[i]
            combat_description +=  '\n' +  first_attacker.take_turn( first_attacker_turn , second_attacker)
            if second_attacker.is_alive:
                combat_description += '\n' + second_attacker.take_turn( second_attacker_turn , first_attacker)

            if not (self.player1.is_alive and self.player2.is_alive):
                break

        if(self.player1.is_alive and self.player2.is_alive):
            raise RuntimeError('Error: both fighters survived')

        result = lambda player: f'{player.name} gana la pelea y aun le queda {player.hp} de energia '

        combat_description += '\n'
        combat_description += result(self.player1) if self.player1.is_alive else result(self.player2)

        return combat_description

    def __get_order(self, turn_player1: str, turn_player2: str) -> (Player, Player):

        def split_turn(turn: str) -> (int, int):
            if 'K' in turn or 'P' in turn:
                return 1, len(turn) -1

        first_attacker = self.player1
        second_attacker = self.player2

        if len(turn_player1) < len(turn_player2):
            pass
        elif len(turn_player2) < len(turn_player1):
            first_attacker, second_attacker = second_attacker, first_attacker
        else:

            player1_attacks, player1_movements = split_turn(turn_player1)
            player2_attacks, player2_movements = split_turn(turn_player2)

            if player2_movements < player1_movements:
                first_attacker, second_attacker = second_attacker, first_attacker
            elif player2_attacks < player1_attacks:
                first_attacker, second_attacker = second_attacker, first_attacker

        return first_attacker, second_attacker
