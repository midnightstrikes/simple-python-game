import random
import time
class Game:
    life = 3
    attackSayings = ["ouch!", "oof!", "Noo!"]
    attackOrNo = ["yes", "y", "no"]

    def main(self):
        checkAttack = random.choice(self.attackOrNo)
        if checkAttack in ("yes", "y"):
            self.attack()
        if checkAttack in ("no"):
            self.heal()

    def attack(self):
        randomSaying = random.choice(self.attackSayings)
        time.sleep(1)
        self.life -=1
        print randomSaying
        time.sleep(1)
        self.checkHealth()

    def heal(self):
        time.sleep(1)
        print "I feel so much better!"
        self.life +=1
        time.sleep(1)
        self.checkHealth()

    def checkHealth(self):
        lifeNew = str(self.life)
        if self.life == 1:
            print "You have 1 life left"
        else:
            print "You have " + lifeNew + " lives left"

    def checkDead(self):
        lifeNew = str(self.life)
        if self.life <= 0:
            time.sleep(1)
            print "You are dead, thanks for playing!"
        else:
            print "You survived."

gameNew = Game()
while gameNew.life > 0:
    gameNew.main()
else:
    gameNew.checkDead()
