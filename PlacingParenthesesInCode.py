# Проверить, верно ли расставлены скобки. Если нет, то вывести индекс первой ошибки (start_index=1).

stack = []
stack_number_correct = []
stack_number_invalid = []
correct_string, invalid_string = "([{", ")]}"
cnt_operation = 0

for i in input():
    cnt_operation += 1
    if i in correct_string:
        stack.append(i)
        stack_number_correct.append(cnt_operation)
    else:
        if i in invalid_string:
            stack_number_invalid.append(cnt_operation)
            if len(stack) == 0:
                break
            else:
                if invalid_string.index(i) != correct_string.index(stack.pop()):
                    break
                else:
                    stack_number_correct.pop()
                    stack_number_invalid.pop()

if len(stack_number_correct) == 0 and len(stack_number_invalid) == 0:
    print("Success")
else:
    if len(stack_number_invalid) != 0:
        print(stack_number_invalid[-1])
    else:
        print(stack_number_correct[-1])