RIGHT_BORDER = 200**2


def mean(num1, num2):
    return (num1 + num2) / 2


def apply_filter_condition(e):
    return e > 0 and e*e < RIGHT_BORDER


def filter_list(l):
    return list(filter(apply_filter_condition, l))


def fill_na(text_line):
    parsed = text_line.split(' ')
    result = [int(parsed[0])]

    for i in range(1, len(parsed) - 1):
        if parsed[i] == 'N/A':
            result.append(mean(result[i-1], int(parsed[i+1])))
        else:
            result.append(int(parsed[i]))

    result.append(int(parsed[-1]))

    return result


if __name__ == '__main__':
    with open('../third_task.txt') as input_file:
        output_lines = list(map(fill_na, input_file.readlines()))
        output_lines = list(map(filter_list, output_lines))
        output_lines = list(map(sum, output_lines))
        with open('../outputs/output_3.txt', 'w') as output_file:
            for line in output_lines:
                output_file.write(f'{line}\n')
