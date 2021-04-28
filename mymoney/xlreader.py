import xlrd
import datetime
'''from .models import Expense
from .models import Income
from .models import MoneyAccount
from .models import ToBePaid'''

class Readerxl():

    def printData(set,date):
        print("Date" + str(date))
        print("Category : " + str(set[1]))
        print("Amount : " + str(set[2]))
        print("Reason : " + str(set[3]))
        print("Remark : " + str(set[4]))
        x = "*** Done Adding ***"
        print(x)


    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'templates/mymoney/MoneyData.xls')

    book = xlrd.open_workbook(file_path)

    # getting the workbook
    sheet_expence = book.sheet_by_name('Expences')
    sheet_income = book.sheet_by_name('Income')
    sheet_account = book.sheet_by_name('List of Accounts')
    sheet_transfers = book.sheet_by_name('Transfers')
    sheet_tobepaid = book.sheet_by_name('To be paid')

    # printing how many rows the workbook has
    print(sheet_transfers.nrows)

    for i in range(sheet_income.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_transfers.row_values(i)

        #print each Row
        #print(row_header_set)

        # print nested cells
        '''for cell in row_header_set:
            print (cell)'''

        # This returns the pure data!!
        try:
            #Grabbing Date
            date = int(row_header_set[0])
            #convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))

            #Datetime Converter to Django Date time
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware
            expence_date_formated = make_aware(date_as_datetime)

            #Add Expence
            '''p = Expense(expense_date = exexpence_date_formated, expense_category=str(row_header_set[1]),
                         expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                         expense_note=str(row_header_set[4]))
            p.save()'''

            #print Data
            print("Date" + str(date_as_datetime))
            print("Category : " + str(row_header_set[1]))
            print("Amount : " + str(row_header_set[2]))
            print("Reason : " + str(row_header_set[3]))
            print("Remark : " + str(row_header_set[4]))
            x = "*** Done Adding ***"
            print(x)
        except:
            pass

    done = "Done!"
    print(done)