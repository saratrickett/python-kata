word = "bottles"
#assign the value "bottles" (a string) to a new variable called "word"

for beer_num in range (99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    """loop specified number of times from 99 down to none. Use "beer_num" as the 
    loop iteration variable"""
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    """The four calls to the print function display the current iteration's song """
    if beer_num == 1:
        #check to see if we are on the last passed around beer
        print("No more bottles of beer on the wall.")
        #if we are, the song ends
    else:
        new_num = beer_num - 1
        #remember value of next beer in another variable called "new_num"
        if new_num == 1:
            #if we're about to drink our last beer...
            word = "bottle"
            #change value of "word" variable
        print (new_num, word, "of beer on the wall.")
    print()
    #At the end of this iteration, print a blank line. When all the iterations
    #are complete, terminate the program.