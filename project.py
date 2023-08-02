import random
print("Hey! Do you want to start the game?")
start = input("Input 'Yes!' to start.")
if start == "Yes!":
    temp_num = random.randrange(1, 4)
   
if temp_num == 1:
    num = input('Input number:')
    measure_of_time = input('Input measure of time:')
    mode_of_transportation = input('Input mode of transportation:')
    adj = input('Input adjective:')
    adj2 = input('Input adjective:')
    noun = input('Input noun:')
    color = input('Input color:')
    part_of_body = input('Input part of body:')
    verb = input('Input verb:')
    num2 = input('Input number:')
    noun2 = input('Input noun:')
    noun3 = input('Input noun:')
    part_of_body2 = input('Input part of body:')
    noun4 = input('Input noun:')
    adj3 = input('Input adjective:')
    silly_word = input('Input silly word:')
    print("""It was about {} {} ago when I arrived at the hospital in a {}. The hospital is a/an {} place, there are a lot of {} {} here.
            There are nurses here who have {} {}. If someone wants to come into my room I told then that they have to {} first. 
            I've decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. 
            I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is 
            the {} {}!""".format(num, measure_of_time, mode_of_transportation, adj, adj2, noun, color, part_of_body, verb, num2, noun2, noun3, part_of_body2, verb, noun4, adj3, silly_word, noun))

if temp_num == 2:
    proper_noun = input("Input person's name:")
    noun = input('Input noun:')
    adj = input('Input adjective(feeling):')
    verb = input('Input verb:')
    adj2 = input('Input adjective(feeling):')
    animal = input('Input animal:')
    verb2 = input('Input verb:')
    color = input('Input color:')
    gerund = input('Input verb(ending in ing):')
    adverb = input('Input adverb(ending in ly):')
    num = input('Input number:')
    measure_of_time = input('Input measure of time:')
    silly_word = input('Input silly word:')
    noun2 = input('Input noun:')
    print("""This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. I am {} we might see a(n) {},
            I hear they're kind of dangerous. While we're camping, we are going to hike, fish and {}. I have heard that the {} lake is great for {}. Then we will {} hike through 
            the forest for {} {}. If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and roast {} around  
            campfire!!".format(proper_noun, noun, adj, verb, adj2, animal, verb2, color, gerund, adverb, num, measure_of_time, color, animal, num, silly_word, noun2))
    
if temp_num == 3:
    proper_noun = input("Input person's name:")
    adj = input('Input adjective:')
    color = input('Input color:')
    animal = input('Input animal:')
    place = input('Input place:')
    adj2 = input('Input adjective(feeling):')
    magical_creature = input('Input magical creature(Plural):')
    adj3 = input('Input an adjective:')
    magical_creature2 = input('Input magical creature(Plural):')
    room = input('Input room in a house:')
    noun = input('Input noun:')  
    noun2 = input('Input noun:')
    noun3 = input('Input noun(plural):')
    adj4 = input('Input adjective:')
    noun4= input('Input noun(plural):')
    num = input('Input number:')
    measure_of_time = input('Input measure of time:')
    gerund = input('Input verb(ending in ing):')
    adj5 = input('Input adjective:')
    noun5 = input('Input noun:')
    print("""Dear {}, I am writing to you from a {} castle in an enchanted forest . I found myself here one day after going for a ride on a {} {} in {}. There are {} {} and  {} {} here! 
            In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and dream of {} {}.  It feels as though I have lived here for {} {}. I hope one day you can visit,
            although the only way to get here now is {} on a {} {}!!""".format(proper_noun, adj, color, animal, place, adj2, magical_creature, adj3, magical_creature2, room, noun, noun2, noun3, adj4, noun4, num, measure_of_time, gerund, adj5, noun5))
