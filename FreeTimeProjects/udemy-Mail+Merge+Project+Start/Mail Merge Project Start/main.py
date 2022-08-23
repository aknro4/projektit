#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/letters/starting_letter.txt") as letters:
    letter_content = letters.read()

with open("./input/Names/invited_names.txt") as names:
    for name in names:
        xd = name.replace('\n', ' ')
        with open(f"./output/ReadyToSend/{xd}.txt", mode="w") as out_put:
            out_put.write(letter_content.replace("[name],", name))
