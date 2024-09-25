# takeing total amount as input from user
amount =int(input("please enter amount for withdraw:"))
#calulatoring the number of notes of diffrent denominations
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("notes of 100 dolers", note_1)
print("notes of 50 dolers", note_2)
print("notes of 10 dolers", note_3)