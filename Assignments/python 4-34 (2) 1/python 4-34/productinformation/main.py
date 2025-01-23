with open('toys.txt', 'r') as old_file:
    toys_content = old_file.readlines()
    
with open('new_toys.txt', 'w') as new_file:
    for line in toys_content:
        new_file.write(line)
        
num_new_toys = int(input("Enter the no. of new toys: "))
print("Enter the toy's details:")

new_toys = [] 
for _ in range(num_new_toys):
    toy_detail = input() 
    new_toys.append(toy_detail)
    
with open('new_toys.txt', 'a') as new_file:
    for toy in new_toys:
        new_file.write('\n' + toy)
        
with open('new_toys.txt', 'r') as new_file:
    updated_content = new_file.readlines()
    
print("\nThe updated details are:")
for line in updated_content:
    print(line.strip())
    
total_toys = len(updated_content)
    
print(f"\nNo. of toys: {total_toys}")