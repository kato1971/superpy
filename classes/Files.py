from os.path import abspath, exists
import csv
from functions.export_report import make_dir


class Files():
    
    def __init__(self, filename='', columns=[]):

        if filename == '':
            raise ValueError("The 'filename' argument is required")
        elif len(columns) == 0:
            raise ValueError(
                "The 'columns' argument requires at least one column")

        self.filename = filename

        # Create directory if needed
        make_dir('files')

        self.filepath = abspath(f'./files/{self.filename}')
        self.columns = columns
        self.columncount = len(columns)
        
        self.create()
        self.read()


    def read(self):
        data = []
        try:
            with open(self.filepath, 'r+', newline='') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                for row in reader:
                    rowdata = {}
                    for column in self.columns:
                        rowdata[column] = row[column]
                    data.append(rowdata)

        except OSError:
            raise OSError(
                f"Unable to read file from '{self.filepath}'")
        except:
            raise Exception(
                f"Unable to process file '{self.filepath}'")
        self.data = data
        self.rowcount = len(data)


    def write(self):
        try:
            with open(self.filepath, 'w+', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.columns, delimiter=',')
                writer.writeheader()
                for row in self.data:
                    writer.writerow(row)

        except OSError:
            raise OSError(
                f"Unable to save file to '{self.filepath}'")
        except:
            raise Exception(
                f"Unable to process file '{self.filepath}'")
        

    def add(self, row={}):

        if not isinstance(row, dict):
            raise TypeError("The 'row' argument is a dictionary of properties")

        # Validate column names
        for column in row:
            if column not in self.columns:
                raise ValueError(
                    f"Column '{column}' is not a valid property for this file")

        # Validate required columns
        for column in self.columns:
            if column not in row:
                raise ValueError(
                    f"Column '{column}' is a required property for this file")

        self.data.append(row)
        self.rowcount = len(self.data)

        try:
            # Append row to existing csvfile for quick writes
            with open(self.filepath, 'a+', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.columns, delimiter=',')
                writer.writerow(row)

        except OSError:
            raise OSError(
                f"Unable to add data to file '{self.filepath}'")
        except:
            raise Exception(
                f"Unable to process file '{self.filepath}'")
        

    def create(self):

        try:
            # Create a new file if needed
            if not exists(self.filepath):
                self.data = []
                self.write()

        except OSError:
            raise OSError(
                f"Unable to save to file '{self.filepath}'")