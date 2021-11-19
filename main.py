from pprint import pprint


def main():
    states, alphabet, initial_state, final_states, transitions = read_data("FA.in")
    option = print_menu()
    while option:
        match option:
            case '1':
                print(states)
            case '2':
                print(alphabet)
            case '3':
                print(transitions)
            case '4':
                print(final_states)
            case '5':
                print(initial_state)
            case '6':
                verify_sequence(initial_state,final_states,transitions)
            case _:
                break
        option = print_menu()


def verify_sequence(initial_state,final_states, transitions):
    string = input()
    result = process_string(string, initial_state, transitions)
    if result in final_states:
        print("accepted")
    else:
        print("not accepted")


def process_string(string, initial_state, transitions):
    sequence = string.split()
    current_state = initial_state
    for index in range(0, len(sequence)):
        pair = '' + current_state + ',' + sequence[index]
        current_state = transitions[pair]
    return current_state


def read_data(file_name):
    file = open(file_name)
    data = file.read()
    lines = data.split("\n")
    index = 0
    for line in lines:
        newl = line.split()
        lines[index] = newl
        index += 1
    Q = format_data(lines[0])
    E = format_data(lines[1])
    F = format_data(lines[2])
    q0 = lines[3][2]
    S = {}
    for index in range(5, 5 + len(Q) * len(E)):
        elem = lines[index]
        t1 = elem[1]
        t2 = elem[3]
        t3 = elem[6]
        key = '' + t1 + ',' + t2
        S[key] = t3
    return Q, E, q0, F, S


def format_data(line):
    data = []
    index = 0
    while index < len(line) and line[index] != "[":
        index += 1
    index += 1
    elem = ''
    while index < len(line):
        if line[index] != "," and line[index] != ']':
            elem += line[index]
        else:
            data.append(elem)
            elem = ''
        index += 1
    if elem:
        data.append(elem)
    return data


def print_menu():
    print("Select option:")
    print("1. print the set of states")
    print("2. print the alphabet")
    print("3. print all the transitions")
    print("4. print the set of final states")
    print("5. print the initial state")
    print("6. check if string is accepted")
    return input()


if __name__ == '__main__':
    main()
