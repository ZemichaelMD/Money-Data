from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.


def read(request, pk):
    income = models.Income.objects.get(id=pk)
    context = {'income': income}
    return render(request, 'mymoney/list.html', context)


def index(request):
    expences = models.Expense.objects.all()
    context = {'expences': expences}
    return render(request, 'mymoney/list.html', context)


def addFromExel(request):
    import xlrd
    import datetime
    from .models import Expense

    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'templates/mymoney/MoneyData.xls')

    book = xlrd.open_workbook(file_path)

    # getting the workbook
    sheet_expence = book.sheet_by_name('Expences')
    sheet_income = book.sheet_by_name('Income')
    sheet_account = book.sheet_by_name('Accounts')

    # printing how many rows the workbook has
    # print(sheet.nrows)

    data = {}

    for i in range(sheet.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet.row_values(i)

        #print each Row
        #print(row_header_set)

        # print nested cells
        # for cell in row:
        # print (cell)

        # This returns the pure data!!
        try:
            #Grabbing Date
            date = int(row_header_set[0])
            #convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))

            data = {'Date': date_as_datetime}

            #Datetime Converter to Django Date time
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware

            exexpence_date_formated = make_aware(date_as_datetime)

            #Add Expence
            p = Expense(expense_date = exexpence_date_formated, expense_category=str(row_header_set[1]),
                         expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                         expense_note=str(row_header_set[4]))
            p.save()

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

    done = "Done adding..."
    context = {'done': done}
    print(data)
    return render(request, 'mymoney/done.html', context)
    '''JSON
    {
        {Date: the date, Category: Lost, Amount: 120.0, Reason: Lost or unknown}
    }'''

    # count += 1

    '''for sheet in book.sheets():
        print (sheet.name)'''

    '''
    read as date

    import datetime, xlrd
    book = xlrd.open_workbook("myexcelfile.xls")
    sh = book.sheet_by_index(0)
    a1 = sh.cell_value(rowx=0, colx=0)
    a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(a1, book.datemode))
    print 'datetime: %s' % a1_as_datetime

    '''