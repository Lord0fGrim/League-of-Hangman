import random

# Open the file in read mode
with open("LeagueChampion.txt", "r") as f:
    # Read the contents of the file into a string
    contents = f.read()

# Split the string into a list of items
items = contents.split(",")

# Pick a random item from the list
random_item = random.choice(items).upper()

def split(word):
    return list(word)

list_word = split(random_item)

new_list = []

for i in range(len(list_word)):
    if i not in new_list:
        new_list.append("_")

print(new_list)

#check for letters
times = len(list_word) + 1
print(f'You start with {times} of tries. Have fun!!')
while times > 0:
    user_input = input("Your letter of guess: ").upper()
    for i in range(len(list_word)):
            if user_input == list_word[i]:
                new_list[i] = user_input
                print(new_list)
    if list_word == new_list:
        print("You Won!!")
        break
    else:
        times -= 1
        print(f'You have {times} of tries left.')
        
if times == 0:
    print(f'You have run out of guesses and the word is {random_item}.')
    
    

        
        

    






