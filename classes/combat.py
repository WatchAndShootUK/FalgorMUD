import random
import threading
import time
from classes.player import Player
from classes.npc import NPC

class Combat(object):
    def __init__(self,defender,attacker):
        self.defender = defender
        self.attacker = attacker
        
        attacker.send_message('You attack ' + defender.name.title() + '.')
        defender.send_message('You attacked by ' + attacker.name.title() + '.')
    
    def combat_heartbeat(self):
        # Called every time heartbeat.py ticks, only fire if attacker and defender are in the same room.
        if self.defender.parent == self.attacker.parent:
            self.attacker.in_combat = True
            self.defender.in_combat = True
            if self.strike(self.attacker,self.defender):
                self.strike(self.defender,self.attacker)
        else:            
            self.attacker.in_combat = False
            self.defender.in_combat = False
            
    def try_hit(self,aim,dodge,weapon):
        # Level 20 v Level 20: 50% 
        # Level 20 v Level 20 with 100% power weapon: 75%
        # Level 20 v Level 10: 66%
        # Level 20 v Level 10 with 100% power weapon: 86%
        
        hit_chance = aim*(100/(100+dodge))
        if weapon:
            hit_chance += weapon.weapon.power/5
        if hit_chance >= random.randint(0,100):
            return True
        else:
            return False
        
    def get_dam(self,attack,defence): 
        # Level 20 v Level 20: 18 
        # Level 20 v Level 10: 20
        # Level 20 v Level 1: 22
        
        max_damage = attack*(100/(450+defence)) # Base damage
        return random.randint(int(max_damage/4),int(max_damage)) # Value from 1/4 max_damage to max_damage is returned
        
    def strike(self,attacker,defender):
        # First we try to hit the target
        if self.try_hit(attacker.skills.aim,defender.skills.dodge,attacker.inv.weapon if attacker.inv.weapon else None):
            # See what damage we do to the target.
            damage = int(self.get_dam(attacker.skills.attack,defender.skills.defence)) # Damage
            if attacker.inv.weapon:
                damage += attacker.inv.weapon.weapon.power/20 # Add 5% of weapon power to damage (max +5)
            if len(defender.inv.wearing) > 0:
                damage -= defender.inv.get_armour_power()/20 # Reduce damage by 5% of total armour power (max -10)
            damage = round(damage)
            
            if damage < 0:
                damage = random.randint(0,4) # Make sure we don't have negative damage value                
            
            if random.randint(0,100) > 99:
                damage = damage*2 # 1% chance to crit (base damage * 2).   
                if damage < 25:
                    damage = 25 # Crits do at least 25hp damage             
                attacker.send_message('You critically hit ' + defender.name.title() + ' with decimating force!')
                defender.send_message(attacker.name.title() + ' critically hits you with decimating force!')
                attacker.parent.chat_room(attacker.name.title() + ' critically hits ' + defender.name.title() + ' with decimating force!',[attacker,defender])
            else:            
                # Display chats based on what damage we did.
                attacker.send_message(CombatRound(attacker,defender,damage,0).get_emote() + ' ' +  str(damage))
                defender.send_message(CombatRound(attacker,defender,damage,1).get_emote() + ' ' + str(damage))
                attacker.parent.chat_room(CombatRound(attacker,defender,damage,2).get_emote(),[attacker,defender])
            
            # Apply that damage to our oppenent
            defender.hp -= damage
        else:
            # Miss
            attacker.send_message('You miss ' + defender.name + '.')
            defender.send_message(attacker.name + ' misses you.')
        
        if defender.hp < 0:
            # You have been killed.
            self.combat_end(attacker,defender)
            return False
        else:
            return True
        
    
    def combat_end(self,victor,loser):
        from constants.combats import combats
        combats.remove(self)
        victor.send_message('You killed ' + loser.name.title() + '.')
        loser.send_message('You have died.')
        loser.kill()
        
class CombatRound(object):  
    def __init__(self,attacker,defender,damage, index):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage
        self.index = index            
        
        self.emotes = [
                    [
                        'You massacre ' + self.defender.name.title() + ' with incredible force!',
                        self.attacker.name.title() + ' massacres you with incredible force!',
                        self.attacker.name.title() + ' massacres ' + self.defender.name.title() + ' with incredible force!'
                    ], #Massacre
                    [
                        'You inflict massive damage to ' + self.defender.name.title() + '.',
                        self.attacker.name.title() + ' inflicts massive damage to you.',
                        self.attacker.name.title() + ' inflicts massive damage to ' + self.defender.name.title() + '.'
                    ], #Inflict
                    [
                        'You hit ' + self.defender.name.title() + ' very hard.',
                        self.attacker.name.title() + ' hits you very hard.',
                        self.attacker.name.title() + ' hits ' + self.defender.name.title() + 'very hard.'
                    ], #Very Hard
                    [
                        'You hit ' + self.defender.name.title() + ' hard.',
                        self.attacker.name.title() + ' hits you hard.',
                        self.attacker.name.title() + ' hits ' + self.defender.name.title() + 'hard.'
                    ], #Hard
                    [
                        'You hit ' + self.defender.name.title() + '.',
                        self.attacker.name.title() + ' hits you.',
                        self.attacker.name.title() + ' hits ' + self.defender.name.title() + '.'
                    ], #Hit
                    [
                        'You graze ' + self.defender.name.title() + '.',
                        self.attacker.name.title() + ' grazes you.',
                        self.attacker.name.title() + ' grazes ' + self.defender.name.title() + '.'
                    ], #Graze        
                    [
                        'You scratch ' + self.defender.name.title() + '.',
                        self.attacker.name.title() + ' scratches you.',
                        self.attacker.name.title() + ' scratches ' + self.defender.name.title() + '.'
                    ], #Scratch
        ]

    def get_emote(self):
        if self.damage > 20:
            return self.emotes[0][self.index] # Massacre
        elif self.damage > 16:
            return self.emotes[1][self.index] # Inflict
        elif self.damage > 12:
            return self.emotes[2][self.index] # Hit very hard
        elif self.damage > 8:
            return self.emotes[3][self.index] # Hit hard
        elif self.damage > 4:
            return self.emotes[4][self.index] # Hit
        elif self.damage > 2:
            return self.emotes[5][self.index] # Graze
        else:
            return self.emotes[6][self.index] # Scratch
                