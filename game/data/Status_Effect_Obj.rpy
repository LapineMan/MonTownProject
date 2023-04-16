init 3 python:
    class Status_Effect_Type(Enum):
        PRE_ATTACK = 0
        POST_ATTACK = 1
        PRE_DAMAGED = 2
        POST_DAMAGED = 3
        TURN_START = 4
        TURN_END = 5
        STAT_CHANGE = 6
        PHASE_START = 7
        PHASE_END = 8

    class Slime_Digestion_Debuff:
        debuff = True
        name = "Slime Burn"
        description = "Burning slime covers you!"
        type = Status_Effect_Type.TURN_END
        life = 3

        @classmethod
        def effect(cls, subject:RpgStats):
            if(subject.statuses[cls.type][cls] == 0):
                return
            dmg = subject.deal_damage(2, 2)
            renpy.with_statement(hpunch)
            renpy.play("sounds/sfx/squelch.mp3")
            renpy.say("Slime Poisoning!", "{} received {} damage due to the burning slime!".format(subject.name, dmg))
            cls.sub(subject)

        @classmethod
        def add(cls, subject:RpgStats):
            if(cls.type not in subject.statuses):
                subject.statuses[cls.type] = {}
            subject.statuses[cls.type][cls] = cls.life
            return

        @classmethod
        def sub(cls, subject:RpgStats):
            if(subject.statuses[cls.type][cls] <= 1):
                #cls.remove(subject)
                return
            subject.statuses[cls.type][cls] -= 1

        @classmethod
        def remove(cls, subject:RpgStats):
            del(subject.statuses[cls.type][cls])
