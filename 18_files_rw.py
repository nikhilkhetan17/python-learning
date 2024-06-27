# ------ writing a file ----------
# with open('userInfo.txt', 'a') as file:
#     file.write("This is third line...\n")

# 'w' for write - it will remove all the previous text which we have already written
# 'a' for append - it will appemd text to the exsisting file
    
# -------- reading a file ----------
    
with open('userInfo.txt') as file:
    # content = file.read()
    content = file.readlines() # returns a array list
print(content)

for ele in content:
    print(f'Hello: {ele.rstrip()}') #rstrip() -> to remove the whitespace

