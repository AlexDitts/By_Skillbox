with open('names.txt', 'w') as file:
    file.write('alex\n')
    file.write('li\n')
    file.write('john\n')
    file.write('po\n')
    file.write('iten\n')

with open('names.txt') as file:
    with open('log_errors.txt', 'a') as log_file:
        line_count = 0
        for name in file:
            current_name = name.strip()
            line_count += 1
            print(current_name)
            try:
                if len(current_name) < 3:
                    raise ValueError
            except ValueError:
                log_file.write(('The name {} in {} string is too short.\n'.format(current_name, line_count)))
