#Step1 Open and read text file 'dracula.txt'
with open("dracula.txt", encoding="utf8")as input_file:
       whole_txt=input_file.read()
       print(whole_txt)
#Step2 Split the string of the newline character      
new_split=whole_txt.split('\n')
print(new_split)
#Step3 Join the split string by inserting the given string
new_join="### NEW LINE OF TEXT ###".join(new_split)
print(new_join)
#Step4 Write the last variable to new string 'dracula_extra_txt'
with open("dracula_extra.txt", "w", encoding="utf8") as output_file:
       output_file.write(new_join)     
