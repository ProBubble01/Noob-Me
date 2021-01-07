#recieves input from user
sentence = input('enter the sentence: ')
tofind = input('what do you want to find?: ')
#checks if tofind value exists in the sentence
trueis = sentence.find(tofind)
#prints output depending on trueis value
if trueis == (-1):
    print ((tofind) , 'does not exist in that sentence!')
else:
    print ((tofind), 'exists,'+' position is',(trueis + 1))
