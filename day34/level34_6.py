def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    
    print("Hello from the outer function!")
    inner_function()

outer_function()
