# Day 12: Leonardo's Monorail


def execute_cpy(registers, instruction):
    source, target = instruction.split()[1:]

    try:
        registers[target] = int(source)
    except ValueError:
        registers[target] = registers[source]


def execute_inc(registers, instruction):
    register = instruction.split()[1]

    registers[register] += 1


def execute_dec(registers, instruction):
    register = instruction.split()[1]

    registers[register] -= 1


def calculate_jump(registers, instruction):
    value, jump = instruction.split()[1:]

    try:
        value = int(value)
    except ValueError:
        value = registers[value]

    if value != 0:
        return int(jump)
    else:
        return 1


def main(registers):
    instruction_pointer = 0
    instructions = open('input.txt').read().splitlines()

    while instruction_pointer < len(instructions):
        instruction = instructions[instruction_pointer]

        if instruction.startswith('cpy'):
            execute_cpy(registers, instruction)
        elif instruction.startswith('inc'):
            execute_inc(registers, instruction)
        elif instruction.startswith('dec'):
            execute_dec(registers, instruction)
        else:
            instruction_pointer += calculate_jump(registers, instruction)
            continue

        instruction_pointer += 1

    print(registers['a'])

main({'a': 0, 'b': 0, 'c': 0, 'd': 0})
main({'a': 0, 'b': 0, 'c': 1, 'd': 0})
