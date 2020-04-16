import time
import random
'''
from twilio.rest import Client

account_sid = 'AC751f6b64a9a84b96c57142d7eaccb4ad'
auth_token = 'c87adf9fa0af841e83f16729928c5839'
client = Client(account_sid, auth_token)

{
  "account_sid": "AC751f6b64a9a84b96c57142d7eaccb4ad",
  "api_version": "2010-04-01",
  "body": "Join Earth's mightiest heroes. Like Kevin Bacon.",
  "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
  "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
  "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "+15017122661",
  "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "status": "sent",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
  },
  "to": "+15558675310",
  "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
} 

'''

#myGame = Game(newName='hello')

#STARTING SCREEN------------------------------------*
print("\nWelcome to your \"PREVENTATIVE SPACE\"!")
print("A simulation of the experience as a disease is breaking out in your city\n")
time.sleep(1)

#VARIABLES--------------------------------------------*
name = ""
passes = 0 
health = 100

#FUNCTIONS--------------------------------------------*
def testYesOrNo(answer):
    while answer != "yes" and answer != "no":
        print("whoops! try entering yes or no")
        answer = input().lower()
    return answer

def testOptions(answer):
    while (answer != "a") and (answer != "b") and (answer != "c"):
        prompt = "whoops! try entering a, b, or c" 
        answer = input(prompt).lower()
    return answer

#MENU-----------------------------------------------*
chosenOption = ""
print("--WELCOME TO THE MENU--")

while chosenOption != "1":
    print("\nPlease pick one")
    print("1: Start Game")
    print("2: Commands")

    chosenOption = input()

    while chosenOption != "1" and chosenOption != "2":
        print("\nWhoops! please try again. Enter one of the option numbers")
        chosenOption = input()

    if chosenOption != "1":
        if chosenOption == "2":
            print(
                "\nUse the options:\n- yes\n- no\n- A\n- B\n- C" 
            )
            print(
                "\n)Only use custom responses when prompted (ex: please type character name)\n\n"
                        )
        print("Would you like to return to menu?")
        chosenOption = input()
        testYesOrNo(chosenOption)
        while chosenOption == "no":
            print("\nOkay, you're just stuck on this page then...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("... Would you like to return to the menu now?\n")
            chosenOption = input()

#GAME STARTS ---------------------------------------*
#CHARACTER NAME***
print("\nPlease type your character's name")
name = input()
name = name.upper()
print("\nWould you like to name your character " + name + "?")
answer = input()
answer = testYesOrNo(answer)

while answer == "no":
    print("\nPlease input character name")
    name = input()
    name = name.upper()
    print("\nWould you like to name your character " + name + "?")
    answer = input()
    answer = testYesOrNo(answer)
    '''
    print("\nWould you like to use your phone number in this game? Please type in this without dashes, without the national area code.\n")
    phoneNumber = input()
    phoneNumber = '+1' + phoneNumber 
    message = client.messages \
    .create(
         body='WELCOME to preventative health',
         from_='+19102188683',
         phoneNumber='+14158167260'
     )
print(message.sid)
    '''
    
    
    
print("\nPerfect! Welcome " + name + "!")
print("Your life will now load...\n")
time.sleep(1)
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait\n")
time.sleep(2)

#GAME START (INTRO)------------------------------------*
""" 
General Info, all paths will have this code
"""

print("-- DAY 1 --\n")
time.sleep(1)
prompt = "You wake up in the morning, and cry just a little bit. Now what do you do?\n\
      a) The room feels stuffy, go open up a window and take a deep breath of fresh air\n\
      b) You feel hungry, eat the food your friend bought you from last night\n\
      c) You notice the time, your sister is about to be late to school, go and shake her awake\n"
        
ans = input(prompt).lower()
ans = testOptions(ans)

if ans == "a":
    travel = 1
elif ans == "b":
    travel = 2
else:
    travel = 3

prompt = "\nYou go to school and walk down the hall, you hear whispers of student being out with some sickness this week from students around you. Once lunch starts, your friend goes to wash their hands before eating, do you wash your hands as well? (yes/no)\n"
ans = input(prompt).lower()
ans = testYesOrNo(ans)
passes = 0 
if ans == "yes":
    passes = 1
    prompt = "\nHow long do you wash your hands?\n\
        a) 20 seconds, we're being thorough today!\n\
        b) Quickly, there's more important things to do!\n"
    
    ans = input(prompt)
    ans = testOptions(ans)
    
    if ans == "a":
        passes +=1
    elif ans == "b":
        health -= 3
else:
    health -=5

prompt = "\nAfter lunch you decide to buy a drink from the vending machine to get you through the day, what do you want to buy?\n\
        a) Water\n\
        b) RedBull\n\
        c) Orange Juice\n"
        
ans = input(prompt).lower()
ans = testOptions(ans)

if ans == "b":
    health -= 5
elif ans == "c":
    passes += 1

print("\n-- DAY 2 --\n")
#text about the person who went to the hospital: "Did you hear about what happeneed to..."
prompt = "The next day at school you hear whispers about a potential disease going around, how weird... In class that day, the teacher discusses the coming flu season, and your friend decides to get flu shots after school, do you get the shot as well? (yes/no)\n"

ans = input(prompt).lower()
ans = testYesOrNo(ans)

if ans == "yes":
    passes += 1
else:
    health -= 5

prompt = "\nAfter stopping by the pharmacy for the flu shots, it is a bit chilly outside as you are walking home. But your fit is on point today, do you wear a jacket? (yes/no)\n"

ans = input(prompt).lower()
ans = testYesOrNo(ans)

if ans == "no":
    health -= 5
else:
    passes += 1

prompt = "\nThat evening during dinner, you want a sip of your sister's drink but she says she's had a cough all day, do you still take a drink? (yes/no)\n"

ans = input(prompt).lower()
ans = testYesOrNo(ans)

if ans == "yes":
    health -= 5
else:
    passes += 1

print("\nYou settle into bed and drift off to the sounds of the news, but you can't make out what they are saying... z z Z\n")

if passes > 2:
    passes = 2

print ("\n-- DAY 3 --\n")
time.sleep(1)
print ("You open your planner Sunday night and take a look at what you have coming up soon in your schedule:\n")
time.sleep(1)

#DIVICO (airborne)------------------------------------*
if travel == 1:
    print("Week 1: Bus Trip\n")
    print("Week 1: School Sports Game\n")
    print("Week 1: Mall Trip\n")
    time.sleep(2)
    print("--WEEK ONE--\n")
    print("This week, your class is going on a bus trip to a nearby national park! You have been anxiously waiting for this trip for a while now. The park is about three hours away, so the school has organized some charter buses for transportation.\n")
    time.sleep(2)
    print("-- 6:45AM --")
    print("You arrive at school at 6:45 am, ready to go on the trip! You can see that most of your classmates have already arrived. As you get on the bus, it appears to already be really full. It’s going to be a long ride…") 
    time.sleep(4) 
    print("\nYou get on the bus, and realize that your friends are on it! You're really excited. However, it seems like there's only one seat left. It's located near the middle of the bus, next to your friend! She smiles and waves at you, but you quickly notice that the girl in the seat behind her breaks into a coughing fit. ")
    prompt = "\nDo you take the seat next to your friend? (yes/no) "
    ans = input(prompt).lower() 
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
      health -= 3
    elif ans == "yes":
      passes -= 1
    prompt = "\nIt's an hour into the ride! You're talking to your friend about the trip, and how excited the two of you are. As you're having the conversation, you can't help but notice that a lot of people on the bus seem to be sick. It feels like the back of your throat seems to be getting a little dry too... What do you do?\na) drink some water \nb) take a short nap, you're probably okay\nc) continue talking to friend\n"
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if (ans=="b" or ans=="c") and passes == 0:
      health -=3
    elif ans == "b" or ans =="c":
      passes -= 1

    prompt = "\nAfter several long hours of being in the stuffy charter bus, you and your classmates finally arrive at the park! It's going to be so fun to get to spend so much time with your friends! The teacher organizes everyone into groups for activities during the day. All of your friends join the group that will be learning about wildlife in the area. Wow, you'll get to see the animals! Do you go with them? (yes/no)\n"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
      health -= 5
    elif ans== "yes":
      passes -= 1
  

    prompt = "\nOn the next day of the trip, your friends decide to go hiking early next morning. The area is so beautiful, the trees are magnificently green and you can see the sunlight coming in through the leaves of the trees. The paths \
        are a little hard to navigate though. Amidst conversation, one of your friends suddenly trips and hits their leg on a large jagged rock. Oh no, it looks like the cut is bleeding. Your friend should probably go to the park's health clinic. Do you take them?\n"

    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
      health -= 5
    elif ans == "yes":
      passes -= 1

    print("\nThe trip was a lot of fun. You take the bus back. The next day you arrive back home, you hear a notification come in on your phone. Looks like a school email.  \n")
    time.sleep(3)
    print("\nThe email says that a large handful of students are sick, and to stay safe... It encouraged students to take care of themselves and make sure everyone stays home while they are sick! Wow, it seems like a lot of people got sick on that trip.\n")
    time.sleep(3)

    print("\n--WEEK 2--")
    time.sleep(2)
    print("\n It's the next week! There is a football game at your school today, and it's been the buzz of the school for weeks. Everyone will be there!\n")
    time.sleep(4)
    print("\nYou think you might go to the football game with your friends, and then maybe go to the after party!")
    time.sleep(4)

    prompt = "\nWhat is your plan for the football game?\na) hang out in the front to watch\nb) sit near the back and try to see what you can\nc) walk around and say hi to everyone!\n" 
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if ans == "a" and passes == 0:
      health -= 7
    elif ans == "a":
      passes -= 1
    elif ans == "c" and passes == 0:
      health -= 3
    elif ans == "c":
      passes -= 1
    elif ans == "b" and passes== 0:
      health -= 3
    elif ans == "b":
      passes -=1

    print("\nEveryone seems to be having so much fun! The atmosphere is loud and everyone is moving around. ")
    time.sleep(2)
    prompt = "\nWow! It looks like your team is winning. Everyone is cheering loudly. As you're watching the game, your friends approach you and tell you about the after party happening at another student's house. Do you want to go?\n"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes <= 1:
      passes = 0
      health -= 4
    elif ans == "yes":
      passes -=1
    if ans == "yes":
      print("\nYou show up to the party with your friends. Even with the cautionary emails from your school, it looks like most people managed to make it. Who would miss an event like this? ")
      time.sleep(2)
      print("\nSome people still do look sick though. Hopefully flu season passes soon...")
      time.sleep(2)
      prompt = "\nIt can't be THAT bad. You see the person you like near the snack table at the party. Maybe you should go say hi? (yes/no)\n"
      ans = input(prompt).lower()
      ans = testYesOrNo(ans)
      if ans == "yes" and passes <= 1:
        health -= 5
      elif ans == "yes":
        passes -= 1

    else:
      print("\nYou decide to stay in and hang out with your friends inside instead. Seems like the better, safer idea.\n")
      time.sleep(2)
      print("\nIt's been really hectic being around so much people. Especially with all the health precautions going around, it's better to be safe than sorry.\n")
      time.sleep(2)
      prompt = "\nWhat should you do with your friends?\na) watch a movie at home\nb) have a fun gossip session\nc) work out together..haha\n"
      ans = input(prompt).lower()
      ans = testOptions(ans)
      if ans == "a" and passes == 0:
          health -= 2
      elif ans == "a":
          passes -= 1
      elif ans == "b" and passes == 0:
          health -= 7
      elif ans == "b":
          passes -= 1


    print("\nIt was a fun, and productive evening! You're glad you got to see your friends. However, it IS stil a school night...\n")
    time.sleep(2)
    print("\nOh right... a school night...\n")
    time.sleep(2)
    print("\nDon't you have an exam tomorrow?\n")
    time.sleep(2)
    prompt = "\nDo you \na) sleep early, \nb) study a little bit, \nc) cram in another study session for the exam...just in case?"
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if ans == "b" and passes == 0:
      health -= 4
    elif ans =="a":
      passes -= 1
    elif ans == "c" and passes == 0:
      health -= 10
    elif ans == "c":
      passes -= 1
    print("\nWell...we'll see how you do on that test...fingers crossed!")
    time.sleep(2)

    print("\n--Week Three: Home Stretch! --")
    time.sleep(2)
    print("\nIt sems like everyone has gotten better since the news from the email. People aren't coughing at school anymore, and everyone seems okay.\n")
    time.sleep(2)
    print("\nPlus, it doesn't seem like you caught anything...yet...\n")
    time.sleep(2)
    print("\nThis weekend, you have plans to go to the mall with your friends. Seems like it would be good time for you to catch up after the exams.\n")

    time.sleep(2)
    print("\n--11:00AM--\n")
    time.sleep(2)
    prompt = "\nYou arrive at the mall with your friends. It seems like they're hosting some health prevention fair outside it. The booths are encouraging people to sanitize their hands and cough in their sleeves and cover their mouths. Do you want to go sanitize your hands?\n"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "no" and passes == 0:
      health -= 5
    elif ans == "no":
      passes -= 1

    prompt = "\nYou head inside the mall. You're so excited to go shopping and finally buy new clothes! Inside the mall there is a crowd of people around an area. It seems like there's a performer. Want to check it out? (yes/no)\n"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
      health -= 5
    elif ans == "yes":
      passes -= 1

    print("\nYou and your friends go around the different shops having fun, trying on clothes and picking out outfits for each other. Some of the items were such a bargain!\n")
    time.sleep(2)
    print("\nWho can resist a good shopping trip? This hangout was just what you needed. \n")
    time.sleep(2)
    prompt = "\nYou do feel a bit tired though. Is it time to \na) stay for food before you leave \n b) start heading home \n c) buy more clothes?\n" 
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if ans == "a" and passes == 0:
      health -= 5
      print("\nGuess there's always time for food!")
      time.sleep(2)
    elif ans == "a":
      passes -= 1
      print("\nGuess there's always time for food!")
      time.sleep(2)
    elif ans == "c" and passes == 0:
      health -= 8
      print("\nCan't blame you for making that choice...")
      time.sleep(2)
    elif ans == "c":
      passes -= 1
      print("\nCan't blame you for making that choice...")
      time.sleep(2)
    elif ans == "b":
      print("\nYou should probably get rest anyway...")
      time.sleep(2)
      
    print("\nLet's see how you did...\n")
    time.sleep(5)
    if health >= 75:
      print("\nYou didn't get the flu, which is great!\n")
      time.sleep(1)
      print("\nIn the case of getting the flu, make sure to be taking the same precautions. Sanitize often, get rest. Get vaccinated!")
    elif health < 75 and health >=50:
      print("\nYou are feeling feverish...that's not good...\n")
      time.sleep(1)
      print("\nPlease make sure that you are taking medicine, and stay indoors so you don't infect others!\n")
      time.sleep(1)
      print("\nIn the current conditions, it would be recommended that you see a doctor if your symptoms do not get better within reasonable time.")
    else:
      print("\nYou seem to have developed a fever...And it's really high...\n")
      time.sleep(1)
      print("\n...\n")
      time.sleep(1)
      print("\n...\n")
      time.sleep(1)
      print("\nYou wake up in the hospital. The doctor is currently monitoring your symptoms to make sure your fever doesn't get any higher. Next time, please be more careful!\n")
      time.sleep(1)


#COLAPO (FOOD - SALMONELLA)-------------------------------------------*
elif travel == 2:
    print ("Monday: School Food Fair")
    print ("Tuesday: Dinner with Friends!")
    print ("Wednesday: Street Food Fair\n")
    print ("You can't wait for this week to get started :D")
    time.sleep(5)
    
    print ("-- MONDAY --\n")
    print ("Tomorrow there is a big school food fair where students or clubs and make food for students to buy. There are common popular foods as well as exotic foods or even raw foods from around the world!\n")
    print ("The night before, you overhear on the news something about a contamination, but you are too busy messaging your friends to pay close attention.\n")
    time.sleep(2)
    print ("-- 11:45 AM --")
    print ("It's the day of the school food fair and you are starving, you forgot breakfast and the thought of all the foods available is almost making you drool... yum...")
    time.sleep(1)

    prompt = "As you search for the first course of your lunch, you hear your friend raving about three stalls and decide to choose one of their favorites:\n\
            a) Chicken, cooked quickly to serve the long line, a popular choice among students, surely implying its deliciousness\n\
            b) Fried Rice, a meal as filling as it is easy to cook\n\
            c) Salad, a healthy option that apparently tastes delicious\n\
    which food do you buy?\n"
    
    ans = input(prompt).lower()
    ans = testOptions(ans)
    
    if ans == "a"and passes == 0:
        health -= 3
        print("\nYou take a couple of bites but realize the chicken is still quite pink in the middle, but you're hungry so you demolish the dish anyways.")
    elif ans == "a":
        passes -= 1
        print("\nYou take a bite of the chicken, see some bright pink, inidcating the chicken was not cooked thoroughly and toss it immediatly. Instead, you just get some fried rice, at least there's no uncooked meat in this dish.")

    prompt = "\nAfter eating you casually browse the reamining stalls to pass the rest of lunch. One last stall catches your eye however, a raw cookie dough stall that looks very popular and very aesthetically pleasing. Do you buy some dessert before lunch is over? (yes/no)\n"
    
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    
    if ans == "yes" and passes == 0:
        health -= 5
    elif ans == "yes":
        passes -= 1
        
    time.sleep(1)
    print("\nFull from all the delicious food you tried today, you go float through the rest of your classes through the day, and go home to see what other classmates ate and posted on Instagram.")
    print("\nYou hear from your friends that someone got food poisoned by one of the stalls serving milkshakes! You didn't even notice they were serving milkshakes... now they are resting at home from 'COLAPO'? That sucks...")
    time.sleep(2)
    
    print("\n-- TUESDAY --\n") 
    time.sleep(2)
    print("-- 3:30 PM --")
    print("In order to keep the happy vibes between the school food fair and the city food fair Wednesday, your friends have planned a little dinner where everyone brings a yummy dish.\n")
    print("You were planning on making deviled eggs, but you get a text that makes you change your mind and bring the drinks instead.\n")
    time.sleep(2)
    print("TEXT from Bestie <3: Hey {}, please no eggs, you know I'm allergic, I need at least one dish that I can eat at the dinner!!\n").format(name)
    time.sleep(2)
    
    prompt = "As the main course, your friend Henry had cooked up some steaks, but as you guys begin to dig in you all notice that the steaks are quite bloody. Your best friend even asks 'are you sure you really cookied this?' What do you do?\n\
        a) eat the steak, you've always liked your meat on the rarer side\n\
        b) take a couple bites, you don't want your friend to feel bad\n\
        c) pass on the steak, that amount of blood probably means it wasn't cooked enough for consumption\n"
    
    ans = input(prompt).lower()
    ans = testOptions(ans)
    
    if ans == "a"and passes == 0:
        health -= 10
        print("\nYou eat the steak, but it sits heavy in your stomach... this steak was NOT cooked enough")
    elif ans == "a":
        passes -= 1
    elif ans == "b" and passes == 0:
        health -= 3
        print("\n3 small bites is all you can manage, but you assure your friend it was delicious.")
    elif ans == "b":
        passes -= 1
    else:
      print("\nYou claim you are trying to cut back on meat, and safely avoid the bloody steak without offending Henry.")
    
    print("\nAs dessert rolls around, Madison, who had been in charge of that dessert, tells everyone 'I almost forgot to make something, but I whipped together some milkshakes for dessert using some eggs I left on the counter a couple days ago, milk, and ice cream!!'")
    prompt = "Your best friend gives you a sad looks and says 'Guess I can't have dessert since it has eggs, but honestly I'm questioning the quality of the milkshakes if they were made so last minute.' Do you have have some milkshakes as dessert? (yes/no)\n"
    
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    
    if ans == "yes" and passes == 0:
        health -= 5
        print("You drink a whole milkshake, it tastes delicious!")
    elif ans == "yes":
        passes -= 1
        
    time.sleep(2)
    print("\nAs the dinner and the night comes to an end, you lay in bed thinking about the nice meal you had, regardless of the little bumps in the road that may have been hit.")
    print("One of your classmates texts you that they seem to suddenly have gotten a fever, and asks you to send them your notes from class the next day. You agree, tell them to rest up, and go to sleep thinking about all the food you'll be eating the next couple of days")
    time.sleep(1)

    print("\n-- WEDNESDAY--\n") 
    time.sleep(1)
    print("-- 10:00 AM --")
    print("The city food fair is a tradition each year, and all schools cancel classes for the day so students can enjoy it freely.")
    time.sleep(1)
    print("As you watch some TV that morning, you see some shocking news")
    time.sleep(1)
    print("BREAKING NEWS: Salmonella Breakout, 3 teenagers hospitalized with COLAPO, potential contamination source: uncooked meat or raw eggs")
    time.sleep(1)
    print("Almost immediately after reading the headline you get a text from your best friend.")
    time.sleep(1)
    print("TEXT from Bestie <3: {}! Did you see the news about the food poisoning? Henry from yesterday is apparently one of the hopsitalized teenagers, his mom said he must've eaten some meat that wasn't cooked properly or something... Do you still want to go to the food fair tomorrow? You know that some of those vendors like serving dishes with raw food...\n").format(name)
    prompt = "Your best friend brings up a good point, but you were so looking forward to the event... Do you still want to go? (yes/no)\n"
    
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    
    if ans == "yes":
      print("\n-- THE NEXT DAY --\n")
      time.sleep(1)
      print("-- 11:30 AM --")
      print("At your insistence, your friend decides to come along to the food fair, and immediatly notice the low audience turnout, most likely due to the the news from last night. ")
      time.sleep(3)
      print("The most popular stall seems to be a group of student serving japanese cuisine, and you decide to purchase some food to show support.\n\
      They boast to you 'Try the raw egg dish we have with rice! The rice is still a little warm, and don't worry about the raw eggs, if people in Japan eat this and don't get Salmonella, so can we! It's just eggs, right?'")
      prompt = "What do you decide to get?\n\
        a) the raw egg dish, it's just egg after all!\n\
        b) a teriyaki chicken dish, seems to be safer way to support your fellow students\n\
        c) just some water, this booth seems to have a questionable food quality\n"
      
      ans = input(prompt)
      ans = testOptions(ans)
    
    if ans == "a" and passes == 0:
        print("\nThe egg was very raw, but you're a fan of Japanese cuisine and finish it all.")
        health -= 10
    elif ans == "b" and passes == 0:
        print("\nYou take a bite, the chicken is bright pink and undercooked so you toss it. What a waste of money.")
        health -= 5
    elif ans == "a" or ans == "b":
        passes -= 1
    else:
      print("\nSafe move, you and your friend decide to just have a movie night and hang out together at home.")
      
    time.sleep(2)
    print("\n-- 7:00 PM --\n")
    print("\nIt's the evening after the city food fair, and you are sitting on the couch.\nYou see on the news that there is now a confirmed COLAPO outbreak and all citizens are warned to watch out for certain raw meats and eggs, and to thoroughly cook all food.")
    time.sleep(1)
    
    if health >= 75:
        print("You feel completely fine, health-wise. It's a good job you took all those extra precautions this past week.\n")
        time.sleep(1)
        print("\nMake sure that you continue to stay healthy and encourage others to take extra precautions as well")
    elif health < 75 and health >=50:
        print("\nYou are feeling terrible. You got a fever in the evening and have spent the past hour on the toilet after your stomach pains were too much to handle\n")
        time.sleep(1)
        print("\nYou most likely got food poisoned, but probably not with the COLAPO that has been placing people in the hospital.\n")
        time.sleep(1)
        print("\nYou spend the rest of the epidemic, resting up at home and getting over your bad tummy-ache.")
    else:
        print("Your stomach is in crazy pain.... oh no...\n")
        time.sleep(1)
        print("\n...\n")
        time.sleep(1)
        print("\n...\n")
        time.sleep(1)
        print("\nYou wake up in the hospital. Welp. Apparently all that careless eating led to you getting COLAPO, a foodborne disease! Next time, try to be more careful about the food you consume!\n")
        time.sleep(1)
        
    time.sleep(5)
      
#TANESSLA (BODILY CONTACT - EBOLA)------------------------------------*
elif travel == 3:
    print ("Week one: Hangout with friends at the rollerskating rink\n")
    print ("\nWeek two: Date with your crush <3\n")
    print ("\nWeek three: School formal!\n")
    print ("\nYou can't wait for this week to get started :D\n")
    time.sleep(3)

    print ("-- WEEK 1 --\n")
    print ("This week, you have a huge hangout planned with your friends! The plan is everyone is meeting up at the rollerskating rink and dance to music all night.\n")
    time.sleep(1)
    print ("You are a little wobbly on your feet, but you know you can rely on your friends to hold onto so you can get your balance. Hopefully ~youknowwho~ is there ;)\n")
    time.sleep(1)
    print ("-- 5:00PM --")
    print ("It's the day of the event and you are picking between outfits before you have to meet up with everyone at 7pm.")
    time.sleep(1)

    prompt = "Your sister comes into your room with fresh laundry and picks up one of your favorite shirts and says \"Hey you should wear-\" before coughing into her arm. Do you still take the shirt? (yes/no)"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
        health -= 3
    elif ans == "yes":
        passes -= 1
    time.sleep(1)
    print("You leave your house and drive to the rink. woohoo!")
    time.sleep(1)

    prompt = "As your pulling into the rink's parking lot, you spot your friends pulling in at the same time. You all run out of your cars and convene in the middle. They open their arms to do a group hug, do you join?\n a) awkwardly avoid the hug\n b) yes, get as close as humanly possible to them\n c) give only one of them a weird side hug"
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if (ans == "b" or ans == "c") and passes == 0:
        health -= 5
    elif ans == "b" or ans == "c":
        passes -= 1
    
    prompt = "\nYou all excitedly head inside and go to the rent equipment station. You quickly realize you forgot to bring socks since you are wearing birkens. The renter says that they clean the shoes after every single day and you got there 30 minutes after the rink opened so there might be a chance no one has worn it for the day. Do you buy $10 socks to wear with your rented shoes? (yes/no)"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "no" and passes == 0:
        health -= 5
    elif ans == "no":
        passes -= 1

    print("Your skating with your friends around the rink when you spot ~youknowwho~ across the rink. You tell your friends you'll catch them later and head over to ... ;)\n")
    time.sleep(1)
    print("As your skating over there, you see the person of interest coughing into their elbow and then quickly laugh it off.\n")
    time.sleep(1)
    prompt = "You reach their wall and start skating beside them. They seem to keep leaning your direction as they wobble a little bit. Do you:\n a) hold their hand\n b) tell them to go practice skating by holding onto the wall\n c) wait till they grab onto your shirt sleeve\n"
    ans = input(prompt).lower()
    ans = testOptions(ans)
    if (ans == "a" or ans == "c") and passes == 0:
        print("Oooh lala~ Looks like things are heating up ;)")
        health -= 5
    elif ans == "a" or ans == "c":
        passes -= 1
    else:
        print("Welp. You could've helped them you know.")

    time.sleep(1)
    print("At the end of your hangout, you wave bye to each of your friends and start heading home. As your driving home, you turn on the radio and listen to your local news station. They are talking about the importance of getting vaccinated for the flu and that flu cases seem to just keep growing. Weird.")
    time.sleep(1)
    print("You think about how great your night was as the radio station starts listing the places you can get your flu shots. You drive on through the night and when you get home, you get ready for the next coming weeks.")
    time.sleep(1)

    print("-- WEEK 2 --") 
    time.sleep(1)
    print("\nIt is now the next week, and you jump excitedly out of your bed because today is the day! The perfect date with your crush <3\n")
    time.sleep(1)
    print("\nTwo weeks ago, you worked up the courage to ask ~youknowwho~ out on a cute picnic to Central Park ^-^ and today is finally the day~ <3\n")
    time.sleep(1)
    print("\nYou are getting ready and searching through your closet for outfits. While you are going through them, you get an email from the school about flu season and text from your friend saying \"LOL did you see the school email\"\n")
    time.sleep(1)
    prompt = "The email reads: \"Dear student body, you all should be taking great precautons as the flu this season seems to be more aggressive than ever before... Do you take the email seriously and take better precautions? (yes/no)"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "no" and passes == 0:
        health -= 5
    elif ans == "no":
        passes -= 1
    else:
        passes += 1
    
    prompt = "As soon as you finish reading it, you get a text from your crush saying they are unsure if they should go because they don't feel great. Do you convince them? You've been waiting for this day for a long time. (yes/no)"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    if ans == "yes" and passes == 0:
        health -= 5
    elif ans == "yes":
        passes -= 1
    else:
        passes += 1
        
    if ans == "yes":
        print("\n\nYou go on the date and meet your crush at the park. Their eyes are so red and you wonder what's wrong?")
        prompt = "You guys are walking from the parking lot and they are complaining that their leg muscles hurt and ache. Do you hold their hand to support them?"
        ans = input(prompt).lower()
        ans = testYesOrNo(ans)
        if ans == "yes" and passes == 0:
            health -= 5
        elif ans == "yes":
            passes -= 1
        else:
            passes += 1
            
        print("\nYou guys continue walking, and they collapse from how weak they feel...\n")
        time.sleep(1)
        print("Something isn't right...\n")
        time.sleep(1)
        print("Immediately, you drive them to the emergency room.\n")
        time.sleep(1)
        print("\nOne you get there, the doctor asks for their symptoms and you state that they had: weakness, confusion, aches, red eyes, a cough\n")
        time.sleep(1)
        print("\nThe doctor looks pale as you are telling them this information. The doctor thanks you for bringing them and allows you to go home.\n ")
        time.sleep(1)
        print("\n What is going on right now?\n")
        time.sleep(1)
        print("You drive home. You reach home just before sunset.")
    
    else:
        print("\nYou're pretty bummed about that your date fell through but it is probably for the best they stay home for their good and yours.")

    while passes < 2:
     passes += 1
     
    print("\nYour sitting on your couch when you receive another email from school.\n")
    time.sleep(1)
    print("\nThe email reads: EMERGENCY! Reported cases of the Novel Tanessla virus has been reported. Everyone please be digilent about taking precautions. If you are feeling any symptoms just as severe coughing, coughing blood, vomiting, red eyes, and other flu-like symptoms, please go to the emergency room!\n")
    time.sleep(1)
    print("\nYou overhear the radio from the kitchen where your mother is listening to the news.\n")
    time.sleep(1)
    print("\n\"The county has reported cases of the Tanessla-00 virus, a few others are being tested for it now. Please stay cautious everyone\" the radio states.")
    time.sleep(1)
    print("\nThis is all too much for you, after the stress of the day you just had. You go upstairs and lay down. You drift off\n")
    time.sleep(1)
    print("\n-- WEEK 3 --\n")
    print("\nYou wake up to a text from your friend asking if you are still going to the school dance this week\n")
    prompt = "\nDo you go? (yes/no)\n"
    ans = input(prompt).lower()
    ans = testYesOrNo(ans)
    
    if ans == "yes" and passes == 0:
        health -= 5
    elif ans == "yes":
        passes -= 1
    if ans == "yes":
        print("\nYou are getting ready to go to the dance.")
        if health < 75:
            time.sleep(1)
            print("\nYou are coughing a bit. Ah jeez. \"I should be ok though\"\n")
        time.sleep(1)
        print("\n You drive to the dance and there you notice more people are coughing than usual.\n")
        time.sleep(1)
        print("\nYou meet up with your friends and tell them about your date. You guys find your way to the dance floor and start jamming out to the bops playing.\n")
        time.sleep(1)
        print("\nYou forget about what's happening for a quick second as you dance with your friends\n")
        time.sleep(1)
        print("*COUGH COUGH* *HACK*\n")
        time.sleep(1)
        print("You and your friends turn around to see one of your classmates on the floor coughing and it's bad\n")
        time.sleep(1)
        health -= 10
        print("\nSome adults rush over and immediately one of them divert the attention and tells everyone to go outside.\n")
        time.sleep(1)
        print("\nAs you are all waiting outside, the principal comes out and tells everyone to go home. They are worried that the student might have caught the deadly virus.\n")
        time.sleep(1)
        print("\nBummed out. You and your friends turn to go home.\n")
    else:
        print("\nYou stayed home. But over the news you hear that the school dance got shut down due to a possible case of Tanessla-00.\n")
        print("\n\"Good thing I didn't go\" you think to yourself.\n")
        while health < 50:
          health += 1

    time.sleep(2)
    print("\n-- 9:00PM --\n")
    print("\nIt's been a few hours since the dance and you are at home, sitting on the couch.\n")
    time.sleep(1)
    if health >= 75:
      print("You feel completely fine, health-wise. It's a good job you took all those extra precautions.\n")
      time.sleep(1)
      print("\nYou spend the rest of the epidemic, completely fine.")
    elif health < 75 and health >=50:
      print("\nYou don't feel great, but not quite death either.\n")
      time.sleep(1)
      print("\nYou most likely caught some kind of disease but probably not the one that is going around.\n")
      time.sleep(1)
      print("\nYou spend the rest of the epidemic, resting up at home and getting over your \"illness\"?")
    else:
      print("You feel nauseous.... oh no...\n")
      time.sleep(1)
      print("\n...\n")
      time.sleep(1)
      print("\n...\n")
      time.sleep(1)
      print("\nYou wake up in the hospital. Welp. Next time, try not to get infected and take better precautions!\n")
    time.sleep(1)
  


#ENDING INFO------------------------------------*
  
print("\nCongrats " + name + "! You finished the game. Depending on your choices/precautions, you either didn't get it, got only a little sick or ended up in the hospital with the virus!\n")
time.sleep(1)  
print("\n\n-------------------------------------------------------------------------------")
time.sleep(1)

if travel == 1:
    time.sleep(10)
    print("\nDIVICO-22\n\n")
    time.sleep(2)
    print("DIVICO is a based off of an airbone virus, which we incorporated because of the recent cases of the 2019 novel Coronavirus. We also thought this was relevant as it is currently flu season!")
    print("In this game, the character notices that the people surrounding them are experiencing flu like symptoms, like coughing, sneezing, feeling tired, and fevers. ")
    print("In the game, most of the interactions are based off of going to places where people are together in a close vicinity. Interacting with people who have the flu or taking in air droplets \
    with the virus can affect your health. ")
    print("Usually, the body can fight off the flu on its own, with time, hydration, and rest. It's imporant to take time to rest! There are also medicines that can suppress the effects of the symptoms meanwhile, as some of them can be difficult. ")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT YOURSELF:\n\n")
    time.sleep(2)
    print("Try not to interact with people who are experiencing the flu or flu-like symptoms. \n\
    It is REALLY, REALLY important to stay hydrated during this time. \n\
    With the cases of Coronavirus happening around the country, many people can be worried. However, the CDC recommends that if you would not have otherwise visited the doctor if not for the Coronavirus concerns, you shouldn't have to go.\n")
    print("Symptoms of the flu include fever, body pains, cough, sneeze, a stuffy nose, an overall feeling of tiredness, and sometimes even pain in your ears. ")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT/HELP OTHERS:\n\n")
    time.sleep(2)
    print("While the flu is generally easy to fight off for people with good immune systems, prevention of the spread is still important. Make sure to always wash your hands.")
    
          
if travel == 2:
    time.sleep(10)
    print("\nCOLAPO-20\n\n")
    time.sleep(2)
    print("COLAPO is a made up disease based off of Salmonella, a bacteria transmitted through food, most popularly through raw or undercooked meats or egg that can Salmonella infections.")
    print("Notice the timeline of this game, within 3 days (72 hours) an epidemic of COLAPO had begun; in reality diseases such as Salmonella will begin affecting your body anytime between 24 to 72 hours after consuming contaminated food.")
    print("In the game, your character had many opportunities to eat semi-questionable food, some straight up raw that would definitely poision a person, or small bites improperly prepared food that can still lead to stomach pain or diarrhea")
    print("In reality, you most likely won't have to go to the hospital if you caught Salmonella, but in serious cases where your body becomes dehydrated, then it is possible.")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT YOURSELF:\n\n")
    time.sleep(2)
    print("Beware of raw foods, eggs cooked unproperly can be harmful. In the case of the japanese cuisine booth, regular eggs were not the best idea, as in Japan eggs are checked to make sure that they are safe to eat raw.\n\
    Similarly, meats that are not properly cooked should not be consumed, regardless if your friend will feed bad or not :(\n\
    Also, pay attention to the news, any contaminations in food sources is important to notice, especially since we all need to eat!")
    print("Symptoms of foodborn illnesses include stomach pain, diarrhea, but also fever and vomitting.")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT/HELP OTHERS:\n\n")
    time.sleep(2)
    print("As a disease that passes through food, you cannot pass Salmonella to someone, but to cook and serve foods with caution if you are using meats or eggs that may not be cooked very thoroughly (such as steaks or eggs).")
    
if travel == 3:
    time.sleep(10)
    print("\nTANESSLA-00\n\n")
    time.sleep(2)
    print("Tanessla is a fictional disease that is based off diseases that spread through bodily contact such as Ebola. We modeled the symptoms after ebola which included: red eyes, coughing up blood, nausea, confusion, and vomitting and other flu-like symptoms.")
    print("During the game, everytime the user came in direct contact with another individual, it was a direct affect on their health. It is important to protect yourself and the health of others. Yes, you should not touch anyone that might have such an easily contracted disease, however, it is important to get peeople you suspect that might have it, proper help.")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT YOURSELF:\n\n")
    time.sleep(2)
    print("\n- Always wash your hands for at least 20 seeconds\n- Don't touch anyone directly who may have a disease that spreads though bodily contact easily\n- don't go to areas with a large amount of people during a time of pandemic\n")
    time.sleep(5)
    print("\n\nWAYS TO PROTECT/HELP OTHERS:\n\n")
    time.sleep(2)
    print("\n- If you think you contracted it, stay away from people and go get the proper help from medical professionals\n- Don't touch anyone directly\n- If you see someone who might have it, immediately call medical professionals and leave lots of fluids next to them\n- If you believe someone has it, consult authorities to get proper help and help contain the disease, don't try to be hero if you don't know what you are doing")
    
