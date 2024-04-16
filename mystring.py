# for the counting of vowel and consonents and which are they in the sentence

def count_vowels_and_consonants(string):
    vowels = 0
    consonants = 0
    vowel_list = []
    consonant_list = []
    # Define a set of vowels for efficient lookup
    vowel_set = set("aeiouAEIOU")

    for char in string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowel_set:
                vowels += 1
                vowel_list.append(char)
                

            else:
                consonants += 1
                consonant_list.append(char)

    return vowels, consonants, vowel_list, consonant_list

input_string = input("Enter a string: ")
vowels, consonants, vowel_list, consonant_list = count_vowels_and_consonants(input_string)
print("Number of vowels in the string :", vowels)
print("Vowels found are :", ', '.join(vowel_list))
print("Number of consonants in the string :", consonants)
print("Consonants found are :", ', '.join(consonant_list))
print ("The length of the string is ", len(input_string))

