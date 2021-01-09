#Programm must read the number of blocks and tell the maximum heigh the pyramid can reach with those blocks
blocks =  int(input("Enter the number of blocks: "))

builder = 1
layers = 0
while(builder <= blocks):
        blocks -=  builder
        builder += 1
        layers += 1
        
print("The height of the pyramid: ", layers)

