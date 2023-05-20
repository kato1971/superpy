from os import makedirs
from os.path import abspath, exists
import csv
import json
import xlsxwriter

format_date = '%Y%m%d_%H%M%S'

def make_filename(prefix='', suffix=''):
    return f'{prefix}{suffix}'

def report_csv(filename, fieldnames, data):
    directory = 'files/inventory'
    make_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_csv_file(filepath, fieldnames, data)
    return

def report_xlsx(filename, fieldnames, data):
    directory = 'files/inventory'
    make_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_xlsx_file(filepath, fieldnames, data)
    return

def report_json(filename, data):
    directory = 'files/inventory'
    make_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_json_file(filepath, data)
    return

def create_csv_file(filepath, fieldnames, data):
    with open(filepath, 'w+', newline='') as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return

def create_xlsx_file(filepath, headers, data):
    with xlsxwriter.Workbook(filepath) as xlsx_file:
        worksheet = xlsx_file.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers)
        for index, item in enumerate(data):
            row = map(lambda field_id: item.get(field_id, ''), headers)
            worksheet.write_row(row=index + 1, col=0, data=row)
    return

def create_json_file(filepath, data):
    with open(filepath, 'w+') as json_file:
        json.dump(data, json_file, sort_keys=True, indent=4, ensure_ascii=False, default=str)
    return

def make_dir(dir=''):
    if dir == '':
        raise ValueError("A valid directory name is required")
    try:
        if not exists(abspath(f'./{dir}')):
            makedirs(abspath(f'./{dir}'))
    except:
        raise OSError(f"Unable to create directory './{dir}'")
    
    return