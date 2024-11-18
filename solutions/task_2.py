def text_line_to_int_list(text_line):
    transformed = text_line.split(' ')
    return list(map(lambda e: int(e), transformed))


def filter_negatives(int_list):
    return list(filter(lambda e: e > 0, int_list))


if __name__ == '__main__':
    with open('../second_task.txt') as input_file:
        lists = list(map(text_line_to_int_list, input_file.readlines()))
        lists = list(map(filter_negatives, lists))
        sums = list(map(sum, lists))
        total = sum(sums)
        with open('../outputs/output_2.txt', 'w') as output_file:
            for s in sums:
                output_file.write(f'{s}\n')
            output_file.write('\n')
            output_file.write(f'{total}\n')
