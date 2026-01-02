#!/usr/bin/python3

# # Project 1: Archer Class with Shoot Method
# class Archer:
#     arrows = 10

#     def shoot(self):
#         self.arrows -= 1

# robin = Archer()

# robin.shoot()
# robin.shoot()
# robin.shoot()

# print(robin.arrows)



# # Project 2: Mage Class with Cast Spell Method
# class Mage:
#     mana = 100
#     spells_cast = 0

#     def cast_spell(self, mana_cost):
#         self.mana -= mana_cost
#         self.spells_cast += 1

# merlin = Mage()

# merlin.cast_spell(25)
# merlin.cast_spell(40)

# print(merlin.mana)
# print(merlin.spells_cast)



# Project 3: Warrior Class with Attack Method
class Warrior:
    strength = 50
    rage = 0

    def attack(self):
        damage = self.strength + self.rage
        self.rage += 10
        return damage
    
conan = Warrior()

print(conan.attack())
print(conan.attack())



# Project: Tank Class with Fuel Efficiency
class Tank:
    fuel = 100
    weight = 50
    engine_power = 80

    def get_fuel_efficiency(self):
        base_efficiency = 10
        base_efficiency -= self.weight / 10
        base_efficiency += self.engine_power / 20
        return base_efficiency
    
francis_fury = Tank()

print(francis_fury.get_fuel_efficiency())