def greet(name, last_name="No tiene apellido"): 
    print("Hello", name, last_name)
    
greet("Carli", "Gonzalez")
greet("Isaac")

greet(last_name="Garcia", name="Isaac")