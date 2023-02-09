class Stack:
    def __init__(self, stack_list1):
        self.stack_list = stack_list1

    def is_empty(self):
        if self.stack_list:
            return 'False'
        else:
            return 'True'

    def push(self, i):
        self.stack_list.append(i)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def bracket_balance(text, brackets='()[]{}'):
    opening = brackets[::2]
    closing = brackets[1::2]
    my_list = []
    for i in text:
        if i in opening:
            atr_stack = Stack(my_list)
            atr_stack.push(opening.index(i))
        elif i in closing:
            atr_stack = Stack(my_list)
            if my_list and atr_stack.peek() == closing.index(i):
                atr_stack.pop()
            else:
                print('Несбалансированно')
                return 'Несбалансированно'
    print('Сбалансированно')
    return 'Сбалансированно'


if __name__ == '__main__':
    text1 = input('Введите строку со скобками: ')
    bracket_balance(text1)
