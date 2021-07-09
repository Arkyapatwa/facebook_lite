# string="aabaa"
# length = 5
# length // 2
# if string[::-1]==string:
#     print("true")
# else:
#     print("False")

# print(True if string == string[::-1] else False)

# # do using for loop
# n=len(string)
# flag = 0
# for i in range (n):
#     if string[n-i-c1] == string[i]:
#         pass
#     else:
#         print(False)
#         flag = 1
#         break

# if flag == 0:
#     print(True)
string="aabaaa"
n=len(string)
i = 0
j = n-1
while i<j:
    if string[i] != string[j]:
        print(False)
        break
    i += 1
else:
    print(True)



# flag = 0
# for i in range (n//2):
#     if string[n-i-1] != string[i]:
#         print(False)
#         break
# else:
#     print(True)





    # if string[n-i::-1]==string[i::1]:
        
   





