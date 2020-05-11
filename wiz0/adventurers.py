from .d20 import roll_dice


class Adventurer:

    def __init__(self, attributes=None):
      self.attributes = attributes
      if not attributes:
          self.roll_attributes()

    def roll_attributes(self):
        self.attributes = {
            'strength': 10,
            'intelligence': 10,
            'wisdom': 10,
            'constitution': 10,
            'charisma': 10,
            'luck': 10,
            'dexterity': 10,
        }
        for attribute, value in self.attributes.items():
            self.attributes[attribute] += roll_dice('1d6+2')

    def __str__(self):
        return ' '.join([f'k=v' for k, v in sorted(self.attributes.items())])
