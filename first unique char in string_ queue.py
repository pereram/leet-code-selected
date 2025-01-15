
# creating a dictionary (hash table) to count the occurances of each char. 
# The keys are lined up in order of entrance.
def fistChar(str):
    char_cnt={}
    for char in str:

        if char in char_cnt.keys():
            char_cnt[char]+=1

        else:
            char_cnt[char]=1
# go through each key and find the first one with only one count value
    for key in char_cnt:
        if char_cnt[key]==1:
            return key
        

print(fistChar("asda"))
