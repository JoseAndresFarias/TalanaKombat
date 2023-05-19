import config
from typing import Any

tranlator = {
    'A': "se mueve a la izquierda",
    'D': "se mueve a la derecha",
    'S': "se agacha",
    'W': "salta",
    'K': "patea a su oponente.",
    'P': "golpea a su oponente.",
}

class Player:
    def __init__(self, character_name: str) -> None:

        if not character_name in config.CHARACTERS_INFO.keys():
            raise RuntimeError(f'No character named {character_name} defined')

        self.name = character_name
        self.hp = config.CHARACTERS_INFO[character_name]['hp']
        self.is_alive = True

        self.special_attacks = {}

        for special_attack_name, special_attack_info in config.CHARACTERS_INFO[character_name]['special_attacks'].items():
            self.special_attacks[special_attack_info['combination']] = (special_attack_name,special_attack_info['damage'])

    
    def recieve_damage(self, damage: int) -> None:
        self.hp -= damage
        self.is_alive = self.hp > 0

    def take_turn(self, turn: str, opponent: Any) -> str:

        if not self.__validate_turn(turn):
            raise RuntimeError('Invalid turn')

        turn_description = self.name + ' '

        while turn != '':
            if not turn in self.special_attacks.keys():
                # Not special attack, so takes first key
                key = turn[0]
                connector = ", " if len(turn) > 2 else " y " if len(turn)> 1 else ''
                turn_description += self.__translate_key(key) + connector

                if key in ['K', 'P']:
                    opponent.recieve_damage(1)

                turn = turn[1:]
            else:
                #Special attack
                attack = self.special_attacks[turn] # attack = (name, damage)
                turn_description += 'ataca con su ' + attack[0]
                opponent.recieve_damage(attack[1])
                break
            
        return turn_description
    
    def __translate_key(self, key: str) -> str:
        if not key in tranlator.keys():
            raise RuntimeError('Invalid movement')

        return tranlator[key]

    def __validate_turn(self, turn: str) -> bool:
        if len(turn) > 6:
            return False
        if len(turn) > 5 and turn[5] not in ['K','P']:
            return False
        if turn.count('K') > 1 or turn.count('P') > 1:
            return False
        if not turn.isupper():
            return False
        
        return True