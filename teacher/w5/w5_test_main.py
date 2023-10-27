import w5_test_module
import hello_package.hello_greet

print(dir(w5_test_module))

w5_test_module.greeting("Jonathan")

a = w5_test_module.person1["age"]
print(a)

hello_package.hello_greet.SayHello("Jonathan")