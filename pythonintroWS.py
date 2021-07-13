# 1. Write a function that takes in a list of programming languages and prompts the user for their 
# favorite programming language. If the user’s favorite programming language exists in the list, 
# return it and print the returned result to the console.

#start a function that to combine a list of programming languages and compares it to the users input.
#comprise a list of programming languages[Java, Python, JavaScript, SQL, C#, C++, Swift, Kotlin]
#prompt user to enter a name of their favorite programming laguage.
#if language is within the list, print language. if not print try another language.

def favorite_programming_lang(languages):
    user_input = input('Enter your favorite programming language:')
    if user_input in languages:
        print(user_input)
    else:
        print('try another language')

programming_languages = ['Java', 'Python', 'JavaScript', 'SQL', 'PHP', 'Swift', 'Kotlin']
favorite_programming_lang(programming_languages)

# 2. Write a function that takes in a minimum number and maximum number, and return a random 
# number between the minimum and maximum range.

# write function that passes in two numbers. One reps a min number the other will rep Max.
#generate a random number between the minimum and maximum numbers that were passed into the function.
def random_num(min, max):
    import random
    print(random.randint(min, max))

random_num(5,50)

# 3. Write a function that takes in a word and return the reversal of that word. 
# a. Example: “packers” will be returned as “srekcap”

#create a function that takes a string as an argument
#slice the string starting from the end to the beginning
#return the string back in reverse
#call the function with a string as the parameter
#print the result
def reverse_string(word):
    return word[::-1]

word_reversed = reverse_string('flow')
print(word_reversed)

# 4. Write a function that prints every number from 100 to 1 (descending).
# a. If the number is divisible by 4, print “Banana” instead of the number
# b. If the number is divisible by 7, print “Flamingo” instead of the number
# c. If the number is divisible by 4 and 7, print “Flamingo -Banana!”

# creat a function that outputs 100 - 1 in descending order.
# if a number is divisible by 4 output will be Banana
# if a number is divisible by 7 output will be Flamingo
# if a number is divisibile by both 4 and 7 output will be Flamingo -Banana!
#def div_numbers():
#   for n in range(100)


# 5. Write a function that takes in a list of numbers. Return a new list that contains only the 
# elements that are less than 5. Print to the console the contents of the returned list.
# a. [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]
# i. Bonus for fun: No duplicates in the new list.


# 6. Write a function that prompts the user for their name and age, and then prints out the user’s 
# name and the year they will turn 100 years old.


# 7. Write a function that returns a list that contains only the elements that are common between 
# the lists (without duplicates). Make sure your program works on two lists of different sizes. 
# Examples of two lists:
# i. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# ii. b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# iii. Bonus for fun: Randomly generate two lists to test this.


# 8. Write a function that takes in two words and determines if the two words are an anagram of 
# each other. a. An anagram is a word or phrase that is formed by rearranging the letters of another 
# word or phrase.
# b. Assume any word that is passed in is a word that exists in the English language
# c. If the two words are an anagram, return true. Otherwise, return false.


# 9. Write a function that takes in a phrase and reverse each word inside the string, but keeps the 
# same order of the phrase.
# a. “Hello world I am a programmer”
# b. “olleh dlrow I ma a remmargorp”


# 10. Print downward Pyramid Pattern with Star (asterisk).
# a. *****
# ****
#  ***
#  **
#  *
# b. Bonus for fun: Allow user input to decide how many stars on the first row.