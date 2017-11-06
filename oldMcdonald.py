#oldMacdonald.py
# this is a prigram to print out lyrics using functions and the modulus opporator as a variable. 
 
#creating a funtion for the lyric sequence     
def sing(animal,noise):
    sound = tuple([noise]*8)
    chorus = "Old MacDonald had a farm, Ee-i, Ee-i, Oh!"
    print chorus
    print "And on that farm he had a %s, Ee-i, Ee-i, Oh!" %animal
    print "With a %s, %s here and a %s, %s there.\n\
Here a %s, there a %s, everywhere a %s, %s." %sound
    print chorus
 
#Creating another function for our chosen animals and noises
#This function calls from the first function     
def main():
    sing("cow", "moo")
    sing("horse", "neigh")
    sing("pig", "snort")
    sing("kitty","meow")
    sing("chick", "cheep")
     
main()
