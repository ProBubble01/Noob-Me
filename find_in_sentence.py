#recieves input from user
sentence = input('Sentence: ')
find = input('Find: ')
#checks if find value exists in the sentence
is_true = sentence.find(find)
#prints output depending on is_true value
if is_true == (-1):
    print ((find) , 'does not exist')
else:
    print ((find), 'exists,'+' position = ',(trueis + 1))
