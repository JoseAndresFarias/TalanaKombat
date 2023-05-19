import config


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

