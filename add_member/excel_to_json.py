
import pyexcel as pe
from zipfile import BadZipfile


field_name = {
    'Campus': 'campus',
    'Employee Status': 'emp_stat',
    'Employee Class': 'emp_class',
    'Name': 'name',
    'Employee Class Long Description': 'emp_class_desc',
    'Current Hire Date': 'hireDate',
    'Position': 'position',
    'Position Title': 'position_title',
    'Position Begin Date': 'pos_beg_date',
    'Position End Date': 'pos_end_date',
    'Department': 'department',
    'Job Suffix': 'job_suffix',
    'Termination Date': 'term_date',
}

name_fields = ['lName', 'fName', 'mName']

def convert_excel_json(content):
    all_dict = []
    try:
        book = pe.get_book(file_content=content,file_type='xlsx')
        for sheet in book:
            temp = sheet.row[2]
            temp = [x for x in temp if x != '']
            sheet.name_columns_by_row(2)
            for i in range(0, sheet.to_records().__len__(), 1):
                row_temp = sheet.row[i]
                a = 0
                valid = True
                while a <= 4 and valid is True:
                    valid = row_temp[a] != ''
                    a += 1

                temp2 = {}
                if valid:
                    for z in range(0, len(temp), 1):
                        if temp[z] != "Name":
                            temp2[field_name[temp[z]]] = sheet[i, z]
                        else:
                            array = [x.rstrip(',.') for x in sheet[i, z].split(' ')]
                            for j in range(0, len(array)):
                                temp2[name_fields[j]] = array[j]

                if temp2:
                    all_dict.append(temp2)
    except BadZipfile:
        all_dict.append({'Error':'The you uploaded is not an excel file'})

    return all_dict