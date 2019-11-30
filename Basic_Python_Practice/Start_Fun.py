##what is the function 
## Functions are  convenient way to divide your code into useful blocks, make it more readable and reuse our code.

## function method 

#block_head:
#     1_block line 
#     2_block line 
#     ....



def my_function_with_args(username, greeting):
    print ("Hello, %s, From my function!, I wish you,%s"%(username, greeting))

my_function_with_args("Dileep", "Happy new year")
        
def sum_two_numbers(a, b):
    return a + b

x = sum_two_numbers(5,6)
print(x)

def list_benefits():2
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return " %s is a benefit of functions!"% benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

