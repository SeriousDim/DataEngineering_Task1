import re


def get_all_words(text: str):
    return re.findall(r'[A-Za-z\']+', text)


def get_words_beginning_with_vowel(text: str):
    # 1) Y считаем гласной
    # 2) Слова с дефисом считаем двумя словами
    return re.findall(r'\b[AaEeIiUuYyOo][a-z\']*\b', text)


if __name__ == '__main__':
    with open('../first_task.txt') as input_file:
        text = ''.join(input_file.readlines())
        vowel_words = get_words_beginning_with_vowel(text)
        words = get_all_words(text)
        vowel_fraction = len(vowel_words) / len(words) * 100
        with open('../outputs/output_1_b.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(f'Кол-во слов, начинающихся на гласную: {len(vowel_words)}\n')
            output_file.write(f'Доля слов, начинающихся на гласную: {vowel_fraction}%\n')
