import json
from datetime import datetime
from config import ROOT_DIR


def load_operations(path):
    with open(path) as file:
        operations_list = json.load(file)
        return operations_list


def executed_operations(operations_list):
    exec_ops = []

    for operation in operations_list:
        if isinstance(operation, dict) and 'state' in operation and operation['state'] == 'EXECUTED':
            exec_ops.append(operation)

    return exec_ops


def sorted_date(executed_operations):
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def formatted_date(operation):
    date = datetime.strptime(operation, '%Y-%m-%dT%H:%M:%S.%f')
    date = date.strftime('%d.%m.%Y')
    return date


def hidden_numbers(requisites: str):
    if requisites is None or not requisites.strip():
        return "Нет данных"
    else:
        splitted_reqs = requisites.split()
        card_number = splitted_reqs[-1]
        if requisites.lower().startswith("счет"):
            hided_number = f"**{card_number[-4:]}"
        else:
            hided_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return f"{" ".join(splitted_reqs[:-1])} {hided_number}"


def formatted_operations(sorted_ops):
    all_lines = []

    for operation in sorted_ops:
        date = formatted_date(operation['date'])
        description_op = operation['description']
        line_one = f"{date} {description_op}"

        from_who = hidden_numbers(operation.get('from', ' '))
        to_whom = hidden_numbers(operation['to'])
        line_two = f"{from_who} -> {to_whom}"

        oper_sum = operation['operationAmount']['amount']
        oper_curr = operation['operationAmount']['currency']['name']
        line_three = f"{oper_sum} {oper_curr}"

        all_lines.append(f"{line_one}\n{line_two}\n{line_three}\n")

    return '\n'.join(all_lines)
