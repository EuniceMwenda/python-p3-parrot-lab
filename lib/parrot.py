def parrot(argument="Squawk!"):
    print(argument)
    return argument

result = parrot("Hello!")

result_default = parrot()

print(result)          # Output: Hello!
print(result_default)  # Output: Squawk!




pass
