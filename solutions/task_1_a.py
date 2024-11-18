import re


def sort_dict(d: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}


def get_word_frequency(text: str) -> dict[str, int]:
    # 1) Слова с дефисом считаем двумя словами
    # 2) Слова с апострофом считаем одним словом
    result = dict()

    words = re.findall(r'[A-Za-z\']+', text)
    words = map(lambda w: w.lower(), words)

    for word in words:
        if word not in result.keys():
            result[word] = 0
        result[word] += 1

    return sort_dict(result)


def output_frequency(d: dict[str, int]):
    return map(lambda key: f'{key}:{d[key]}', d.keys())


if __name__ == '__main__':
    input_file = open('../first_task.txt')
    word_frequency = get_word_frequency(''.join(input_file.readlines()))
    input_file.close()
    with open('../outputs/output_1_a.txt', 'w') as output_file:
        output_lines = output_frequency(word_frequency)
        for line in output_lines:
            output_file.write(f'{line}\n')
