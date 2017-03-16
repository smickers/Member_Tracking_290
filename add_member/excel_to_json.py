
import pyexcel as pe
from zipfile import BadZipfile

# Dictionary used for associating the excel file's column header to the correct key that's being used
#   by the Person model
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
    """
        Method that converts the excel file to JSON
    """
    all_dict = [] # create a holder for all the dictionaries
    try:
        book = pe.get_book(file_content=content,file_type='xlsx')  # open the excel book in memory
        for sheet in book:  # loop for each sheet found in the excel book
            temp = sheet.row[2]  # store the values of the third row (This row identifies the column)
            temp = [x for x in temp if x != '']  # Remove the row last remaining row that contains an empty string
            sheet.name_columns_by_row(2)
            for i in range(0, sheet.to_records().__len__(), 1):  # loop for each row
                row_temp = sheet.row[i]  # store a row to a temporary variable
                a = 0
                valid = True
                while a <= 4 and valid is True:  # checks to see if the first four row is not empty
                    valid = row_temp[a] != ''
                    a += 1

                temp2 = {}
                if valid:  # If the row is valid
                    for z in range(0, len(temp), 1):  # loop each column of the row
                        if temp[z] != "Name":   # If the current column does not belong to the 'Name' column
                            temp2[field_name[temp[z]]] = sheet[i, z]  # create a key value pair based on the field name and its value
                        else: # If the current column belong sto the 'Name' column
                            array = [x.rstrip(',.') for x in sheet[i, z].split(' ')] # split the names into an array
                            for j in range(0, len(array)): # loop the resulting array
                                temp2[name_fields[j]] = array[j]  # assign the key/val pair using the name_fields as key
                if temp2:
                    all_dict.append(temp2)
    except BadZipfile:
        all_dict.append({'Error':'The you uploaded is not an excel file'})

    return all_dict