class Stack:
    '''
    абстрактный тип данных, представляющий собой список элементов,
    организованных по принципу LIFO (англ. last in — first out,
    «последним пришёл — первым вышел»). Чаще всего принцип работы 
    стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, 
    нужно снять верхнюю. Или с магазином в огнестрельном оружии
    (стрельба начнётся с патрона, заряженного последним).
    '''
    stack_list = [4, 7, 8]
  
    #def __init__(self, lst):
        #self.list = lst

    #проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        if len(Stack.stack_list) == 0:
            return True
        return False
    
    #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, data):
        self.data = data
        if self.data:
            Stack.stack_list.append(self.data)
            return self.data
        else:
            print('Trying to push an empty list')

    #удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        try:
            last_el = Stack.stack_list.pop()
            return last_el
        except IndexError:
            return 'Trying to pop from empty list'

    #возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        try:
            return Stack.stack_list[-1]
        except IndexError:
            return 'Trying to peek from empty list'

    #возвращает количество элементов в стеке.
    def size(self):
        return len(Stack.stack_list)