import pandas as pd
from bs4 import BeautifulSoup


def get_all_text(items):
    result = []

    for item in items:
        try:
            result.append(item.get_text())
        except:
            continue

    return result


def parse_html_thead(html_table):
    thead = html_table.find('thead')
    row = thead.find('tr')

    result = get_all_text(row)
    result = list(filter(lambda e: e != '\n', result))

    return result


def parse_html_body(html_table):
    thead = html_table.find('tbody')
    rows = thead.find_all('tr')
    result = []

    for row in rows:
        parsed_row = get_all_text(row)
        parsed_row = list(filter(lambda e: e != '\n', parsed_row))
        result.append(parsed_row)

    return result


def create_csv(header, rows, csv_name):
    df = pd.DataFrame(data=rows, columns=header)
    df.set_index('Product ID (#)', inplace=True)
    df.to_csv(csv_name)


def html_table_to_csv(html_file_name, csv_file_name):
    soup = BeautifulSoup(open(html_file_name, encoding='utf-8'), 'html.parser')
    table = soup.find('table')
    thead = parse_html_thead(table)
    tbody = parse_html_body(table)
    create_csv(thead, tbody, csv_file_name)


if __name__ == '__main__':
    html_table_to_csv('../fifth_task.html', '../outputs/output_5.csv')
