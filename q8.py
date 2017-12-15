registers = {}
with open('in.txt', 'r') as in_file:
    for line in in_file:
        register, operation, amount, _, depends_on_register, logic_operation,\
            logic_operand = line.strip().split()
        amount, logic_operand = int(amount), int(logic_operand)
        registers.setdefault(register, 0)
        registers.setdefault(depends_on_register, 0)

        perform = False
        if logic_operation == "==":
            if registers[depends_on_register] == logic_operand:
                perform = True
        elif logic_operation == ">=":
            if registers[depends_on_register] >= logic_operand:
                perform = True
        elif logic_operation == "<=":
            if registers[depends_on_register] <= logic_operand:
                perform = True
        elif logic_operation == ">":
            if registers[depends_on_register] > logic_operand:
                perform = True
        elif logic_operation == "<":
            if registers[depends_on_register] < logic_operand:
                perform = True
        elif logic_operation == "!=":
            if registers[depends_on_register] != logic_operand:
                perform = True

        if perform:
            if operation == "inc":
                registers[register] += amount
            else:
                registers[register] -= amount

values = registers.values()
print max(values)
