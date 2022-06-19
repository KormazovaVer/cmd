from class_stack_1 import Stack
#проверка соответствия скобок
def check_brackets(stack, string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')

    for i in string:
        if i in brackets_open:
            stack.push(i)
        if i in brackets_closed:    
            if len(stack.stack_list) == 0:
                return 'Небалансированно'
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack.stack_list[-1] == open_bracket:
                stack.pop()  
            else: 
                return 'Небалансированно'
    return 'Сбалансированно'        




