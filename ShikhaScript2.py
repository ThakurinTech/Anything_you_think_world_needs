#Step 1 Create a dictionary named words_to_replace
words_to_replace = {"Dracula": "Luke Skywalker",
                    "blood": "fruit juice",
                     "vampire": "panda",
                     "kill": "greet"}
#Step2 Open 'dracula.txt' for reading each line as list of strings through readlines function
with open("dracula.txt", encoding="utf8") as input_file:
    new_file=input_file.readlines()
    print(new_file) 
#Step3 Empty string created
censored_txt=('')
#Step4 Iteration over the txt file line by line for word replacement 
orignal_line = new_file
for iterated_line in new_file:
        for key, value in words_to_replace.items():
            if key in iterated_line:
                iterated_line = iterated_line.replace(key,value)
#Step 5 Cesored text added to empty string, with escape sequence '\n' to maintain the spacing of orignal txt file                
        censored_txt += iterated_line+'\n'
#Step 6 New file 'dracula_censored.txt' created with last variable wriiten to it       
with open("dracula_censored.txt", "w", encoding="utf8") as censored_file:
     censored_file.write(censored_txt)
#Step 7 Print function to read and check the code     
with open("dracula_censored.txt", "r", encoding="utf8") as censored_file_2:
    print(censored_file_2.read())