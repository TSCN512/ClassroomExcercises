file = open("sampleRW.txt")
contents = file.read()
print(contents)
file.close()

#alternative syntax, slightly tidier
with open("sampleRW.txt") as file:
    contents = file.read()
    print(contents)
    #no need for file.close here, program detects if file goes unused, then closes

#file = open("sampleRW.txt", mode= 'w') remember w is write, overwrites existing content
#opening a file in write when file dosent exist creates it
file = open("sampleRW.txt", mode= 'a') #a is append, only adds
file.write("\nThank you")

file.close()
