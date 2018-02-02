#Sam Krimmel
#1/31/18
#adventure.py - takes the user on a grand adventure

print('You are taking a leisurely ride on train through the mountains of southern France. All of a sudden, a giant Squid Man jumps in front of the tracks, forcing the train to stop.')

print('Do you get out of the train??')
ans = input()

if 'yes' in ans:
    print("Thank Cthulu you did, Squid Man just crushed the train with a single blow, killing everyone but you and a man who you can't help but think looks exactly like Arnold Schwarzenegger.")
    print("Arny says that you and him should use the sled nearby to get to the town down the hill.")
    
    print('Do you agree?')
    ans2 = input()
    if 'yes' in ans2:
        print("Good choice, you sled down with Arny and get a good lunch at a nice Italian place that seems to not care whatsoever that you are covered in blood.")
    else:
        print("Uh oh, too late, Squid Man kills you. RIP")
else:
    print("You huddle in the corner, Squid Man smashes the train with one blow, but luckily, he just managed to not crush you.")
    
    print("There is shrapnel stuck in your upper arm, do you pull it out?")
    ans3 = input()
    if 'yes' in ans3:
        print("Your arm starts gushing blood like Niagra Falls, and you bleed out within seconds.")
    else:
        print("It hurts, but you decide to leave it in. You start to climb out of the wreck and there is a very cute looking rabbit sitting in front of you.")
        
        print("It looks so fluffy and soft, do you pet it?")
        ans4 = input()
        if 'yes' in ans4:
            print("Turns out it's that rabbit from Monty Python, you die.")
        else:
            print("Good choice, it seems to be munching on human flesh.")
            
        
