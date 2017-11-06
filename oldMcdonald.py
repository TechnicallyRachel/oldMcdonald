#oldMacdonald.py
#Write a program to print the lyrics of the song "Old MacDonald."
#The program should print the lyrics for five different animals.
#put parameter 'noise' in a tuple!

     
 
def sing(animal,noise):
    sound = tuple([noise]*8)
    chorus = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    print chorus
    print "And on that farm he had a %s, Ee-igh, Ee-igh, Oh!" %animal
    print "With a %s, %s here and a %s, %s there.\n\
Here a %s, there a %s, everywhere a %s, %s." %sound
    print chorus
 
         
def main():
    sing("cow", "moo")
    sing("horse", "neigh")
    sing("pig", "snort")
    sing("kitty","meow")
    sing("chick", "cheep")
     
main()

#m,f="Old MacDonald had a farm, E-I-E-I-O",
#lambda x,y:m+",\nAnd on that farm he had a %s, E-I-E-I-O,\nWith a %shere and a %sthere,\nHere a %s, there a %s, everywhere a %s %s,\n%s!"
#%((x,)+((y+' ')*2,)*2+(y,)*4+(m,))

