init 2 python:
    class SkillInterface():
        name = ""
        description = ""

        # What does the skill do
        @classmethod
        def use(cls, caster, target):
            pass

        # This serves to make it so you can make a skill force you to forget another one
        @classmethod
        def learn(cls, subject):
            pass

    class Skill_Double_Strike():
        name = "Double Strike"
        manaCost = 5
        description = "Perform 2 attack actions at once, second strike deals reduced damage"

        @classmethod
        def use(cls, attacker:RPG_Stats, targets:[RPG_Stats]):
            target = targets[0]
            renpy.say(None, "{} switfly strikes {} twice!".format(attacker.name, target.name))
            dmgDealt = attack(attacker, target)
            dmgDealt += attack(attacker, target, multiplier = 0.5)
            renpy.say(None, "Dealt a total of {} damage!".format(dmgDealt))
