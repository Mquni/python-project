""" Simple Program to Check Palindrome String"""

print '*****************'
print '**HELLO THERE!***'
print '*****************'
print '\n Welcome the the Python Palindrome Prober!\n'

def palidrome():

    print """Please enter the word you would like to check
                              for example: racecar         """

    word = raw_input(">> ")

    if word == word[::-1]:							#Checks if the string doesnt change when reversed				
        print 'Yes your word is a palindrome!'
    else:
        print 'Sorry this word isn\'t a palindrome :('

    print '\nHave a nice day!'

    re_play = raw_input("Want to play agian (y/n)?")

    if re_play.lower().startswith("y"):
        palidrome()
    else:
        print "Your Loss!"

palidrome()
