from validator_1 import check_brackets
from class_stack_1 import Stack

def main():
    #задача №1
    my_stack = Stack()
    

    print(my_stack.isEmpty())

    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    print(my_stack.pop())
    print(my_stack.isEmpty())
    print(my_stack.size())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())


    #задача №2
    str1 = '[{([[[<>]]])(<>)(){}}]' 
    str2 = ']()(){<>}[[()]]' 
    str3 = '{{[()]}}'
    str4 = '{[[[[((()))]]<]>]}'
 
    print()
    print(check_brackets(my_stack, str1))
    print(check_brackets(my_stack, str2))
    print(check_brackets(my_stack, str3))
    print(check_brackets(my_stack, str4))



if __name__ == '__main__':
    main()   
    