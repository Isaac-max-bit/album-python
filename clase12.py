numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aqui i es igual a: ", i+1)
    
for i in range(3, 10):
    print(i)
    
fruits = ["manzana", "pera", "uva", "naranja", "tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "naranja": 
        print("naranja es una fruta de color naranja")
        
x = 0
while x<5:
    if x == 3:
        break
    print(x)        
    x +=1
    
numbers = [1, 2, 3, 4, 5,6]
for i in numbers:
    if i == 3:
        continue
    print("Aqui i es igual a: ",i)