import math
import random
import string

#copy static http://localhost:8888

def generate_random_string(length=10, character_set=None):
  
    if character_set is None:
        character_set = string.ascii_letters + string.digits
    random_chars = random.choices(character_set, k=length)
    return ''.join(random_chars)

# Generate a 10-character alphanumeric string
random_string = generate_random_string()
print(random_string)  # e.g. "aB3xF9tZ0p"

# Generate an 8-character string with only lowercase letters
lowercase_string = generate_random_string(8, string.ascii_lowercase)
print(lowercase_string)  # e.g. "abcdefgh"

# Generate a 12-character password with letters, digits, and punctuation
password = generate_random_string(12, string.ascii_letters + string.digits + string.punctuation)
print(password)  # e.g. "a@3xF9!Z0p&*
#END


# .append() is for lists
# .add() is for sets
# .update() updates the current set or dictionary
# + adds to strings(concatenation)
# Tuples are immutable



def newMachine(numbers, letters):
  pointA = 417.99
  pointB = 417
  pointC = 179
  pointD = 191919.0
  component = "Neutron"
  rocket = "Laser"
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
newMachine(177, "Alpha")
#-----------------
   #pass is a placeholder that does nothing lol
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

def Japan(tokyo, kyoto):
  shinto = {
    "shrine" : "pond",
    "sushi" : 7.50,
    "ayaka": "strange",
    "shinzo": "comedian",
    "katana" : "sword"
  }
  for key in shinto: #because there's 5 keys it prints 5 times. So don't target a specific value unless needed
    print(shinto[key]) #using print(key) just brings out all the names of the keys. shinto[key] prints out all the values
Japan('Tokyo', 'Kyoto')
#END

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


def bigVirus(number, string):
  defrag = [12, 14, 19, 101, 39, 34, 54, 31, 67, 68, 909, 455, 777, 43, 41, 0, 0, 1, 17, 65, 1010, 1111, 222, 320, 77]
  defrag.append(444)
  defrag[1] = 32
  print(sorted(defrag)) #same as defrag.sort()
  print(defrag[10])
  print(sorted(number))
bigVirus([77, 55, 4, 909, 44, 1, 3, 34], "this")
#--------------

def carShield(toyota, honda):
  prototype = [7, 77, 55, 18, 94, 43, 20, 20, 33, 37, 8, 87, 50, 97]
  new_prototype = [301, 302, 22, 232, 224, 600, 987, 555, 5757, 93, 90, 0, 80, 8888, 42]
  for proto in prototype:
    for new in new_prototype:
     prototype.sort() #ascending order
     new_prototype.sort(reverse=True) #sorts in descending order
  print(prototype) #why does print return 97? because it returns the last iteration
  print(new_prototype)
carShield(11, 12)
 #END 

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
#END 

janToJunRain = 1.93 + 0.17 + 3.53 + 3.04 + 3.90 + 4.40
annualRain = janToJunRain
july = 2.02
annualRain += july #concatenation
augToDec = 2.0 + 4.00 + 1.90 + 3.4 + 2.17
annualRain += augToDec
print(annualRain)
#END 

haiku = """ At the old pond,
a frog jumped out of the water:
It's now on a lilypad."""  #multiline string
#END 

#string formatting, when % formatting the values need to be in a tuple ()
string1 = "block"
string2 = 3.0
print("the value of %s is around %s" % (string1, str(string2)))
#END 

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
#END 

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
#END 

puffin = "Icelandic bird"
print(len(puffin))
print(puffin[9]) #space

#END 

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
    print("Cast House has " + str(len(castHouse)) + "only.")

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
#END 


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
#END 

def mathProblems(low, high): #python can't preform arithmitic operations between an int and a list
  prob = [7, 14, 21]
  prob2 = [15, 30, 45]
  prob3 = -900
  print(max(prob)) #max/min takes 2 or more arguments. since prob has a list of 3 ints, it targets the max int which is 21
  print(min(prob2))   #and the minimum about in prob2 is 15
  print(low * high) #2178
  print(abs(prob3)) #instead of -900 you get 900. no decimal point 
mathProblems(33, 66)

#________________ https://github.com/Mute10?tab=repositories
def math(multiplication, division):
 numbers = [75, 77, 777, 54, 32, 21, 10, 5, 22, 404, 33, 47, 48, 88, 509]
 numbers.remove(5) #remove acts as a filter and can only remove the element in it parentheses
 oddNums = [3, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31]
 del oddNums[3] #removes the desired index, so 11 is deleted
 evenNums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26 , 28, 30]
 del evenNums[1:7] #removes index 1-6 index 7 (16) is xclusive. This is like a slice method
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
#END 


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
#END 

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
#END 

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
#END 

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


def motorcycle2(power, fuel): #my greatest challenge yet...It was printing the same number 30 times followed by None.
  fineTuning = 3              #to Solve this I simply added a return statement. Empty return statements return None.
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
     print(finalTune * fineTuning) # this codition is true, 5,309.34 
     return result + 2
    else: 
     print("No solution found")
print(motorcycle2([2200, 2200, 2000, 1000, 10], [130, 140, -200, 300, 30, 9]))

#END 

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

#END 


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
#END 


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

#END 

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
#END 


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

#END 

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

##END 

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
#END 


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
#END 


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
#END 


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
#END 


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
#END 



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
#END 

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

#END 

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
#END 

#finding the average score between four players
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105

average_score = (game_one_score + game_two_score + game_three_score +
                game_four_score) /4


print(round(average_score))
#END 

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
#END 

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
#END 

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
#END 

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
#END 

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
#END 

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

#END 

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

#END 

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
#END 

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
#END 



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

def calendar(month, day): # \n can start a new line
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

#END 

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
#END 

#global variables can be used in any scope in the program


def total_xp(level, xp_to_add): # a unit test that calculates how much exp you'll have per level
   xp = (level * 100) + xp_to_add #and if any extra exp is added
   return xp
total_xp(1, 100)

#END 

def take_magic_damage(health, resist, amp, spell_power):
    totalMaximumDamage = (spell_power * amp) - resist
    playerHp = health - totalMaximumDamage
    print(playerHp)
    return playerHp
take_magic_damage(1500, 5, 25, 35)
#First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. 
# Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and 
# return the new health.

# // is floor division (rounded down)
linkinpark = 444 // 4
print (linkinpark) #111

#changing in place
def update_player_score(current_score, increment):
    score = current_score + increment
    bigScore = 44
    bigScore = bigScore * 8
    print(bigScore) #352
    return score
update_player_score(22, 2)
#END 

#practice using & bitwise and operator with binary numbers
#which functions return True or False?
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
     userInput = can_create_guild & user_permissions 
     return userInput
get_create_bits(0b0101)


def get_review_bits(user_permissions):
    userInput = can_review_guild & user_permissions
    return userInput
get_review_bits(0b0101)


def get_delete_bits(user_permissions):
    userInput = can_delete_guild & user_permissions
    return userInput
get_delete_bits(0b0101)


def get_edit_bits(user_permissions):
    userInput = can_edit_guild & user_permissions
    return userInput
get_edit_bits(0b0101)
#END 

#practice using bitwise | operator (or)
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    calculatePermissions = glorfindel | galadriel | elendil | elrond
    return calculatePermissions
calculate_guild_perms(0b0101, 0b0111, 0b0111, 0b0110) #only 1 and 0 can be used in binary 



def dontSub():
    defense = 2.33e15 #15 is the highest scientific notation. the first few numbers are multiplied and e is 10 ^15
    #print(defense) #using scientific notation seems to always require a floating number
    attack = 2217.7790
    hp = 1118.12
    dodge = 82
    swipe = 89
    sprint = attack // 2 #1108.0 floor takes two numbers and rounds down to the nearest integer
    doubleSprint = hp //3 #372.0
    if attack or hp >= 99.99:
     print(0b0010) #2
    elif attack and hp <= 9999:
     print(0b0100) #4
    elif not swipe < dodge: #not returns False if the input was True and vice-versa.
      print(swipe + 1000)
    else: 
      return None
dontSub()
#END 


def binary_string_to_int(num_servers, num_players, num_admins):
    newData = int(num_servers, 2)
    new_data = int(num_players, 2)
    new_Data = int(num_admins, 2)
    return newData, new_data, new_Data
binary_string_to_int("100", "101", "110")


def player_1_wins(player_1_score, player_2_score):
    if player_1_score > player_2_score:
     return True
    else: 
     return False
player_1_wins(11, 10)

express = "result" == "fruit"
print(express)


def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
player_status(4)

#memo: and boolean requires both conditions to be true to return true
#or boolean returns true if atleat one condition is true 

def does_attack_hit(attack_roll, armor_class):
    if attack_roll != 1 and attack_roll >= armor_class or attack_roll == 20:
        return True
    else: 
        return False
does_attack_hit(20, 9)

 #Drinking virtual beer refills stamina!

def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
      return False
    if on_break:
      return False
    if time < 5 or time > 10: #can a number be both less than 5 AND greater than 10 at the same time? No! 
      return False
    return True
print(should_serve_customer(22, False, 7)) #All conditions are true

#above code is supposed to be a cleaner version... I disagree
def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21 and not on_break and time >= 5 and \
     time <= 10:
     return True
    return False
should_serve_customer(21, True, 7)
#END 

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = (distance_one_way * 2) / meters_per_energy #by dividing meters by the distance you'll correctly calculate
    print(energy_needed)                                        #the amount of energy points needed
    if energy_needed <= energy_available:
        return True
    return False
has_enough_energy(500, 180, 200)

#more range practice
def arrow(length, distance):
   become_warrior = "Onomotopia" #10 characters
   become_archer = "Sniper tactics"
   for i in range(0, len(become_warrior)): # 0-9 is printed
    print(i)
arrow(8, 55)

for i in range(-22, 1): #the first number can never equal the second. So it decrements by 1
 print(i)


 #remember len() is for strings 
operation = 20
for q in range(0, operation): 
   #without break here it would count from 0 up to 1010990 so lets change operation to 20
 print(q) #19

#range doesn't work with float and list objects

for i in range(3, 0, -1): #using the third step "step" you can also count  backwards
    print(i)

    #Remember you can use in-place operators to increase or decrease a variable by any amount.

    def sum_of_odd_numbers(end):#this function counts only odd numbers starting from one
     total = 0
     for i in range(1, end, 2):
        total += i
     return 
    sum_of_odd_numbers(33)

    #while: It's a loop that continues while a condition remains True
def regenerate(current_health, max_health, enemy_distance):
     while enemy_distance > 3 and current_health < max_health:
        current_health += 1
        enemy_distance -= 2
     return current_health #iterates twice or until players health is at max
regenerate(8, 10, 20)


def countdown_to_start(): #remember the second number is exclusive and is decremented by 1. so to stop at 1 you need 0
    for i in range(11, 0, -1):
      i -= 1
      print(f"{i}...")
            
      if i == 1:
        print("1...Fight!")

#what this code does is calculate how huch damage will be done in 5 swings.
def calculate_flurry_crit(num_attacks, base_damage):
    total = 0
    for i in range(0, num_attacks, 1):
      if i == num_attacks -1: #since i will never reach num_attacks a -1 in in order
           total += base_damage * 4 #this function runs on if i < num attacks
           print(total) #prints tthe final attack
      else:
            total += base_damage * 2
            print(total) #four attacks prints first
    return total
calculate_flurry_crit(5, 13)


def calculate_experience_points(level): #this calculates how much exp you'll have accumulated by each level
    xp = 0
    for i in range(1, level):
      if level == 4:
          xp += i * 5
          print(xp)
    return xp
calculate_experience_points(4)#solving this problem took me about an hour...


#find prime and non prime numbers
def is_prime(number): 
    if number < 2: #this checks for non prime numbers as all number less than 2 are not
        return False
    for i in range(2, number):
     if number % i == 0: #finds prime numbers and if there are none, return True
      return False
    return True
#attached to this is some code that runs a series of tests
  #the function is_prime is called on line 1343
  # Basically, the code above works with the tests below. the for and if statements iterate through the each case          
run_cases = [
    (7, True),
    (-7, False),
    (9, False),
    (23, True),
]

submit_cases = run_cases + [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (4, False),
    (31, True),
    (100, False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_prime(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("Resolved")
    else:
        print("Failed")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()


#Energy Supply
def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana and (energy > 0 or energy_drinks > 0): 
      if energy > 0:
        mana += 1 #while meditating one energy is converted into mana until max mana is reached(40)
        energy -= 1
        print(f"{mana} {energy}") #without the parenthesis the console will explode.
                                  #they ensure proper operator precedence
      elif energy == 0:
       energy_drinks -= 1 #I don' need to check energy drinks here because it does it in the while loop
       energy += 50 #energy never reached 0 so no energy drinks are consumed
    return mana, energy, energy_drinks
meditate(20, 40, 50, 3)
    

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore": #changes the second index to iron bar
     inventory[1] = "Iron Bar"
     
    return inventory
smelt_ore(["Desert", "Iron Ore", "Axe", "Diamond"])


def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    for i in range(0, len(items)):
        if "Potion" in items[i]: 
         potion_count +=1
        if "Bread" in items[i]:
         bread_count +=1
        if "Shortsword" in items[i]:
         shortsword_count +=1

    return potion_count, bread_count, shortsword_count
#END 

def contains_leather_scraps(items):
    found = False

    for item in items: #searching for the value (key value) in a list
        if item == "Leather Scraps":
            found = True

    return found
    #END 


def check_character_levels(): 
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    for i in range(0, len(old_character_levels)):#this compares the values of each variable and returns the indes number where the new
        if old_character_levels[i] < new_character_levels[i]: #level is higher than the old one
            print(i)    #2, 3 7          to make this more interesting, change the i, to an index number for specific comparisons
      
def test():#this is more like a visual inspection test. Much simpler than standard tests
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")
def main():
    test()
main()
#END 

def find_max(nums): #how to find the maximum value in a list
    max_so_far = float("-inf") #here's the baseline
    for num in nums: #checks the entire list
        if num > max_so_far: #compares each list index
         max_so_far = num #updates the variable per iteration
        
    return max_so_far #return the max value after checking all indexes
print(find_max([1, 2, 300, 5, 60]))
        
  #END 

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
       if i % 2 == 1:
           odd_numbers.append(i)

    # An odd number is a number that when divided by 2, 
    #the remainder is not 0

    return odd_numbers
    #END 

def get_champion_slices(champions): #slicing practice
    return champions[3:], champions[1:4], champions[::2] #counting backwards you use [::-1]
print(get_champion_slices([11, 22, 3, 4, 555, 77, 9]))
#❔❔❔❔❔❔

# By using + you concatenate to create a new single list. Using a , would create a tuple of lists
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    newArmoryList = favorite_weapons + favorite_armor + favorite_items
    return newArmoryList
#END 

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    for wep in top_weapons:
     if weapon == wep:
         return True
     
    return False #only returns False after the loop finishes and doesn't find a match. That logic works perfectly.
#END 

def get_heroes():#using tuples
    heroes = [
        ("Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False)
    ] #unpacking tuples
    heroesName, heroesAge, isElf = heroes[0]
    print(heroesName)  #returns the contents of the entire variable unless[0] is added somewhere
                          
    #return heroes
get_heroes()
    #END 

school = ("Math", "Geography", "Gym") #a three value tuple can't be converted into two variabls
schoolSubject, schoolSubject2, _ = school
print(schoolSubject) #

#END 
def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
#END 

def get_first_item(items):
    if len(items) == 0:# 0 is always used to check if something is empty
       return "ERROR"  
    return items[0]
  #END 


def filter_messages(messages):
    filteredMessages = []
    badWordCount = []
    for mess in messages:
        words = mess.split()
        #Splits the message into words
        cleanWords = []
        counter = 0
        for w in words: #Checks each word
            if w == "dang":
                counter += 1
            else:
                cleanWords.append(w)
        sentence = " ".join(cleanWords) #Joins the clean words back into a sentence
        filteredMessages.append(sentence)
        badWordCount.append(counter)
    return filteredMessages, badWordCount #Saves both the clean sentence and the count
messages = ["Use some dang bloody sense", "dang you", "dang it all", "what if i say dang?lol"]
result = filter_messages(messages)
print(result)
filter_messages("ok")
#END 

definitions = "case1".upper() #lower() does the opposite
print(definitions)
#END 

def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    for n in numbers:
        if n % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds, num_evens

#standard test case
run_cases = [
    ([1, 7, 2, 5, 3, 4], (4, 2)),
    ([0, 99, 2, 33, 61, 44, 9, 10, 12, 240, 35, 9082, 1234], (5, 8)),
]

submit_cases = run_cases + [
    ([], (0, 0)),
    ([1, 3, 5, 7, 9], (5, 0)),
    ([2, 4, 6, 8, 10], (0, 5)),
    ([1], (1, 0)),
    ([2], (0, 1)),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (5, 5)),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_odds_and_evens(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")
test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()


run_cases = [
   
    ([2, 3, 4], (1, 2)),
]

submit_cases = run_cases + [
   ([6, 33, 92], (11, 22, 29))
]
def test(input_numbers, expected_output):
    # Print a line to separate each test
    print("---------------------------------")
    
    # Show what we're testing
    print(f"Testing with numbers: {input_numbers}")
    print(f"We expect: {expected_output}")
    
    # Run the function and get the result
    actual_result = get_odds_and_evens(input_numbers)
    print(f"We got: {actual_result}")
    
    # Check if we got what we expected
    if actual_result == expected_output:
        print("Test passed!")
        return True
    else:
        print("Test failed!")
        return False
#END 


def split_players_into_teams(players):
    even_team = players[::2]
    odd_team = players[1::2]
    return even_team, odd_team
players = (11, 22, 33, 44, 3111)#standard tuple
badPlayers = [(77.9, 44.5, 22),  (33.333, 21.0, 0, 73)]#a list of tuples
print(players[0])
print(badPlayers[0]) #prints the first tupl in the list
split_players_into_teams([9, 9.09, 9.99,  999.090])
#BLACK  FLAG

def check_ingredient_match(recipe, ingredients):
    correct = 0 #Counts matching ingredients ✓
    wrongIngredients = [] #Stores non-matching recipe ingredients in wrongIngredients ✓
    for R in range(0, len(recipe)):
        if recipe[R] == ingredients[R]: #The ingredients list is just used for comparison but never gets modified.
          correct += 1                  #any recipe items don't match theyre recycled to wrongIngredients
        else:
            wrongIngredients.append(recipe[R])
    percentage = (correct / len(recipe)) * 100 #Calculates percentage as a float ✓
    return (percentage, wrongIngredients) #Returns the correct tuple format ✓
check_ingredient_match(["pizza", "burger"], ["orange", "lime"])
#END 


def validate_path(expected_path, character_path): 
    counter = 0 #Count matches
    for R in range(0, len(expected_path)):
        if expected_path[R] == character_path[R + 1]:
           counter += 1
        #else:
            #print("There was no match")
    percentage = (counter / len(expected_path) * 100) #Calculate percentage
    print(percentage)
    return (character_path[0], percentage)#Return the result
validate_path(["A", "B", "C", "D", "E"], ["Kaladin", "A", "X", "C", "D", "E"])
#END 

def bigMove(Michigan, Japan):
  counter = 0
  miles = []
  for R in range(0, len(Michigan)):
    if Michigan[R] == Japan[R]:
      counter += 1
    else:
      miles.append(Michigan[R])
  percentage = (counter / len(Michigan) * 100)
  print(percentage) #20.0
bigMove((["8", "16", "18", "80", "800"]), (["haneda", "9", "yarp", "800", "800"]))

#END 
def double_string(string):
    emptyString = ""
    for char in string:
      emptyString += char * 2 
    return emptyString
strings = "sky diving with a parachute "
result = ""
for b in strings:
  result += b * 3
print(result) #ssskkkyyy   dddiiivvviiinnnggg   wwwiiittthhh   aaa   pppaaarrraaaccchhhuuuttteee  
#The loop is only iterating over my_word, 
#which stays the same length throughout the loop. Meanwhile, result is growing but we're not iterating over it.
#furthermore, if the print statement is inside the loop, it will print with each iteration
double_string("sky diving without a parachute")
#END 


def get_character_record(name, server, level, rank):
    getSomething = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}" #concatenates two parameters so people can't have the same name on a server
    }
    return getSomething
get_character_record("Mike", "Jesse", 74, 1)
#END 


def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict: #IF it's already in the dictionary: increment its count
         enemies_dict[enemy_name] += 1  #the bug was in the if statement. We're trying to see if we've already started 
        else:                            #counting this enemy in our dictionary. 
                                        #If we try to do enemies_dict[enemy_name] += 
                                        #1 without the enemy being in the dictionary first, we'll get a KeyError 
                                        # because we can't increment a value that doesn't exist yet
         enemies_dict[enemy_name] = 1 #IF it's not in the dictionary: add it with an initial count of 1
    return enemies_dict
count_enemies(["jackal", "kobold", "soldier"])
#END 


#where creativity mingles with logic, and mastery is born!
def nachos(burrito, tortilla):
    menuDictionary = {}
    secondary = {}
    for b in burrito:
      if b in menuDictionary:
        menuDictionary += 1
      else:
        menuDictionary[b] = 0  # Initialize the key with something before updating it
        menuDictionary[b] += 3
    for t in tortilla:   #resetting auxiliary data structures when switching loops.
      if t in secondary:
        secondary[t] += 1
      else: 
        secondary[t] = 2
        secondary[t] *= 4 #multiples 3 by the default value in this case is 2
    return menuDictionary, secondary                                    
result = nachos(
    ["cheese oz", "tomatoes oz", "onions oz", "cilantro oz", "Chili oz"],
    ["lettuce oz", "steak oz", "hot sauce oz", "beef oz"]
)
print("\nFinal Result:", result) #print out how many ounces of ingredients I will have per item in result nachos
nachos(["cheese", "bacon"], ["lettuce", "beef"])
#END 

#Iterating Over a Dictionary
def get_most_common_enemy(enemies_dict):
    findMax = float("-inf")
    countMax = None
    for R in enemies_dict:
        count = enemies_dict[R]
        if count > findMax:
            findMax = count 
            countMax = R
            print(findMax)#22, 33
            #print(countMax) prints out th key names
        else:
            print(count)
    return countMax
result = get_most_common_enemy({"test": 22, "bubble": 33})
print(result)
get_most_common_enemy("giaganic lamp")   
    
    #END 

def merge(dict1, dict2):
    merging = {}
    for key, value in dict1.items():
        merging[key] = value
    for key, value in dict2.items():
        merging[key] = value
    return merging
dict1 = {"first_quarter": 24, "second_quarter": 31}
dict2 = {"third_quarter": 29, "fourth_quarter": 40}
merged = merge(dict1, dict2) #I learned a new way to callback... I like the old way better
print(merged) 

def total_score(score_dict):
   sum = 0
   for key, value in score_dict.items():
       sum += value
   return sum
print(total_score({"third_quarter": 29, "fourth_quarter": 40}))


def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    unpurchased_items = [] #unpurchased_items appends items from pinned_list that aren't in items_purchased. It keeps track of what the player wanted but didn't buy.
    receipt = {} #receipt is a dictionary that stores the key name(item) and value (the number/price).
    total = 0 #adds up the prices of only the items that were purchased (items_purchased), not all items in item_prices
    for item in pinned_list:
        if item not in items_purchased:
          unpurchased_items.append(item)
    for item in items_purchased:
        price = item_prices[item]
        receipt[item] = price
        total += item_prices[item]
    return unpurchased_items, receipt, total
#END 


def remove_duplicates(spells):
    spellTracker = set() #Creates an empty set to track spells we've seen
    uniqueSpells = [] #Creates an empty list to store our unique spells
    conversion = spellTracker, uniqueSpells
    for s in spells: #s is the current spell
       if s not in spellTracker: #spells is the whole list and Only processes spells we haven't seen before
         spellTracker.add(s)   #Marks the current spell as "seen"
         uniqueSpells.append(s) #Adds the unique spell to our result list
    return uniqueSpells   
    #END 

#list(set(spells)) converts set and back to a list. also is a quick, concise way to remove duplicates       

def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0 #his variable tracks the total number of vowels found in the input string.
    uniqueVowels = set() #Starts as an empty set. This set will store unique vowels (not duplicated) from the input string.
    for t in text: # analyze each character individually.
        if t in vowels:
         count += 1
         uniqueVowels.add(t)
    return count, uniqueVowels
shard = count_vowels({"a", "b", "c", "A", "B", "C"})
print(shard)

def find_missing_ids(first_ids, second_ids):
    merge = set(first_ids)
    baseline = set(second_ids)
    outliers = merge - baseline
    return list(outliers)  
find_missing_ids()


#try except block
def main():
 try:
    print(get_player_record(1))
    print(get_player_record(2))
    print(get_player_record(3))
    print(get_player_record(4))
 except Exception as error:
    print(error)

#To raise an exception (raise) on its own, you don’t need a try

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


main()
#END 


#In the try block, we call get_player_record(player_id) and return its result if no error occurs.
#If an IndexError is raised (e.g. out of bounds), the except IndexError block catches it and returns "index is too high".
#For any other exception (negative player_id), the except Exception as e block catches it and returns the exception object (e).
def handle_get_player_record(player_id):
    try:
     get_player_record(player_id)
     return get_player_record(player_id)
    except IndexError:
      return "index is too high"
    except Exception as e:
      return e
concise = handle_get_player_record([1, 4, 33, 0, 77])


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

print(handle_get_player_record(0))  
print(handle_get_player_record(1))   
print(handle_get_player_record(3))   
print(handle_get_player_record(-1))  
print(handle_get_player_record(10)) 
#END 

#Unhinged Arithmetic: a cosmic tornado of data types and operations
def outerSpace(numOfStars, planetsOnSatellite):
   import math
   structure = set()
   galaxy = 0
   stars = 11
   planets = 7
   moon = 17.9
   sun = 2.100
   i = 0
   neptune = []
   mars = {}
   mars.update({"rule 1": "no cell phones", "rule 2": [22]})
   saturn = [1, 22, 2, 4, 5] #if I call this in the if statement, 2 isn't in the list anymore
   for star in numOfStars:
    if i > 3:
        break
    i +=1
    for planet in planetsOnSatellite:
      if i > 3:
        break
      i += 1
      if sun <= moon:
        sun += 22
        sun -= 100 #starts at -75.9 then jumps to 922. It's no longer a float by the second iteration 
        moon += 333                                    
        moon /= 3 
        #dividing by a larger number (10 instead of 3) would make the exponent smaller, not larger!
        #where as * would create the high numbers
        #neptune.append(sun) #BAD CODE :)
        #del moon = "UnboundLocalError: cannot access local variable 'moon' where it is not associated with a value"
      if star not in structure:
        galaxy += 100
        galaxy *= 2**4
        moon = int(moon)
        #moon = float(int(moon)) changes a converted data type into a float
        moon *= moon #interesting output: 48661191875666868481 to 2367911594760467245844106297320951247361
        sun = math.ceil(int(sun)) * 8
        sun += galaxy
        neptune.append(galaxy)
        neptune += neptune #creates a lengthy list
        return None
      elif planet not in structure:
        planets -= 1 #-=1 to -= 17 changed the outcome astronomically Final iteration: 1310722, -7077854
        planets += planets
        stars += stars * 999
        stars += star
        #stars *= stars  Exceeds the limit (4300 digits)
      else:
        stars += star
        sun += sun
        moon += moon
        galaxy += galaxy
        structure.add(galaxy) #6,990,400 then 1,118,480,000
   return stars
      
outerSpace({2, 22, 33, 55, 77}, {55, 0, .9, 46, 400})

#END 

def purchase_item(price, gold_available):
     if gold_available < price:
         raise Exception("not enough gold")
     return gold_available - price
     

def process_transactions(purchase_orders):
    leftovers = [] # this empty list was made to store successful purchases' leftover gold
    for p in purchase_orders: # Iterates over single prices and available gold from the current order
        price = p["price"]
        gold_available = p["gold_available"]
        try: # Attempts to make the purchase, If successful, it returns the remaining gold
         leftover = purchase_item(price, gold_available)
         leftovers.append(leftover) # Adds the remaining gold to our list
        except Exception as e: # If purchase fails print the error and continue without adding to the list
         print(e)
    return leftovers #return list of successful purchases' leftover gold

def main():
    print("Processing transactions...")
    leftovers = process_transactions(
        [
            {"price": 10.00, "gold_available": 125.00},
            {"price": 5.00, "gold_available": 2.00},
            {"price": 20.01, "gold_available": 5.20},
            {"price": 1.04, "gold_available": 254.00},
            {"price": 40.20, "gold_available": 6.00},
            {"price": 16.00, "gold_available": 235.01},
            {"price": 10.70, "gold_available": 10.70},
            {"price": 12.00, "gold_available": 2.30},
        ]
    )
    print("Transactions complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception(f"{gold_available:.2f} is not enough for {price:.2f}")
    return gold_available - price

main()
#END 


def number_sum(n):
    sum = 0
    for i in range(1, n + 1):
      sum += i
    return sum
number_sum(4)
  #END 

def find_min(nums):
    min = float("inf")
    for i in nums:
        if i < min:
         min = i   
    return min
    #END 

def factor(burger):
  import math
  count = math.factorial(7) #I want to make this work 
  for b in range(1, burger +1, 2): 
      count *= b
      print(count)
  return count 
factor(25)

def factor(burger):
  import math
  count = math.factorial(2) 
  i = 0
  for b in range(70, burger -1, -8): 
      count -= b
      i +=1
      if i > 7:
       break
      print(count)
  return count 
factor(-2)

#using subtraction with factorials doesn't calculate it, it becomes basic arithmetic
def factor(burger):
    if burger < 0:
        return "Cannot calculate factorial of negative numbers"
    return math.factorial(burger)
    #END 



#RANDOM Password Generator
import random as r; p = 'ibBJkKmMnNrRsuVxXyYzZ0789$:-=;[]<>?./|!@%^&*)_+'; 
print(''.join(r.choices(p, k=10)))
print(''.join(r.choices(p, k=10)))
print(''.join(r.choices(p, k=10)))
#END

#tell time
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#another way to configure time
def formatted(dateString):
    month, day, year = dateString.split("-")
    return year + month + day
    
def sort_dates(dates):
    return sorted(dates, key = formatted)
#dates.sort(key=formatted)
#return dates
#END


#common test during an interview
for i in range(1, 21): print("Fizz" * (i%3==0) + "Buzz" *(i % 5 ==0) or str(i))

def fizzbuzz(start, end):
    fbList = []
    for s in range(start, end):
        if s % 3 == 0 and s % 5 ==0: #if this isn't in the correct place, the % 3 or 5 will skip the rest of the elifs
             fbList.append("fizzbuzz") # mathematically it has to work this way because if %3 is false and %5 is false
        elif s % 3 == 0:                # then %3 and %5 will be false
             fbList.append("fizz")
        elif s % 5 == 0:
             fbList.append("buzz")
        else:
             fbList.append(s)  
    return fbList
#END 


# Happy 2100 lines of Python Code!
def pour_beer(style="IPA"): #ASCII creation
    return """
    |~~~~|
    |    |  *virtual honey ale*
    |    |
    |    |
    [____]
    """
print(pour_beer())

#END 


#this joins multiple strings as one
def join_strings(strings):
    myString = ""
    for s in strings:
         myString += s + ", " 
    if len(myString) > 0:
         myString = myString[:-2]
         print(myString)
    return myString
join_strings(["hello", "exit", "door"])

#this function puts a period on the last string
def join_strings(strings):
    myString = ""
    for i in range(len(strings)): #range can be used with strings like so
     if i == len(strings) - 1:  # if it's the last string
            myString += strings[i] + "."  # add period to last word
            print(myString)
     else:
            myString += strings[i] + ", "  # add comma and space to others
            #print(myString)
    return myString
join_strings(["hello", "exit", "door"])
#END 




    #this monitors their exp earned and records how any enemies they kill
class SOLDIER:
    def __init__(self, health, level, strength, speed, name, magic):
        self.name = name
        self.health = health
        self.level = level
        self.strength = strength
        self.speed = speed
        self.magic = magic
        self.exp = 0
        self.expToNextLevel = self.level * 20

    def display_stats(self):
        # Implement this method if it's not done yet!
        print(f"Name: {self.name}, Level: {self.level}, Health: {self.health}, "
              f"Strength: {self.strength}, Speed: {self.speed}, Magic: {self.magic}, EXP: {self.exp}/{self.expToNextLevel}")

    def battleSystem(self, enemyLevel=None):
        if self.level >= 100:
            print(f"{self.name} is already at maximum level!")
            return

        if enemyLevel is None:
            enemyLevel = self.level

        # Calculate exp based on enemy level
        enemyExp = enemyLevel * 8

        if enemyLevel > self.level:
            enemyExp *= 1.5

        print(f"{self.name} defeated a level {enemyLevel} enemy and gained {int(enemyExp)} EXP!")
        self.exp += int(enemyExp)
        self.check_level_up()

    def check_level_up(self):
        while self.exp >= self.expToNextLevel:
            self.exp -= self.expToNextLevel
            self.level += 1
            self.health += 4
            self.strength += 3
            self.speed += 1
            self.expToNextLevel = self.level * 20
            print(f"{self.name} leveled up to {self.level}")
            self.display_stats()

def VII():
 
    # Create characters
    cloud = SOLDIER(7, 1, 7, 5, "Cloud", 8)
    tifa = SOLDIER(6, 1, 6, 7, "Tifa", 4)
    
    # Battle loop
    while cloud.level < 100 and tifa.level < 100:
     enemyLevel = max(1, (cloud.level + tifa.level) // 2)
     cloud.battleSystem(enemyLevel=enemyLevel)
     tifa.battleSystem(enemyLevel=enemyLevel)
        

    print("\nFinal Stats:")
    cloud.display_stats() #displays level 100 stats
    tifa.display_stats()

VII()
#END

#create a chaining function
def phaseOne(project, endResult):
  projectBuild = phase2(project)
  staticBuild = phase2(endResult)
  print(staticBuild) #25...this is planChoice 1 and 2 added together 
  if projectBuild != 100:
    return staticBuild
  if staticBuild != 100:
    return projectBuild
  else: 
    return endResult

def phase2(plan):
    planChoice = 12
    planChoice2 = 13
    result = planChoice + planChoice2
    return result

phaseOne(17, 27)
#END 


#static variables
class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0
    #class variables are often referred to as static variables

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name #the constructor is where the employees are created
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1 #how to target class variables. class name, . , variable
        

    def get_name(self):
        return self.first_name + " " + self.last_name
#END 


#a create a library system that will allow people to add, remove, and search for books.
class Book:
    def __init__(self, title, author):
        # Initialize a new book with a title and author
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        # Initialize a new library with a name and empty book list
        self.name = name
        self.books = []

    def add_book(self, book):
        # Add a book object to the library's collection
        self.books.append(book)
        return
        
    def remove_book(self, book):
        # Loop through library books and remove the one that matches
        # both title and author of the given book
        for b in self.books:
            if book.title == b.title and book.author == b.author:
                self.books.remove(b)
        return 
        
    def search_books(self, search_string):
        # Create empty list to store matching books
        results = []
        # Loop through all books in library
        for b in self.books: 
            # Check if search string exists in book title or author
            # Convert everything to lowercase for case-insensitive search
            if search_string.lower() in b.title.lower() or search_string.lower() in b.author.lower():
                results.append(b)
        # Return list of all matching books
        return results
       #END 


# Constant values for game mechanics
fireball_damage = 500  
potion_mana = 100      
fireball_cost = 50    

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10  # Starting mana based on intelligence
        self.health = self.__stamina * 100    # Starting health based on stamina

    def cast_fireball(self, target):
        # - Check if there is enough mana to cast it
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost         
        target.get_fireballed()              
        
    def is_alive(self):
        # Check if the wizard is still alive:
        return self.health > 0

    def get_fireballed(self):
        # reduce health by fireball
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana
        #END 


#start program
#this functions like a real life bank account.
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance #creates a new account

    def get_account_number(self): #keeps record of the private acc number
        return self.__account_number

    def get_balance(self): #keeps track of the balance
        return self.__balance 

    def deposit(self, amount):#prevents faulty deposits
        if amount <= 0:       #and adds the deposit to the balance
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount
        
    def withdraw(self, amount): #prevents negative imbalances
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if amount > self.__balance: #prevents overdraft fees
            raise ValueError("insufficient funds")
        self.__balance -= amount
        #END
            

#What this does is checks students scores and grades them based on their performance
class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80 :
            return "B"
        elif score >= 70 :
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        result = self.calculate_letter_grade(score)
        self.__courses.update({course_name:result}) #updates the dictionary on line 2514
                                #basically adds a new course name and their grade

    def get_courses(self):
        return self.__courses 
#END


#this obviously is going to preform calculator functions. + - * / % ** and square root
class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
       self.__result -=  a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a): #self explanitory
        if a == 0:
            raise ValueError("cannot divide by zero")
        self.__result /= a
        
    def modulo(self, a): #self explanitory
        if a  == 0:
            raise ValueError("cannot divide by zero")
        self.__result %= a
        
    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5 

    def clear(self): #resets result
        self.__result = 0

    def get_result(self):
        return self.__result
#END



#Fire breathing Dragon
class Unit:
    def __init__(self, name, pos_x, pos_y):
        #spawns units
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2 and self.pos_y >= y_1 and
        self.pos_y <= y_2):
            #checks if the units are within striking distance of the dragon's breath
            return True
        return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
         # Initialize a dragon with unit properties and its fire range
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range #striking distance

    def breathe_fire(self, x, y, units):
        #Returns a list of all units caught within the 
        #dragon's fire breath area
        unitsHit = []
        for unit in units:
           if unit.in_area(
               x - self.__fire_range,
               y - self.__fire_range,
               x + self.__fire_range,
               y + self.__fire_range
           ):
             unitsHit.append(unit)
        return unitsHit
#END



#Operator Overload
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):

        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword('iron') #crafts two bronze sword to make an iron sword
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword('steel') #2 iron swords make a steel sword
        else:
            raise Exception("cannot craft") #cannot combine bronze with iron, etc.

#END



#target each dragon in the test cases and print their name and color
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"

run_cases = [
    (Dragon("Smaug", "red"), "I am Smaug, the red dragon"),
    (Dragon("Saphira", "blue"), "I am Saphira, the blue dragon"),
]

submit_cases = run_cases + [
    (Dragon("Nefarian", "black"), "I am Nefarian, the black dragon"),
    (Dragon("Toothless", "blackish"), "I am Toothless, the blackish dragon"),
    (Dragon("", "colorless"), "I am , the colorless dragon"),
    (Dragon("Glaurung", "gold"), "I am Glaurung, the gold dragon"),
    (Dragon("Fafnir", "green"), "I am Fafnir, the green dragon"),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Input: {input1}")
        print(f"Expecting: {expected_output}")
        result = str(input1)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
#END


#Fisher-Yates shuffle algorithm with Mega Man, clean explanations of abilities
# accompanied by a match between Mega Man vs an enemy
import random
import time

class Protoman: #enemy
    def __init__(self, health, barrier):
        self.health = health
        self.barrier = barrier
    def protoAbilities(self):#health and attacks
        protoBuster = "Proto buster base damage: 100"
        protoBusterCharged = "Charged proto buster damage: 350"
        slideAttack = "slide deals 50 damage"
        combo = [protoBuster, protoBusterCharged, slideAttack]
        random.shuffle(combo)
        print(combo)

class DrWily: #enemy
        def __init__(self, health, tech):
            self.health = health
            self.tech = tech #health and immunnity shield
            self.ElectricShieldUse = 0
            self.shieldCooldown = 15 #5 seconds of vunerablility
            self.shield_active = False  # Track if shield is currently up
            self.shield_duration = 10 

        def useElectricShield(self):#Track time since last shield activation: time.time()
            currentTime = time.time()
            time_since_shield = currentTime - self.ElectricShieldUse #subtracts the timestamp of the last shield activation
            if time_since_shield >= self.shieldCooldown: #checks cooldown time
                self.shield_active = True
                self.ElectricShieldUse = currentTime
                return True #return the results
            return False

        def take_damage(self, damage):
            # Check if shield is active and within duration period
            if self.shield_active and (time.time() - self.ElectricShieldUse) < self.shield_duration:
                return "Immune"
            self.health -= damage # If shield isn't active or has expired, take damage
            # Return message about damage taken
            return f"Took {damage} damage! Remaining health: {self.health}"

        def scientificMechanisms(self):
            electricBolt = "Shock dmg: 50" #Dr Wily's attacks
            summonRobot = "Health = 10, missile attack dmg: 200"
            electricShield = "immune for ten seconds, contact dmg: 50"
            attacks = [electricBolt, summonRobot, electricShield]
            random.shuffle(attacks)
            print(attacks)

class MegaMan: #megaman's stats and attacks 
    advancedTech = "Bio Blaster dmg: 350"
    enemies = [Protoman(400, 100), DrWily(101, 300)] #enemy stats
    def __init__(self, health, power_up):
        self.health = health
        self.power_up = power_up

    def attack(self, target, damage): #fight between MegaMan and Dr. Wily
        if isinstance(target, DrWily) and target.shield_active:
            return "Shield Immunity Active"
        target.health -= damage
        return f"Dealt {damage} damage! Target health: {target.health}"

    def blasterMods(self, scissor, fire):#for Mega Man
        self.scissor = scissor
        self.fire = fire
        water, drill, tornado, light = "water blast dmg: 80", "Drill Blast dmg: 150", "tornado dmg: 180", "Light Beam dmg: 170"
        modShift = [light, self.fire, water, drill, MegaMan.advancedTech, tornado]
        random.shuffle(modShift)
        print(modShift)

mega = MegaMan(500, "Power Boost")#creates an outside instance variable to avoid editing self.
mega.blasterMods(140, 200)   #500 hp not sure what to do with the string

proto = Protoman(400, 100)#protman's hp and barrier
proto.protoAbilities() 

doctor = DrWily(101, 300) #hp and damage in one cycle
doctor.scientificMechanisms()

print("\n=== Combat Test ===")
print(mega.attack(doctor, 50))  # Should deal damage
print("Dr. Wily activates shield!")
doctor.useElectricShield()
print(mega.attack(doctor, 50))  # Should be blocked
#END


#deck of cards
class DeckOfCards:
 
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
    ]

    def __init__(self):
        self.__cards = []  # initialize empty private list for cards
        self.create_deck() # fill deck with 52 cards
        
    def create_deck(self):
        for suit in DeckOfCards.SUITS:
            for rank in DeckOfCards.RANKS:
             self.__cards.append((rank, suit))  # add each card as (rank, suit) tuple

    def shuffle_deck(self):
        random.shuffle(self.__cards)  # randomly reorder all cards in deck

    def deal_card(self):
        if len(self.__cards) > 0:
            return self.__cards.pop()  # pop and return top card from deck
        else:
            return None  # return None if deck is empty

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
        #END


#deck of cards 2 with overloading
# Overloading is smply to compare objects with operators < > == and, or
import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card: #Creates a card with its rank and suit, and calculates their indexes
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suit_index = SUITS.index(suit)
        self.rank_index = RANKS.index(rank)
        

    def __eq__(self, other):#Returns True if both rank and suit indexes match
        if self.rank_index == other.rank_index and self.suit_index == other.suit_index:
            return True
        return False

    def __lt__(self, other):#Compares ranks first, and only compares suits if ranks are equal
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):#Same logic as __lt__ but for "greater than" comparisons
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index
   

    def __str__(self):
        return f"{self.rank} of {self.suit}"

        

#test cases
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
run_cases = [
    ("Ace", "Hearts", "Queen", "Hearts", False, True),
    ("2", "Spades", "2", "Hearts", False, True),
]

submit_cases = run_cases + [
    ("Ace", "Spades", "Ace", "Spades", True, False),
    ("3", "Diamonds", "7", "Clubs", False, False),
    ("King", "Clubs", "King", "Hearts", False, False),
    ("Queen", "Diamonds", "Jack", "Spades", False, True),
    ("10", "Hearts", "10", "Hearts", True, False),
]


def test(rank_1, suit_1, rank_2, suit_2, expected_eq, expected_gt):
    print("---------------------------------")
    print(f"Inputs: {rank_1} of {suit_1}, {rank_2} of {suit_2}")
    print("Expected:")
    print(f" * Equal: {expected_eq}")
    print(f" * Greater than: {expected_gt}")
    print(f" * Less than: {not (expected_eq or expected_gt)}")

    card_1 = Card(rank_1, suit_1)
    card_2 = Card(rank_2, suit_2)
    result_eq = card_1 == card_2
    result_gt = card_1 > card_2
    result_lt = card_1 < card_2
    print("Actual:")
    print(f" * Equal: {result_eq}")
    if result_eq != expected_eq:
        print("Fail")
        return False
    print(f" * Greater than: {result_gt}")
    if result_gt != expected_gt:
        print("Fail")
        return False
    print(f" * Less than: {result_lt}")
    if result_lt == (expected_eq or expected_gt or None):
        print("Fail")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
#END


import random
class CardGame:
    def __init__(self):
       self.deck = DeckOfCards() #Initialize the deck by creating an instance of DeckOfCards
       self.deck.shuffle_deck()
        
    def play(self):
        print("Nothing to play...")


class War(CardGame):
    def __init__(self):
        super().__init__()#Call the parent (CardGame) constructor
        self.player1_hand = [] #creatign empty player hands
        self.player2_hand = []

    def __deal_hand(self, hand):
        for i in range(5): #Deals 5 cards
            card = self.deck.deal_card()
            hand.append(card)
            
    def play(self): #after both players have 5 cards the game starts
        self.__deal_hand(self.player1_hand)
        self.__deal_hand(self.player2_hand)
        self.__battle()
        
    #test cases
    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0
        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            if len(self.player1_hand) == 0:
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()
            if len(self.player2_hand) == 0:
                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")
            if card1 > card2:
                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:
                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:
                ties += 1
                print("Tie! Both players draw a card and play again")
        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def index_of(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __cmp(self, other):
        self_suit_i = index_of(SUITS, self.suit)
        other_suit_i = index_of(SUITS, other.suit)
        self_rank_i = index_of(RANKS, self.rank)
        other_rank_i = index_of(RANKS, other.rank)
        if self_rank_i > other_rank_i:
            return "gt"
        if self_rank_i < other_rank_i:
            return "lt"
        if self_suit_i > other_suit_i:
            return "gt"
        if self_suit_i < other_suit_i:
            return "lt"
        return "eq"

    def __eq__(self, other):
        return self.__cmp(other) == "eq"

    def __gt__(self, other):
        return self.__cmp(other) == "gt"

    def __lt__(self, other):
        return self.__cmp(other) == "lt"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)


def test(seed):
    random.seed(seed)
    war = War()
    war.play()


def main():
    test(1)
    test(2)


main()
#END


#seige math...will write comments later
class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        foodForEnergy = (distance / self.efficiency) * food_price
        return foodForEnergy

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        return super().get_trip_cost(distance, food_price) + (self.load_weight * 0.01)
        

    def get_cargo_volume(self):
        return self.bed_area * 2 
        
class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
       self.cargo_volume = cargo_volume 
       super().__init__(max_speed, efficiency)

    def get_cargo_volume(self):
        return self.cargo_volume
#END



# "Handle with care" Robot for tech enthusiasts combined witg Good Programming Practices:
#Clear comments explaining the code, Meaningful variable names and organized code structure

class Machine:
    def __init__(self, power_source):
        self.power_source = power_source

class Robot(Machine): #Object-Oriented Programming: inheritence
    functions = [] #empty list soon to be filled with strings
       #Robot.functions will be shared by all Robot instances  
    def __init__(self, batteries, robot_type):
        super().__init__(power_source=batteries)
        self.type = robot_type
        self.possibleMalfunctions = [] #Each robot gets its own malfunctions list (Data Structures)
        self.instructions = {  #The safety instructions are nicely formatted with indentation
            "Takes 5 double A batteries": "batteries not included", 
            "Flammable": "don't ask why", 
            "Possible injury": "keep out of reach of children", 
            "Do not leave outside in rain": "may spontaneously combust.." 
        }
    def __str__(self): #custom string representation of Robot objects
        return f"Robot(type={self.type}, power_source={self.power_source}, functions={Robot.functions})"

       
    def manual(self):
        #Control Flow:
        if not Robot.functions:  #if list is empty
            Robot.functions.append("Built in calculator")
            self.possibleMalfunctions.append("May shutdown if overheated")
        elif len(Robot.functions) == 1: 
            Robot.functions.append("Built in AC")
            self.possibleMalfunctions.append("AC may stop workin properly. If so, carefully remove the AC unit")
        elif len(Robot.functions) == 2:  
            Robot.functions.append("Built in verbal AI assistant")
            self.possibleMalfunctions.append("Built in memory records everything you say.")
            print("Added AI assistant:", Robot.functions)
            print("Malfunctions:", self.possibleMalfunctions)
            print("FOR SAFETY:", )
            for warning, detail in self.instructions.items():
                print(f"    {warning}: {detail}")  
        else: 
            print("Please Re-read the instruction manual")

            
robot1 = Robot("battery1", "∞R") #mini-specification for what type
robot1.manual() #Robot.functions gets populated through the manual() calls.
robot1.manual() #nothing else shuld go before this
robot1.manual()

robot2 = Robot("Runs on Gasoline", "GR505")
print("\nNew Robot2:")
print(robot2)
#END
        

class Jenova: # Base class for project management and resource tracking
    def __init__(self, project, data): # Initialize with project cost and project data
        self.project = project
        self.data = data
    def supplyCost(self, materials, other):
        #Calculate remaining budget after accounting for expenses
        budget = 7500
        finalCost = (materials + self.project) * other
        result = budget - finalCost
        return result
    def timeConstraints(self):
        # Empty method to be overridden by sub classes
        # This is a form of polymorphism - creating a common interface
        pass


class Research(Jenova):  #Specialized class for research-specific functionality, inherits from Jenova

    NE = ["hysteria", "loss of memory", "uncommunicative", "enlarged lungs"]
    PE = ["increased strength", "faster healing", "enhanced focus", "improved stamina"]

    def __init__(self, cells, positiveEffects, negativeEffects, project, data):
        # Initialize the parent class with project and data
        super().__init__(project, data) #self should never be passed in super. 
        self.cells = cells
        self.sideEffects = positiveEffects 
        self.negativeEffects = negativeEffects

    def calculate_severity(self, effect):
       # Map each negative effect to its severity level
       severity_map = { 
          "hysteria" : "high",
          "enlarged lungs": "high",
          "loss of memory" : "medium",
          "uncommunicative": "medium"
       }
       return severity_map.get(effect, "low") # Default to "low" if effect not found
   
    def compare_results(self):
        results = []  

    
        for effect in self.NE:
            severity = self.calculate_severity(effect) 
            if severity == "high":
                results.append(f"WARNING: {effect} is severely negative")
            else:
                results.append(f"{effect} is under control")

    
        for effect in self.PE:
            if self.sideEffects > self.negativeEffects:  
                results.append(f"{effect} is active and beneficial")
            else:
                results.append(f"{effect} is suppressed")
    
        return results  
    

    def supplyCost(self, materials, other): 
        base_result = super().supplyCost(materials, other)
        energyCosts = (materials + self.negativeEffects) * other
        labFees = self.cells * 10
        total = base_result + labFees + energyCosts
        return total
    
    def timeConstraints(self):
         
        baseTime = self.sideEffects * 3  
        extraTime = 0 #starts at 0
        for effect in self.NE:
           severity = self.calculate_severity(effect)
           if severity == "high":
              extraTime += 15  
           elif severity == "medium":
              extraTime += 5  

        if self.sideEffects > self.negativeEffects:
           baseTime -= 10
        return baseTime      

class Final_Results(Research): #what can I do to make these final results contribute to the rest of the code?
    def __init__(self, cells, positiveEffects, negativeEffects, project, data, malfunctions):
        super().__init__(cells, positiveEffects, negativeEffects, project, data)
        self.malfunctions = malfunctions 
        

    def timeConstraints(self):
        base_time = super().timeContraints()
        return base_time + (self.malfunctions * 3)

project_instance = Jenova(1000, "Some_Data")
result = project_instance.supplyCost(100, 2)
print(f"Budget remaining: {result}")

research_instance = Research(50, 10, 2, 1000, "Research_Data")
effects = research_instance.compare_results()
for result in effects:
    print(result)
    #END


#a string converted to a tuple
def add_prefix(document, documents):
     if isinstance(documents, str):
        documents = (documents,)
     if isinstance(document, str):
        document = (document,)

     prefix = f"{len(documents)}. "
     if document:
        new_doc = (prefix +  document[0],) + document[1:]
     else: 
        new_doc = ()

     return documents + new_doc
result = add_prefix(("document", "funds"), ("I put the docuemnts in the paper shredder to annoy my boss lol",))
print(result)
    #END


    #clever index trick to find even and odd numbers. or the smallest of comparable numbers
def get_median_font_size(font_sizes):
        result = sorted(font_sizes)
        smallestNum = (len(result)-1) //2 #Floor division divides and then rounds down to the nearest integer.
        if len(result) > 0 : #len should always be used to check the contents of a list 
            return result[smallestNum]   #you can also use "if not parameter:"
        return None

print(get_median_font_size([13, 12, 15, 16, 777, 320, 99, 65, 43, 101, 3343]))
#65 becomes the fifth index after being sorted
#END


class Colorado:
   aspen = ["high crime"]
   def __init__(self, miles):
      self.miles = miles
 
   def xyz(self, problems):
        x = 175
        y = 909
        z = 708
        q = ["high tide"]
        Colorado.aspen.append(q)
        print(Colorado.aspen)
        if x <= y:
           x *= x * z + y * y / problems #69882225.0
           print(f"x equals:{x}")
        elif y <= z:
           y +=y / x * x - z
           print(y)
        elif z <= x:
           z *= z + z + x / y
        else:
           return None
        return x, y, z
   
c = Colorado(10)#defines miles
result = c.xyz(3) # class call and calling instanced within that class
print(f"here's the results of x, y, and z: {result}")
#END


#class practice
what = (4444,)
when = 1222
how = {"hard work": "perseversence",
       "skill":"brain training",
       "relaxation": "sleep time"
       }
why = [12, 12, 12, 14, 44]
wackyTaffy = [23.0, 23.4, 7, 88.9, 11, 978, 22, 2.2]

class Infrastructure:
   def __init__(self, production, cloudDev):
       self.production = production
       self.cloudDev = cloudDev
   def newTask(self, job):
       self.job = job
   def machine(self):
       global what
       global when
       global how
       global why
       global wackyTaffy
       what = list(what) #Convert to list, modify, convert back
       what.append(33)
       what = tuple(what)
       #what = what + (33,) #Create new tuple by concatenation
       when += when**8
       how.update({"most used tool":"SQL"})
       why.append([33, 44, 55])
       print(sorted(why))
       wackyTaffy.sort()

class secondPhase(Infrastructure):
    #When you use super(), you're often trying to either call the constructor 
    #or extend an existing method from the parent.
    def __init__(self, production, cloudDev): 
       
        super().__init__(production, cloudDev)#targets parent constructors
        super().machine() #target specific classes
    def results(self):
       input = 707
       output = 200
       test = "change data type"
       doNotChange = 22.999
       tabMeIn = ("logged in", "give me a prize!")
       ilovecoding = [2, 3, 4, 55, 60, 303, 310, 3223, 33, 99, 400, 481, 787, 19.00]
       ilivetocode = [2, 3, 4, 55, 60, 303, 310, 3223, 33, 99, 400, 481, 787, 19.00]
       ifinetunecode = [9, 10, 7.7, 333, 4007, 2.02, 56.56, 101, 994, 553, 91.10]
       for i in range(0, len(ilovecoding), 10):
          print(ilovecoding)
          print(i)

       for l, indexes in enumerate(ilivetocode):
          print(ilivetocode[l])
    
       for f in ifinetunecode:
          print(ifinetunecode[0:13:2])
          
       if input > output:
          input += input * output ** 17
          print(input)
          return tabMeIn
       elif input > doNotChange //2:
          doNotChange += input * output * 7 **7
          print(doNotChange)
       else:
          pass 
       return ilovecoding, ilivetocode, ifinetunecode 

class architect(secondPhase):
   def __init__(self, stuff, production, cloudDev):
    super().__init__(production, cloudDev)  #for super to get parent elements, the subclass constructor must include them
    self.stuff = stuff         
        
   def starsInTheSky(self): #cosmic scale thinking
      counter = 1
      measurement1 = 30388
      measurement2 = 404
      stars = 2 * 10 **22
      blackHoles = "???"# if string values don't have a numeric value an error will occur
      strangeFinding = float(counter)
      newDiscovery = set(blackHoles)
      if measurement1 % 2 == 0:
         counter += 2 **11 + measurement2
         stars *= 2
         print(counter)
         print(stars)
      else: 
         pass

ii = Infrastructure(22, 22) 
sp = secondPhase(10, 10)
a = architect(12, 3, 44)
#END


#figure out how to user capitalize(), upper(), strip(), rstrip(), lstrip(), replace("", "")
def format_line(line):
    egg = "You will      give me an egg  !" #strings are immutable, so you need to assign this result to egg
    egg = egg.replace("i", "b").replace(" ", "").upper().strip()
    egg = ' '.join(egg.split()) #incase of more than 3 spaces apart.
    print(egg)
    return f"{line.strip().upper().replace('.', '')}..."
print(format_line("I forgot the test file."))
#END


def deduplicate_lists(lst1, lst2, reverse=False):

        newList = set(lst1 + lst2)#merge
    
        return sorted(newList, reverse = reverse)
#sorts the deduplicated elements in descending order when reverse=True
#END


def file_type_getter(file_extension_tuples):
    dict = {}
    for f in file_extension_tuples:# f is a tuple like ("document", [".doc", ".docx"])
        type = f[0]
        extensions = f[1]
        for x in extensions: # loop through the extensions list
            dict[x] = type
    return lambda q: dict.get(q, "Unknown")# Return lambda that looks up extensions and returns "Unknown" if not found
#END


#map()
def change_bullet_style(document):
    newLine = document.split("\n")
    conversion = map(convert_line, newLine)
    #how map works: The first argument is the function to apply (which is convert_line in our case)
#The second argument is the iterable (which is our list of lines)
    return "\n".join(conversion)

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
#END


#zip
valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

def pair_document_with_format(doc_names, doc_formats):
    docx = list(zip(doc_names, doc_formats))
    newFolder = list(filter(lambda x: x[1] in valid_formats, docx))
    return newFolder
#END


#this is a pure function. anything that doesn't use global variables.
def convert_file_format(filename, target_format):
    current_format = filename.split(".")[-1]
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    
    valid_conversions = {
    "docx": ["pdf", "txt", "md"],
    "pdf": ["docx", "txt", "md"],
    "txt": ["docx", "pdf", "md"],
    "pptx": ["ppt", "pdf"],
    "ppt": ["pptx", "pdf"],
    "md": ["docx", "pdf", "txt"],
}
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None
#END


#No-op: an operation that does nothing.
def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    words = map(remove_emphasis_from_word, line.split())
    return " ".join(words)
    

def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    updatedLines = map(remove_emphasis_from_line, lines)
    return "\n".join(updatedLines)
#END

#Memoizaton
def word_count_memo(document, memos):
    newMem = memos.copy()
    if document in newMem:
        return newMem[document], newMem

    count =  word_count(document)
    newMem[document] = count
    return count, newMem


def word_count(document):
    count = len(document.split())
    return count
#END


#custom commands
default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}


def add_custom_command(commands, new_command, function):
    newCommand = commands.copy()
    newCommand[new_command] = function
    return newCommand


def add_format(formats, format):
    newList = formats.copy()
    newList.append(format)
    return newList


def save_document(docs, file_name, doc):
    newDoc = docs.copy()
    newDoc[file_name] = doc
    return newDoc


def add_line_break(line):
    newLine = line + "\n\n"
    return newLine
#END


#organizing keywords
def map_keywords(document, document_map):
    newMap = document_map.copy()#Make a copy of the document_map
    if document in newMap:#Check if the document exists in the copy
        return newMap[document], newMap #If it exists, return the keywords from the copy (not the original)
    found_keywords = find_keywords(document)
    newMap[document] = found_keywords #If it doesn't exist, add it to the copy (not the original)
    return found_keywords, newMap #return the found keywords and the copy


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
]
    searchCase = document.lower()
    return list(filter(lambda x: x.lower() in searchCase, keywords))
   #END


#recursive practice
def zipmap(keys, values):
    result = {}
    if len(keys) == 0 or len(values) == 0:
        return result
    result = zipmap(keys[1:], values[1:])
    result[keys[0]] = values[0]
    return result
    #END


#Tree recursion
def list_files(parent_directory, current_filepath=""):
    filePath = [] #You create an empty list to store the file paths
    for i in parent_directory: #You loop through each key in the parent directory
        outputPath = current_filepath + "/" + i
        #You properly construct the new path by concatenating the current path, a slash, and the key
        
        if parent_directory[i] is None: #For files (where the value is None), you add the path to your list
            filePath.append(outputPath)
        else: #For directories, you recursively call the function and extend your list with the results
            filePath.extend(list_files(parent_directory[i], outputPath)) 
    return filePath #return the complete list
#END

#count nested levels
def count_nested_levels(nested_documents, target_document_id, level=1):
    for id in nested_documents:
        if id == target_document_id:
            return level
        if nested_documents[id]:
            foundLevel = count_nested_levels(nested_documents[id], target_document_id, level + 1)
            if foundLevel != -1:
                return foundLevel
    return -1  
#END

#recursve string reversal
def reverse_string(s):
      if len(s) == 0:
          return s
      else:
          return reverse_string(s[1:]) + s[0]
       #END

def find_longest_word(document, longest_word=""):
    if len(document) == 0:#base case runs through
        return longest_word
    words = document.split(maxsplit=1) #splits the document into two files

    if len(words) < 1:#defensive check to handle empty documents w/whitespace
        return longest_word
    first_word = words[0] #gets the first word from split
    if len(first_word) > len(longest_word):#checks if this word is longer than longest
        longest_word = first_word
    if len(words) < 2: #base case: if there's only one word left return the current longest
        return longest_word
    return find_longest_word(words[1], longest_word)#recursive call with the rest of the document
#recursion is similar to a for loop:
#The function calls itself from within itself. so long as it has a base case you won't get an infinite reccursion
#Thus creates multiple function calls on the call stack
def find_longest_word_loop(document):
    longest_word = ""
    words = document.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

#END


#function transformation
def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))
    return logger


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
#END


#filter commands
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
       if option == "--one":
           return filter_one(content)
       if option == "--two":
           return filter_two(content)
       if option == "--three":
           filtered_content = filter_one(content)
           return filter_two(filtered_content)
       else:
           raise Exception("invalid option")


    return filter_cmd


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
#END


#upgrade filter command
def get_filter_cmd(filters):
    def filter_cmd(content, options, word_pairs):
        if not len(options):#We check if options is empty at the beginning
            raise Exception("missing options")
        result = content#We initialize a result variable with the original content

        for option in options:
            if option in filters:#For each option, we check if it exists in filters
                result = filters[option](result, word_pairs)#If it does, we apply the filter function to our current result
            else:
                raise Exception("invalid option")
        return result
    return filter_cmd
        

def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content


def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content


def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))


def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content


filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}
#END


#Closures
def word_count_aggregator():
    count = 0
    def counter(word):
        nonlocal count
        newString = len(word.split())
        count += newString
        return count
    return counter
#END


#copy/paste 
def new_clipboard(initial_clipboard):
    copyCat = initial_clipboard.copy()
    def copy_to_clipboard(key, value):#correctly takes a key and value and adds them to your copy of the clipboard.
        nonlocal copyCat
        copyCat[key] = value
    def paste_from_clipboard(key):#correctly checks if a key exists in the clipboard
        if key in copyCat:
            return copyCat[key]
        else:
            return ""
    return copy_to_clipboard, paste_from_clipboard
#END


#user words
def user_words(initial_words):
    clown_words = initial_words
    def add_word(word):
        nonlocal clown_words
        #adding the new word to the end of the tuple 
        clown_words = clown_words + (word,)
        return clown_words
    return add_word
#END


    #Line breaking
def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            
            if len(lines) == 0:
                return [word]
            current_line = lines[-1]
            if len(current_line) + len(word) +1 > line_length:
                lines.append(word)
            else:
                lines[-1] = current_line + " " + word
            return lines
            

        return reduce(add_word_to_lines, words, [])

    return lineate
#END


#currying: how currying works - you're breaking a multi-parameter function into a chain of single-parameter functions.
def converted_font_size(font_size):
    def innerFunction(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return innerFunction


#More currying practice
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        counter  = 0
        def with_length(doc):
            doctype = doc.split("\n")
            nonlocal counter
            for d in doctype:
                if sequence in d:
                    counter += 1
            return counter
        return with_length

    return with_char
#END


#ow reduce works
from functools import reduce
def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


def create_html_table(data_rows):
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))

    def create_table_headers(headers):
        nonlocal rows
        header_cells = accumulate_headers(headers)
        header_row = tag_row(header_cells)
        rows = header_row + rows
        table = tag_table(rows)
        return table
    return create_table_headers
#END

#resizing image
def new_resizer(max_width, max_height):
    def inner(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
                raise Exception("minimum size cannot exceed maximum size")
        def innerSanctum(width, height):
            newWidth = min(max(width, min_width), max_width)
            newHeight = min(max(height, min_height), max_height)
            return newWidth, newHeight
        return innerSanctum
    return inner
#end


#decorator
def file_type_aggregator(func_to_decorate):
    counts = {}
   

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

@file_type_aggregator
def process_doc(doc, file_type):
    process = f"Processing doc: '{doc}'. File Type: {file_type}"
    return process
#end



#configure plugin
def configure_plugin_decorator(func):
    def wrapper(*args):
        argsConversion = dict(args)#correctly converts *args (a tuple of key-value pairs) into a dictionary
        functhewrapper = func(**argsConversion)#called with the unpacked dictionary,
        return functhewrapper
    return wrapper
#end

#escape html
def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            result = text.replace(old, new)
            return decorated_func(result)
        return wrapper
    return replace

@replacer("&", "&amp;")  
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
#end


#lrucache
from functools import lru_cache

@lru_cache
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
#end





#Export CSV
from enum import Enum
Doctype = Enum('Doctype', ['PDF','TXT', 'DOCX', 'MD', 'HTML'])

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            processed_data = list(map(lambda row: list(map(str, row)), data))
            return "Pending...", processed_data
        case CSVExportStatus.PROCESSING:
            csv_string = "\n".join(map(lambda row: ",".join(row), data))
            return "Processing...", csv_string
        case CSVExportStatus.SUCCESS:
            return "Success!", data
        case CSVExportStatus.FAILURE:
            prepared_data = list(map(lambda row: list(map(str, row)), data))
            csv_string = "\n".join(map(lambda row: ",".join(row), prepared_data))
            return "Unknown error, retrying...", csv_string
        case _:
            raise Exception("unknown export status")
#end





def newline(document, line_number):
    lines = document.split("\n")
    line = lines[line_number]#specific line to modify
    lines[line_number] = line + "\n" #new line to the end of the line
    return "\n".join(lines) #joins all the lines w/ newlines between
def substitute(document, insert_text, line_number, start, end):
    lines = document.split("\n")
    line = lines[line_number]
    #Modifies that line by taking everything before start, adding the insert_text, 
    #and then adding everything after end
    lines[line_number] = line[:start] + insert_text + line[end:]
    return "\n".join(lines)
    
def insert(document, insert_text, line_number, start):
    #code reuse
    return substitute(document, insert_text, line_number, start, start)
    
def delete(document, line_number, start, end):
    return substitute(document, "", line_number, start, end)
    #END



from typing import List, Dict
class Dinner:
    def __init__(self, meat: str, vegetables: List[str]):
        self.meat = meat
        self.vegetables = vegetables

    def get_menu(self) -> str:
        return f"Main: {self.meat}\nSides: {', '.join(self.vegetables)}"

    @staticmethod
    def carrot_juice(sugar: str, vitamin_c: str) -> str:
        sugar_cleaned = "".join(filter(str.isalpha, sugar))
        vitamin_words = vitamin_c.split(maxsplit=1)

        if len(sugar_cleaned) > len(vitamin_words[0]):
            return f"Double juice: {vitamin_c + ' ' + vitamin_c}"
        else:
            return f"Filtered sugar: {sugar_cleaned}"


class Lunch(Dinner):
    def __init__(self, meat: str, vegetables: List[str], fruits: List[str]):
        super().__init__(meat, vegetables)
        self.fruits = fruits

    def shopping_list(self) -> Dict[str, List[str]]:
        extras = ["tabasco sauce", "pepper", "salt"]
        fruit_basket = [f for f in self.fruits if f.startswith("b")]
        return {
            "vegetables": self.vegetables,
            "fruits_starting_with_b": fruit_basket,
            "extras": extras
        }
#END


def simpleProblem(num_list, divisor):
   
   result = []
   for num in num_list:
     if num % divisor == 0:
           print(f"{num} is divisible by {divisor}")
           result.append(num)
     else:
           print(f"{num} is not divisible by {divisor}")
   return result

divisor_beta = [5, 12, 19, 28, 302, 303]    
divisor_alpha = 5
results = simpleProblem(divisor_beta, divisor_alpha) 
print(results)
simpleProblem([5, 12, 19, 27, 28, 302, 303, 305], 2)
#end


def building(infrastructure, budget): #time complexity: O(n * m)
   #if the list is large, print output may become lengthy as it scales with input size
   result = []
   for i in range(len(infrastructure)):
      for b in budget: 
       if i > 0 or b > 0: #to have elif and else blocks reached consider checking the order before executing them
            result.append(i + infrastructure[i])
       elif i > 4 or b > 4:
            print("Out of Range")
       else:
            break
   print(result)
   return result
building([7, 1, 2, 8], [23, 23, 23, 24])


#logarithms
import math
def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)
#logarithmic scale
import math
def log_scale(data, base):
    #return [math.log(x, base) for x in data] (list comprehension)
    result = []
    for i in data:
        result.append(math.log(i, base))
    return result


#exponents
def get_estimated_spread(audiences_followers):
   
    if audiences_followers == []:
         return 0
    num_followers = len(audiences_followers)
    average = sum(audiences_followers) / num_followers
       
    return average * (num_followers ** 1.2)
#end

#growing exponents
def get_follower_prediction(follower_count, influencer_type, num_months):
      total = 0
      if influencer_type == "fitness":
          total = follower_count * (4 ** num_months)
      elif influencer_type == "cosmetic":
          total = follower_count * (3 ** num_months)
      else:
          total = follower_count * (2 ** num_months)
      return total


#find average
def average_followers(nums):
    average = 0
    if nums == []:
        return None
    for num in range(len(nums)) :
        average += nums[num]
        
    return average / len(nums)
#END

#find minimum
def find_minimum(nums):
    minimum = float("inf")
    if not nums:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
find_minimum([])      



#TIME COMPLEXITY AND RECURSION
# Example of 0(n):
def sum_list_opt(n, i=0):
   if i == len(n):
      return 0
   return n[i] + sum_list_opt(n, i +1)
print(sum_list_opt([1, 2, 3, 4, 5]))

def find_max(nums):
    maxNum = -float("inf")
    
    for i in nums:
        if i > maxNum:
            maxNum = i
    return maxNum
#end

def popSum(n): #time complexity is Order(n), space complexity is O(n) due to recursion depth
   #each recursive call adds a frame to the call stack
   if not isinstance(n, list):
      raise TypeError("popSum expects a list")
   if len(n) <= 1:
      return 0
   return n.pop() + popSum(n)
n = [17, 12, 17, 5, 7]
print(f"Before pop(), {n}, \n"
      f"Result of n + popSum(n): {popSum(n)}, \n"
      f"after pop(): {n}")
print(popSum([1, 2]))

def factorial(n):
   if n == 0 or n == 1:
      return 1 #base case
   else:
      return n * factorial(n-1) #recursion case
4 * factorial(3)#mentor loves laying out the call chain. chef's kiss
3 * factorial(2)
2 * factorial(1)
result = 2 * 1, 3 * 2, 4 * 6
print(factorial(6))
#120 for factoial(5) 720 for factorial(6)
#END

# O(n^2)
def does_name_exist(first_names, last_names, full_name):
    for i in first_names:
        for l in last_names:
            if i + " " + l in full_name:
                return True
    return False

# O(nm)
def get_avg_brand_followers(all_handles, brand_name):
    average = 0
    for i in range(len(all_handles)):
        for j in all_handles[i]:
            if brand_name in j:
                average = average + 1
    return average / len(all_handles)


    
#difference between O(log(n)) vs O(n) psuedo code. order(n*2)(squared)
#don't be fooled by list... it could be a parameter
def antiCode(n, target):
   low = 0
   high = n-1
   while low <= high:
      median = math.log(low, high) // 2
      if list[median] == target:
         return True
      elif list[median] < target:
         low = median + 1
      else:
         high = median -1
   return False


#sorting algorithms
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

def vanity(influencer):
    result = influencer.num_bio_links * 5
    result += influencer.num_selfies
    return result
    
def vanity_sort(influencers):
    return sorted(influencers, key=vanity)
#end


#bubble sort. data should be sorted first to avoid O(n^2)
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1, end, 1):
            if nums[i-1] > nums[i]:
                list = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = list
                swapping = True
        end -= 1
    return nums
                
                
        
#merge sort. time complexity: O(n*log(n))
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    return merge(first, second)
    
def merge(first, second):
    result = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    
    while i < len(first):
       result.append(first[i])
       i += 1
    
    while j < len(second):
       result.append(second[j])
       j += 1
    return result


#insertion sort. O(n) if one comparison per element, O(n2) if in reverse
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

#quick sort example. better then bubble sort and merge sort, however
# may reach O(n*2) complexity, merge sort is more stable
#try the median approach and random approach
def quick_sort(nums, low, high):
    if low < high:
        pivot_i = partition(nums, low, high)
        quick_sort(nums, low, pivot_i -1)
        quick_sort(nums, pivot_i +1, high)
        
def partition(nums, low, high):
    pivot = nums[high]
    i = low -1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

#selection sort
def selection_sort(nums):
    smallest_idx = 0
    for i in range(len(nums) -1):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums

#polynominal time
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent = 0
    parent = 1
    current = 0
    for i in range(n-1): #polynominal time O(n)
       current = parent + grandparent 
       grandparent = parent
       parent = current
    return current
    
    #exponential time :( return fib(n - 1) + fib(n - 2)


#O(n^2) exponetial time
def power_set(input_set):
    
    if not input_set:
        return [[]]
    all_subsets = [[]]
    for i in input_set:
        
        subsets_with_elements = []
        for j in all_subsets:
            new_subset = j + [i]
            subsets_with_elements.append(new_subset)
        all_subsets.extend(subsets_with_elements)
    #all_subsets.sort(key=lambda x: - len(x))
    return all_subsets





#linear probing
class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
 




#find matches
class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


#longest common prefix
class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key == self.end_symbol:
                    break
                children.append(key)
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
    
      


#graphs
class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
     



#depth first search
class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)


    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result



#traveling salesman problem
def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


#verify solutions
def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i + 1)
    return total


#prime factorization
import math
def prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        n /= 2
        prime_factors.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors



#subset sub problem
def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    res = find_subset_sum(nums, target, index - 1)
    res2 = find_subset_sum(nums, target - nums[index], index - 1)
    return res or res2


#MORE ADVANCED PYTHON METHODS----------
#REVIEW OF GRAPHS
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])





#DIJKSTAS FULL CODE
def dijkstra(graph, src, dest):
    unvisited = set()
    predecessors = {}
    distances = {}
    for node in graph:
        unvisited.add(node)
        if node == src:
            distances[node] = 0
        else:
            distances[node] = float("inf")

    while len(unvisited) > 0:
        min_dist_node = get_min_dist_node(distances, unvisited)
        unvisited.remove(min_dist_node)

        if min_dist_node == dest:
            return get_path(dest, predecessors)

        for neighbor in graph[min_dist_node]:
            if neighbor not in unvisited:
                continue
            distance_so_far = distances[min_dist_node]
            distance_to_neighbor = graph[min_dist_node][neighbor]
            total_distance_to_neighbor = distance_so_far + distance_to_neighbor
            if total_distance_to_neighbor < distances.get(neighbor):
                distances[neighbor] = total_distance_to_neighbor
                predecessors[neighbor] = min_dist_node


def get_path(dest, predecessors):
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


def get_min_dist_node(distances, unvisited):
    min_dist = float("inf")
    min_dist_node = None
    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            min_dist_node = v
    return min_dist_node



#PRIORITY QUEUE CODE
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]



#POP
class MinHeap:
    def pop(self):
        if len(self.elements) == 0:
            return None

        if len(self.elements) == 1:
            return self.elements.pop()

        root_value = self.elements[0]
        self.elements[0] = self.elements.pop()
        self.bubble_down(0)

        return root_value

    def bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        min_index = index

        if (
            left_child_index < len(self.elements)
            and self.elements[left_child_index][0] < self.elements[min_index][0]
        ):
            min_index = left_child_index

        if (
            right_child_index < len(self.elements)
            and self.elements[right_child_index][0] < self.elements[min_index][0]
        ):
            min_index = right_child_index

        if min_index != index:
            self.elements[index], self.elements[min_index] = (
                self.elements[min_index],
                self.elements[index],
            )
            self.bubble_down(min_index)


    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        parent_priority = self.elements[parent_index][0]
        index_priority = self.elements[index][0]
        if parent_priority > index_priority:
            self.elements[parent_index], self.elements[index] = (
                self.elements[index],
                self.elements[parent_index],
            )
            self.bubble_up(parent_index)

    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0][1]

   

 


#A * CODE
import random


def heuristic(next, dest):
    return abs(next.x - dest.x) + abs(next.y - dest.y)


def a_star_search(traffic_grid, src, dest):
    queue = PriorityQueue()
    queue.push(0, src)
    predecessors = {src: None}
    costs = {src: 0}
    visited = set()
    while not queue.empty():
        current = queue.pop()
        if current == dest:
            break
        if current in visited:
            continue
        visited.add(current)
        for next in traffic_grid.neighbors(current):
            next_cost = costs[current] + next.cost()
            if next not in costs or next_cost < costs[next]:
                costs[next] = next_cost
                priority = next_cost + heuristic(next, dest)
                queue.push(priority, next)
                predecessors[next] = current
    path = []
    pred = dest
    while pred != None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path



class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        bucket = random.randint(1, 2)
        cost = random.randint(1, 5)
        if bucket == 2:
            cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        else:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s



#FAST FIBONACCI MEMOIZATION
def fibonacci(n, precomputed={}):
    if n not in precomputed:
        if n == 0:
            precomputed[n] = 0
        elif n == 1:
            precomputed[n] = 1
        else:
            precomputed[n] = fibonacci(n - 1, precomputed) + fibonacci(
                n - 2, precomputed
            )
    return precomputed[n]


#FAST FIBONACCI TABULATION
def fibonacci(n):
    fib_arr = [None] * (n + 1)
    fib_arr[0] = 0
    if n > 0:
        fib_arr[1] = 1

    for i in range(2, n + 1):
        fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]

    return fib_arr[n]


#SLOW EDIT DISTANCE
def edit_distance(str1, str2):
    if str1 == "":
        return len(str2)

    if str2 == "":
        return len(str1)

    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])

    return 1 + min(
        edit_distance(str1, str2[:-1]),  # insert
        edit_distance(str1[:-1], str2),  # remove
        edit_distance(str1[:-1], str2[:-1]),  # substitute
    )

#dynamic arrays

#DYNAMIC PROGRAMMING EDIT DISTANCE
def edit_distance(str1, str2):
    table = []
    for _ in range(0, len(str1) + 1):
        row = []
        for _ in range(0, len(str2) + 1):
            row.append(0)
        table.append(row)

    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if i == 0:
                table[i][j] = j

            elif j == 0:
                table[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1]

            else:
                table[i][j] = 1 + min(
                    table[i][j - 1],
                    table[i - 1][j],
                    table[i - 1][j - 1],
                )
    return table[-1][-1]



#ALGORITHM FOR SOLVING LP PROBLEMS
class SimplexSolver:
    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)


#SIMPLEX TABLEAU SLACK VARIABLES
class SimplexSolver:
    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)


#TABLEAU SOLUTION
class SimplexSolver:
    def get_solution_from_tableau(self):
        cols = []
        for colI in range(len(self.rows[0])):
            col = [0] * len(self.rows)
            for rowI in range(len(self.rows)):
                col[rowI] = self.rows[rowI][colI]
            cols.append(col)

        results = []
        for i in range(len(cols) - 1):
            if cols[i].count(0) == len(cols[i]) - 1 and 1 in cols[i]:
                results.append(cols[-1][cols[i].index(1)])
            else:
                results.append(0)
        return results, self.objective[-1]


    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)


#PIVOTING THE TABLEAU AND WHEN TO STOP
class SimplexSolver:
    def should_pivot(self):
        return min(self.objective[:-1]) < 0

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)


#FINDING THE PIVOT COLUMN
class SimplexSolver:
    def get_pivot_col(self):
        low = 0
        pivot_idx = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[i]
                pivot_idx = i
        return pivot_idx

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)


#FINDING THE PIVOT ROW
class SimplexSolver:
    def get_pivot_row(self, col_idx):
        last_col = [self.rows[i][-1] for i in range(len(self.rows))]
        pivot_col = [self.rows[i][col_idx] for i in range(len(self.rows))]
        min_ratio = float("inf")
        min_ratio_idx = -1
        for i in range(len(last_col)):
            ratio = float("inf")
            if pivot_col[i] != 0:
                ratio = last_col[i] / pivot_col[i]
            if ratio < 0:
                continue
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_idx = i
        if min_ratio_idx == -1:
            raise Exception("no non-negative ratios, problem doesn't have a solution")
        return min_ratio_idx


    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def get_pivot_col(self):
        low = 0
        pivot_idx = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[-1]
                pivot_idx = i
        return pivot_idx

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)


       
  #SOLVING THE WHOLE SIMPLEX
class SimplexSolver:
    def solve(self):
        self.add_slack_variables()
        while self.should_pivot():
            c = self.get_pivot_col()
            r = self.get_pivot_row(c)
            self.pivot(r, c)


    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def get_pivot_col(self):
        low = 0
        pivot_idx = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[i]
                pivot_idx = i
        return pivot_idx

    def get_pivot_row(self, col_idx):
        last_col = [self.rows[i][-1] for i in range(len(self.rows))]
        pivot_col = [self.rows[i][col_idx] for i in range(len(self.rows))]
        min_ratio = float("inf")
        min_ratio_idx = -1
        for i in range(len(last_col)):
            ratio = float("inf")
            if pivot_col[i] != 0:
                ratio = last_col[i] / pivot_col[i]
            if ratio < 0:
                continue
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_idx = i
        if min_ratio_idx == -1:
            raise Exception("no non-negative ratios, problem doesn't have a solution")
        return min_ratio_idx

    def pivot(self, pivot_row_idx, pivot_col_idx):
        pivot_val = self.rows[pivot_row_idx][pivot_col_idx]
        for i in range(len(self.rows[pivot_row_idx])):
            self.rows[pivot_row_idx][i] = self.rows[pivot_row_idx][i] / pivot_val
        for i in range(len(self.rows)):
            if i == pivot_row_idx:
                continue
            mul = self.rows[i][pivot_col_idx]
            for j in range(len(self.rows[i])):
                self.rows[i][j] = self.rows[i][j] - mul * self.rows[pivot_row_idx][j]
        mul = self.objective[pivot_col_idx]
        for i in range(len(self.objective)):
            self.objective[i] = self.objective[i] - mul * self.rows[pivot_row_idx][i]

    def should_pivot(self):
        return min(self.objective[:-1]) < 0

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)

    def get_solution_from_tableau(self):
        cols = []
        for colI in range(len(self.rows[0])):
            col = [0] * len(self.rows)
            for rowI in range(len(self.rows)):
                col[rowI] = self.rows[rowI][colI]
            cols.append(col)

        results = []
        for i in range(len(cols) - 1):
            if cols[i].count(0) == len(cols[i]) - 1 and 1 in cols[i]:
                results.append(cols[-1][cols[i].index(1)])
            else:
                results.append(0)
        return results, self.objective[-1]
