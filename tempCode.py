import copy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
from random import randint

class Policy(nn.Module):#🥽🤿🔮🎷🎺🧪🧲📱🗾🌎❔Ⓜ™💬 🕒📶(⊙_⊙)💿📀🛸
  """
  implements both actor and critic in one model
  """
  def __init__(self):
    super(Policy, self).__init__()
    self.affine1 = nn.Linear(4, 128)
    self.action_head = nn.Linear(128, 2)
    self.value_head = nn.Linear(128, 1)
    self.saved_actions = []
    self.rewards = []

model = Policy()
optimizer = optim.Adam(model.parameters(), lr=3e-2)
def select_action(state):
  state = torch.from_numpy(state).float()
  probs, state_value = model(state)
# create a categorical distribution over the list of probabilities of actions
  m = Categorical(probs)


def newMachine(numbers, letters):
  pointA = 417.99
  pointB = 417
  pointC = 179
  pointD = 191919.0
  component = "neutron"
  rocket = "laser"
  paper = letters + ' ' + component + ' ' + rocket
  if pointA >= pointB and pointB >= pointC:
   print("we went from point A:", pointA, "to point C:", pointC)
  else: 
   print("We're still at point A")
  if pointC >= pointD:
   print("we went from point C:", pointC, "to point D:", pointD)
  else: 
   print("we're still at point C")
  if 't' in component and rocket:
   print("This device is the perfect version of a", paper)
  else:
   print("null") 
newMachine(177, "PC")
#-----------------

def Hawaii(oahu, maui):
 honolulu = {"Kapolei": "Spam",
              "Waimanalo Beach": "surfing",
     "Honolulu": "turtles",
     "Royal Kuna": "forgotten land",
     "Laie": "apples"
              }
 for h in honolulu:
  print(honolulu[h]) #prints out all key values
Hawaii("oahu", "maui")
#--------------

def dimensions(theory, practice):
     day1 = 71
     day2 = 11
     day3 = 0
     if theory > practice:
      day1 += float(88)
      day2 += float(888)
      day3 += 11
     else:
      day1 -= float(-88)
      day2 -= float(-888)
      day3 -= 22
      print(day3 * day1 - (8 * 189) / day2 + 1200 - 2000)
dimensions(300, 400)
#913.7027027027027
#-4299.681868743048


def bigVirus(numbers, strings):
  defrag = [12, 14, 19, 101, 39, 34, 54, 31, 67, 68, 909, 455, 777, 43, 41, 0, 0, 1, 17, 65, 1010, 1111, 222, 320, 77]
  defrag.append(444)
  defrag[1] = 32
  print(sorted(defrag)) #same as defrag.sort()
  print(defrag[10])
bigVirus(121, "this")
#--------------

def Japan(tokyo, kyoto):
  shinto = {
    "shrine" : "pond",
    "sushi" : 7.50,
    "ayaka": "strange",
    "shinzo": "comedian",
    "katana" : "sword"
  }
  for key in shinto: #because there's 5 keys it prints 5 times. So don't target a specific value unless needed
    print(shinto[key]) #using print(key) just prings out all the names of the keys. shinto[key] prints out all the values
Japan('Tokyo', 'Kyoto')
#-------------

def carShield(toyota, honda):
  prototype = [7, 77, 55, 18, 94, 43, 20, 20, 33, 37, 8, 87, 50, 97]
  new_prototype = [301, 302, 22, 232, 224, 600, 987, 555, 5757, 93, 90, 0, 80, 8888, 42]
  for proto in prototype:
    for new in new_prototype:
     prototype.sort() #ascending order
     new_prototype.sort(reverse=True) #sorts in descending order
  print(prototype) #why does print proto return 97? because is returns the last iteration
  print(new_prototype)
carShield(11, 12)
 #--------------

def aeroProject(stellar, power):
 bluePrints = 200
 sulfate = 10
 result = 0
 archives = {
  "Jet": "fuel",
  'Power Supply': 'Donut',
  "Power Failure" : "no operations",
  "void" : 'null',
  'Robot' : 'Automatic'
 }
 if bluePrints %2 == 0:
  sulfate = sulfate + 100
  result = result + 7
  print(sulfate + result * bluePrints * power)
 elif bluePrints >= stellar:
  sulfate = sulfate + bluePrints
  result -1
  print(sulfate * bluePrints)
 elif bluePrints >= power:
  sulfate + 100
  result -100
  print("Flush the stream @ ", bluePrints - power)
 else:
  print('null')
aeroProject(77.01, 500)
#-------------

janToJunRain = 1.93 + 0.17 + 3.53 + 3.04 + 3.90 + 4.40
annualRain = janToJunRain
july = 2.02
annualRain += july #concatenation
augToDec = 2.0 + 4.00 + 1.90 + 3.4 + 2.17
annualRain += augToDec
print(annualRain)
#------------

haiku = """ At the old pond,
a frog jumped out of the water:
It's now on a lilypad."""  #multiline string
#---------

#string formatting, when % formatting the values need to be in a tuple ()
string1 = "block"
string2 = 3.0
print("the value of %s is around %s" % (string1, str(string2)))
#----------

def knight(swordDmg, knightHP):
  spellBook = None
  armor = 80
  helmet = 70
  brokenGear = 0
  money = 1000
  wallet = 0
  swordAtk = "Slash"
  swordAtk2 = "Mega "
  megaAtk = swordAtk2 + swordAtk
  print(megaAtk)
  if spellBook == None:
    print("You don't have any spells")
  else:
    print("You've casted", spellBook)
  if armor == brokenGear and helmet == brokenGear:
      print("Your equipment needs repair")
  else: 
      print("Your gear doesn't need repair") #remember %s prints the result of a variable, so it's better suited for strings
      print(type(armor))
  if money == wallet:
      print('You have insufficient funds.')
  else: 
      print('Your wallet is looking good.')
knight(28, 150)
#lesson learned: AVOID DEEP NESTING, meaning make sure all if and elif and else statements are linear
#--------

def cycloneRadius(big, small): #something's wrong with this one
  tornado = "Joe"
  hurricaneRadius = 1500000
  tornadoRadius = 4000
  evaporation = hurricaneRadius / tornadoRadius
  print(type(evaporation)) #float
  new_data = str(tornadoRadius)
  new_tornado = int(tornado)
  print("I got blown away by a " + new_data + " a month ago." + new_tornado + "was it's name.") 
cycloneRadius(1000, 20000)
#----------

puffin = "Icelandic bird"
print(len(puffin))
print(puffin[9]) #space

#_________________________

def blastFurnace(controlSystem, centralUnit): #let's focus on lists, control flow, and booleans
  controlSystem = ["temperature sensor", 'pressure sensor', 'level', 'gas analysis']
  centralUnit = ['Shell', "Cooling staves", "Cooling system", 'Refactory Lining', "Charging device", "Hot blast feeding system"]
  castHouse = ["Metal and Slag separator", "Metal and Slag transporters"]
  hotBlastStove = ["Valves", "Hot Air combustion", 'Burners', 'Casing', "Bustle Main"]
  BFG_Gas_Cleaning_Plant = controlSystem + centralUnit + castHouse 
  conicalBells = 2
  airlockTypeHoppers = 3
  if len(controlSystem) < len(centralUnit):
    print("The Control System has fewer compnents than the Central Unit.")
  else: 
    print("the Central Unit has fewer components than the Control System...seriously???")

  if castHouse < controlSystem and castHouse < centralUnit:
    print("The Cast house has ", len(castHouse), "components and the Control System has ",len(controlSystem), "components. " \
      "Central Unit has", len(centralUnit), "components")
  else: 
    print("Cast House has " + len(castHouse) + "only.")

  if hotBlastStove >= BFG_Gas_Cleaning_Plant:
    print("the Hot Blast Stove has", len(hotBlastStove), "components.")
  else: 
    print("The Hot Blast Stove has more compents than a few of the machines.")

  if conicalBells != airlockTypeHoppers:
    print(True)
  else:
    print(False)
  conveyor = conicalBells**4  #2 x 2 x 2 x 2 (number, ** how many times to multiply it by itself)
  print(conveyor) #16
blastFurnace("Control System", "Central Unit")

#now focus for loops and dictionaries
#stopping point
def kitchen(fridge, myFreezer):
   fridges = {
    "Cheese Drawer": ["pepper jack cheese", "jalapenos", "ham", 'string cheese', 'hot sauce'],
     "Main Shelf": ["milk", 'juice', 'eggs', 'beef', 'grapefruit', 'chinese food', 'green peppers'],
     "Bottom Shelf": ['celery', 'bread', 'tomatoes', 'lemon', 'lime', 'beer', 'condiments', 'leftovers']
  }
   for key in fridges:
    print(fridges[key])

    freezers = {
    "Top Shelf": ["Bacon", "Icecream", "hot pockets", 'waffles', 'whiskey', 'white castle', 'popsicles', 'TV Dinner']
  }
   for key in freezers:
    print(freezers[key])

   iceCubes = 50
   iceCubeTrays = 4
   glasses = 10
   cups = 30
   everything = iceCubes / iceCubeTrays + glasses * cups
   print((iceCubes / iceCubeTrays) + glasses - cups) #-7.5
   print(everything + everything) #105.0/625.0  when I change glasses + cups to glasses * cups
kitchen("fridges", "freezer")
#--------------

def mathProblems(low, high): #python can't preform arithmitic operations between an int and a list
  prob = [7, 14, 21]
  prob2 = [15, 30, 45]
  prob3 = -900
  print(max(prob)) #max/min takes 2 or more arguments. since prob has a list of 3 ints, it targets the max int which is 21
  print(min(prob2))   #and the minimum about in prob2 is 15
  print(low * high) #2178
  print(abs(prob3)) #instead of -900 you get 900.I'm guessing it would remove a decimal point too
mathProblems(33, 66)

#________________ https://github.com/Mute10?tab=repositories
def math(multiplication, division):
 numbers = [75, 77, 777, 54, 32, 21, 10, 5, 22, 404, 33, 47, 48, 88, 509]
 numbers.remove(5) #remove acts as a filter and can only remove the element in it parentheses
 oddNums = [3, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31]
 del oddNums[3] #removes the desired index, so 11 is deleted
 evenNums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26 , 28, 30]
 del evenNums[1:7] #removes index 1-6 index 7 (16) is still in the list. This is like a slice method
  # the first index is deleted up to the 2nd index which isn't deleted, only before it.
 thisVarIsBad = 0
 del thisVarIsBad #deletes an entire variable
 squares = 4
 circles = 5
 rectangle = 7
 pentagon = 6
 area = max(squares, circles) #circles is the winner
 area2 = min(rectangle, pentagon) #pentagon has the most minimum number
math(22, 0)

#Control flow
def planet(Saturn, Mars):
  timeFlow = 1
  timeStop = 3**4
  result = 0
  for s in Saturn:
   for m in Mars:
    if s >= 0 and m >= 0:
     timeFlow += 1
     result += 2
     return timeStop + timeFlow + result + 1 #81 + 2 + 2 + 1 = 86
   else:                            #since the first values in Saturn and Mars are greater than 0 the return statement
     return result + 1              # activates on the first iteration
print(planet([1, 75, 44, 0], [4, 4, 5, 0, 9]))

def planet2(Saturn, Mars):
  timeFlow = 1  #initialization
  timeStop = 3**4
  result = 0
  for s in Saturn: #all values are interated #outer loop
   for m in Mars: #then all of mars values are #inner loop this goes first.
    if s >= 0 and m >= 0: #does this each iteration of m then s.
     timeFlow += 1
     result += 2
     timeStop + timeFlow * result * 3 #has no effect
   else:                            
     continue
  return timeStop + timeFlow + result * 4  #so timeStop is 81, timeflow becomes 21 and result becomes 40 multiply is by 4 and you get 262           
print(planet2([1, 75, 44, 0], [4, 4, 5, 0, 9]))
#lesson learned: always concatenate in for loops to make proper updates

def negative(surface, gravity):
  depth = 100
  space = 9
  result = 0
  magnify = depth + space + result #100 + 9 + 0 =109
  for s in surface:
    for g in gravity: #No updates for s since all are positive numbers
      if s < 0 or g < 0: #it's not until the second value in g until there's an update
        depth -= 200     #when true, depth - 200, space 9 + 99, and result -100
        space += 99       #magnify does the following: 109 + (109 - (-100) - 108 - (-100) * 2)
        result -= 100      #simplified: magnify = 109 + (109 + 100 -108 + 200). magnify = 109 + 301 = 410
        magnify += magnify - depth - space - result * 2 #the key formula  for magnify causes exponential growth due to the recursive
      else:                                        # magnify += magnify structure
        continue
  return result - magnify  #-631,238,239. without magnify is #16861
print(negative([22, 22, 22, 29, 22], [11, -11, -22, -33, -44])) 
#final calculation:after the variables have updated many times
#if result has decreased significantly and magnify has grown exponentially, their difference results
#in a exceptionally large negative value

def solarSystem(Sun, Moon):
  cloud = 3   
  rain = 4    
  snow = 5    
  season = cloud + rain + snow
  result = 0
  for s in Sun:
    for m in Moon:
      if s >= 0 or m >= 0:
       season += season 
       result += 33 
       print(result + season) #this condition is true: 57, 114, 195, 324
      elif s < 0 or m < 0:
       cloud -=8
       rain -= 9
       snow -= 4 
       result += cloud + rain + snow * 5
       season += season + 3
       print(result * result)
      else: 
       season += season * 8 #while this condition is False, it still glides down to continue
       result += 8 
       continue
      #print(result, "XYZ")
  return result #this return statement is reached (132)
print(solarSystem([-50, -25], [10.45, 1.90]))
#lesson learned: turn down the coefficience during initialization phase...


def motorcycle2(power, fuel): #my greatest challenge yet...It was printing the same number 30 times followed by a printed None.
  fineTuning = 3              #to Solve this I simply added some return statements. Empty return statements return None.
  dynoTuning = 78.78          # and maybe don't make the function parameters have so many list items.
  flashTuning = -40.0
  minorAdjustments = 12**3
  finalTune = fineTuning + dynoTuning + flashTuning + minorAdjustments 
  result = 0
  for p in power:
   for f in fuel:
    if p <= fineTuning and f <= fineTuning: 
     fineTuning += 7
     dynoTuning += 9
     flashTuning -= 140
     result += 1
     print(fineTuning * dynoTuning * flashTuning)
    elif minorAdjustments <= finalTune:
     minorAdjustments -= 100
     print(finalTune * fineTuning) # this codition is true, 5,309.34 is the answer, but where is None being printed from?
     return result + 2
    else: 
     print("No solution found")
print(motorcycle2([2200, 2200, 2000, 1000, 10], [130, 140, -200, 300, 30, 9]))

#______________
def windRatio(high):
  storm = 50
  hurricane = 20
  tornado = 2
  result = 0
  for h in high:
    if storm <= h:
      storm -= 10
      result +1
      print(storm * storm) #1600
      return storm
    elif hurricane > tornado:
      hurricane *= 16
      tornado += 1
      result += 2
      print(hurricane) #320 prints then 5120?
  else: 
      result += 11
      print(result + result)
      return result # the purpose of a return statement is to stop iteration once certain conditions are met
windRatio([2, 3, 55, 5, 9, 0, 22, 1])   #without return, the for loop would iterate over ever value in the function parameters.

#___________________


def greenTeaBags(dozen, gross):
  organic = 144
  grey = 50
  hamilton = 100
  result = 0
  for d in dozen:
   for g in gross:
    if organic != grey or organic != hamilton:
     organic += 9
     grey += 90
     hamilton += 3
     print(organic)
     return result + 8 
    elif grey < hamilton:   #lesson learned: print and return go hand in hand for debugging
     grey += 100
     result += 2 * 3**4
     print(result)
     continue
  return "No Solution Found"
print(greenTeaBags([12, 12, 12], [144, 144, 109]))



#call functions inside functions and use del, .pop(), and .remove()
def oilNeeded(twoGallons): #how can i add this function to airPlane?
  total = twoGallons * 4
  return total


def airPlane(engine, landing):
  securityCheck = "Inspection Passed"
  electronics = ["Not Allowed", "Razor", "cellphone", "smartwatch"]
  supplies = oilNeeded(2) # 2 gallons x 4 is 8
  print(supplies)
  result = 0
  for e in engine:
    for l in landing:
      if securityCheck != electronics:
        result += 1
        del securityCheck
        electronics.pop(0)
        print(electronics)
      else:
       continue
      print("The plane is good to go")
      return result 
airPlane([2, 2, 3], [ 4, 4, 4])

#____________________
def nintendo(console, controller):
   donkey = {"name": "Donkey Kong",
  "strength": "185", 
  "HP": "2000",
  "defense": "110", 
  "weapon": "coconuts"
  }
   mario = {"name": "Mario",
  "strength": "145", 
  "HP": "1300",
  "defense": "70", 
  "weapon": "Fire Flower"
  }
   luigi = {"name": "Luigi",
  "strength": "138", 
  "HP": "1300",
  "defense": "65", 
  "weapon": "Vacuum"
  }
   bowser = {"name": "Bowser",
  "strength": "200", 
  "HP": "1800",
  "defense": "90", 
  "weapon": "Fire Balls"
  }
   for key in luigi:
    print (key, luigi[key]) #prints the key an value name
   for key in bowser:
    print(bowser["strength"])
    print(key[2]) #targets the m in name
    return bowser # this allows me to print his strength (200) once instead of many keys a dictionary has
nintendo([22, 33, 44], [1, 2, 3])


#🦈🐋🐳🐬🐟 


def atlantic(marine, submarine):
  marine[1] = marine[1] + 13
  lobster[1] = lobster[1] + 9
  return marine + lobster
jellyfish = [4, 8, 12]
lobster = [6, 9]
print(atlantic(jellyfish, lobster)) #[4, 21, 12, 6 , 18]

#BЯΣΛKIПG BΣПJΛMIП

now = "I Don't want to save the"
later = "..."
def benjamin(liquid, metal):
  return liquid[3] + metal[0]
def broken(fuse, world):
   return fuse + ' world!'
print(benjamin([1, 2, 3, 11, 22, 33], [80, 80, 33, 22, 101]))  #91
print(broken(now, later))    

############

def computer(microsoft, sony):
  result = 0
  bridge = [-22, -9, 247]
  betaTest = microsoft + sony
  alphaTest = microsoft + bridge
  for m in range(0, len(microsoft)):
    if betaTest >= alphaTest: #this is the result I was looking for. range counts from index 0 up to the length of microsoft
      result += 1
      print(m)
    else: 
      microsoft.sort()
      print(microsoft)
      return result 
computer([300, 111, 34, 66, 230, 1], [21, 221, 421, 55, 190])

#Ég mun flytja fjöll

def robotics(arx, dro):
    mainframe = 77
    powerCord = -1
    memory = 300
    result = 0
    other = mainframe + powerCord * memory #77 + (-1) * 300 = 77 - 300 = -223
    for a in list(arx):
     for d in list(dro):
      if mainframe > powerCord: 
        other += 2
        result += 1
        print(mainframe * other)  #other starts at -223 and gets incremented by 2
      else: 
        return result 
      if powerCord < memory:
        other *= 2
        result += 1
        print(memory * memory) #90000
        return result
      else: 
        print(2**8)
        return result
print(robotics([11, 276, 343, 11, 22], [90, 0, 878, 33, 5]))
#одиссея


def knightsArmor(cloud, meteor):
  spellCircle = 'Bind '
  shadow = 'Night '
  pyro = "Engineering is a way of life"
  count = 0
  while cloud < meteor:
    print(meteor**6) #64
    count += 2
    break
  else: 
    print(meteor)
     
  for sp in spellCircle:
    print(sp) 
  for s in shadow:
     print (s)
  for char in pyro: 
    if char == 'a':
      print("0"), # the variables spellCircle, shadow, and pyro vertically
    else: 
      print (char),
print
knightsArmor(1, 2)
#исход


def odyssey(iceland, norway):
  exodus = "There will be an exodus..."
  spaceCraft = "Size. "
  forest = [11, 22, 33, 44, 455, 455, 959, 43, 1221, 33,700]
  jungle = [232, 242, 252, 262, 272, 282, 292, 200]
  hills = 8.2
  crator = 10.999
  caveSystem = 100
  oceanDepth = -100000
  result = 17
  theoryOfEverything = hills + crator + caveSystem + oceanDepth
  count = 1
  world = {
    "country": "Europe",
    "area": "30",
    "capital": "Paris",
    "tourism": "poetry"
  }
  for key in world:
    print(key, world[key])
  universe = {
    "size": "lightyears",
    "object": "moon",
    "rock": "neptune",
    "void": "black hole"
  }
  for key in universe:
    print(key[1]) #iboo
    print(universe, key[2]) #prints the dictionary 4 times + z, j, c, i
    print(universe["void"]) # black hole

  for e in exodus:
    if spaceCraft <= exodus:
     spaceCraft += exodus
     print(spaceCraft)
    else: 
     print(exodus)
    break
     
  
  for f in forest:
    if forest <= jungle:
     jungle.append(4444)
     forest.pop(3) #continues to pop 3rd index until 11, 22, 33 are left
     print([forest] + [jungle])
    else: 
      return forest

  #not iterable means it can't be iterated over
  if crator != hills:
    hills += crator
    print(hills, ", the crator is deep")
  elif crator <= hills:
    crator += hills
    result += 1
    print(crator + result)
  else: 
    return result 
  print (result)

  while caveSystem > oceanDepth:
    caveSystem += theoryOfEverything
    oceanDepth += caveSystem
    count += 77
    print(caveSystem) 
    break
  else: 
    print(oceanDepth)
odyssey(7, 777)
#HORROR


def figuration(power, cut):
  pipes = [1, 2, 3]
  radar = [33, 66, 77]
  crystal = [9, 9, 9, 9, 19]
  crypto =  [0, 88, 808, 313, 5]
  shards = max(pipes + radar) #can't multiply lists. max will get the max number in both lists
  glass = min(pipes + radar)
  print(shards)
  print(glass)
  for p in power:
   for c in cut:
    if p == radar: #'<=' not supported between instances of 'int' and 'list' even when they're both lists 
      radar.append(303)
      pipes.append(909)
      print(pipes)
      del shards
    elif c != radar:
      radar.append(-303)
      pipes.append(-909)
      radar += pipes
      print([pipes], radar)
      break
  else: 
    print("what is this")
  if crystal == crypto: 
   print("time to leave")
  else: 
   print([crystal ]+ [crypto])
figuration([111, 44, 3, 5, 88], [22, 23, 77, 8, 9])



def park(thorgarth, crowley):
 result = []
 timber = [22, 9, 7, 44, 303]
 shifts = "Any available park"
 timber.sort()#sort ony works with numbers
 alpine = 3**9
 print(alpine)
 thorgarth = thorgarth.lower()
 shifts = shifts.lower()
 for chr in shifts:
   if chr in thorgarth:
    result.append(True) 
   else: 
    result.append(False)
 print(result)
 return result #my guess is when the " is reached in thorgarth it ends the loop
park("Anything", "parking lot")




def numsss(num1, num2):
  whatNum = 33.34
  overNum = 9000
  staticNum = [202.2, 205, 215, 222.2, 270, 275, 5, 6, 544, 33, 10.23]
  frozenNum = [-112, 0, -222.3, 500, 900, 17, -17.777, 7, 5, -5, -50.003]
  result = []
  for st in range(0, len(staticNum)):
    for fr in range(0, len(frozenNum)):
      if staticNum in num1 or frozenNum in num1:
        result.append(20999)
        staticNum.append(11111)
        frozenNum.append(-111111)
        print(result + staticNum + frozenNum)
        return result
      else: 
        staticNum.pop(1) #205 has been removed
        result.append(-20999)
        print("Hey", staticNum +  [result])
        return result
numsss([22, 220, 343, 590, 40], -1000)

#range and continue
def farm_house(crops, stable):
  supplies = ["pitch fork", "tractor", "harvestor", "pig trough"]
  acres = 77.03
  result = [11, 22, 33, 4, 44, 55, 66, 77, 88, 99, 0]
  for r in range(0, len(result), 2):#starting from index 0(11) I go up two indexes per interation until the end of the list
    if result[r] % 11 ==0:
     print(result[r])
    else:
     print(0.0, "lol")
  for su in supplies:
    if su == "":
      continue
    acres += acres * acres
    print(su[9]) #k
    print(acres)
    return
  else: 
     print(0.0)
farm_house(17, 17)

#--------------
#devleoper training: starting with f-string syntax
player_health = 100
player_has_magic = True

print(f"player_health is a/an {type(player_health).__name__}")
print(f"player_has_magic is a/an {type(player_has_magic).__name__}")


name = "DaBeard"
age = 37
race = "Dwarf"

print(f"{name} is a {race} who is {age} years old.")

# None(NoneType) is not a string, or an integer
enemy = None 
print(enemy is None)


#New quests
quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

print(f"{quest_start}")
print(f"{quest_middle}")
print(f"{quest_end} {quest_objective}")
#---------------

#finding the average score between four players
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105

average_score = (game_one_score + game_two_score + game_three_score +
                game_four_score) /4


print(round(average_score))
#--------------

#magic of f
name = "Lopen"
level = 25
character_class = 'Windrunner'
armor = 12
magic_resistance = 15.4
account_active = True

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")
print("Character Report Complete")
print("Data types:")
print(
    f"level: {type(level).__name__}, name: {type(name).__name__}, character_class: {type(character_class).__name__}"
)
print(
    f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
)
print(
    f"account_active: {type(account_active).__name__}"
)
#-------------

#length of weapons, call function in the function, not just at the end
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
spear_length = 2.0
sword_area = area_of_circle(sword_length)# <--------
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")
print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
#----------

def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
#--------------

#fahrenheit to celsius converter
def to_celsius(f):
  calc = 5/9 * (f - 32) 
  return calc

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")

test(100)
test(88)
test(104)
test(112)
#------------

#hours to seconds conversion
def hours_to_seconds(hours):
    convert = hours * 60**2
    return convert

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

test(10)
test(1)
test(25)
test(100)
test(33)
#--------------

def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power =  power + 1
    return title, new_power
    
def main():
    test("Frodo Baggins", 5) #full_name + the warrior followed by their power level
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)

def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)
main()

#_________

#this code calculates how much health a player has left after getting punched or slashed
#the armor resistance effects this
def get_punched(health, armor = 0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor = 0):
    damage = 100 - armor
    new_health = health - damage
    return new_health

def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")


test(400, 5)
test(300, 3)
test(200, 1)

#---------------

def curse(weapon_damage = 100):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.75
    return lesser_cursed, greater_cursed

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
#greater cursed was doing less damage at 0.25 which made no sense so i change it to 0.75

def main():
    test(100)
    test(500)
    test(1000)
main()
#--------------

#damage testing with enchanted weapons subtracted from health pool
def enchant_and_attack(target_health, damage, weapon):
    new_enchantment = damage + 10
    newHealth = target_health - new_enchantment
    enchanted_weapon = f"enchanted {weapon}"
    return enchanted_weapon, newHealth

def test(target_health, damage, weapon):
    print("The target has", target_health, "health.")
    print(weapon, "base damage:", damage, "- Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print("The target has been attacked with the", enchanted_weapon)
    print("The target has", new_health, "health remaining.")

def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")
main()




#🔋💿📀 let's work with None 
def main(battery, deal):
    outlet, watts, surge = 72, 1910, -29
    solution = outlet * watts * surge
    print(f"{solution}")
    if battery <= outlet:
      battery += battery + outlet
      print(battery) #92.19999999999999
    else: 
      return None

def calendar(month, day): # \ can start a new line
    what_day, what_month, solution = "Between 1 and 20 every month we'll hold a beer festival!", "Except January.", \
      "January is a sad month lmao..." 
    print(f"{what_day} {what_month} {solution}")
    return solution
calendar(22, 22)

def events(sword, shield):
    blastEmEvent, auto = [0, 0, 22, -9], [313, 274, 171717, -9.9]
    blastEmEvent[0] = 72
    auto.append(72)
    print(f"{blastEmEvent} {auto}")
    solution = auto.pop(0)
    print(f"{auto}") #just printing auto prints the varible without pop
    return solution 
events("Attack", "Block")

def newLanguage(GO, STOP):
    listOne = [10, 2, 2.6, 3.0, 4.0, 81.81]
    listTwo = [2, 10.1, 99, 7, 0, 7]
    num1 = 44
    num2 = 44.4
    result = [0, 0]
    for l in listOne:
     for ll in listTwo:
      if num1 >= num2:
       num2 += num2
       num1 -= num1 
       print(f" {num2}, {num1}")
     else: 
       num2 *= num2 * num2
       num1 *= 3 * 4**8
       print(f"outer for loop: {l}, inner for loop: {ll}, num2: {num2}, num1: {num1}")
       result.append(0)
       print(result)
       return None
newLanguage(33, 34)
main(10.100, 20)

#🛺

def scientists(hp, damage, weapon):
    beaker = 9
    poweredUpBeaker = damage + beaker
    newHp4 = hp - poweredUpBeaker
    powerUpBeaker = f"powered up {weapon}"
    return powerUpBeaker, newHp4


def test(hp, damage, weapon):
    print("The target has", hp, "health.")
    print(weapon, "base damage:", damage, "- Enchanting and attacking.")
    powerUpBeaker, newHp4 = scientists(hp, damage, weapon)
    print("The target has been attacked with the", powerUpBeaker)
    print("The target has", newHp4, "health remaining.")

def tester():
    test(100, 9, "beaker")
    test(500, 19, "nitro")
    test(1000, 29, "chemicals")
    test(1000, 200, "Powered Up Beaker")
tester()
