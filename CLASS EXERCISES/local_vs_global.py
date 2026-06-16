# Global variable
global_var = 10

def local_example():
    local_var = 5  # Local variable
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")

def modify_global():
    global global_var
    global_var = 20
    print(f"Modified global_var: {global_var}")

print(f"Before: global_var = {global_var}")
local_example()
modify_global()
print(f"After: global_var = {global_var}")
