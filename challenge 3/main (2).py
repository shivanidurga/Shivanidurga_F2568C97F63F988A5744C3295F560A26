#define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

#define the derived class batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
    
#define the derived class blower
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create object of batsman and bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play method for each object
batsman.play()
bowler.play()
