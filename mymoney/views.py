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

    #Adding Expences
    sheet_expence = book.sheet_by_name('Expences')

    # printing how many rows the workbook has
    # print(sheet.nrows)

    for i in range(sheet_expence.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_expence.row_values(i)

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

            #Datetime Converter to Django Date time
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware

            exexpence_date_formated = make_aware(date_as_datetime)

            #Add Expence
            models.Expense.objects.create(expense_date = exexpence_date_formated, expense_category=str(row_header_set[1]),
                         expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                         expense_note=str(row_header_set[4]))
            print("done adding" + str(row_header_set[3]))

        except:
            pass

    #Adding Income
    sheet_income = book.sheet_by_name('Income')

    # printing how many rows the workbook has
    # print(sheet.nrows)

    for i in range(sheet_income.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_income.row_values(i)

        # print each Row
        #print(row_header_set)

        # print nested cells
        # for cell in row:
        # print (cell)

        # This returns the pure data!!
        try:
            # Grabbing Date
            date = int(row_header_set[0])
            # convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))


            # Datetime Converter to Django Date time
            from django.utils.timezone import make_aware
            expence_date_formated = make_aware(date_as_datetime)

            # Add income
            try:
                models.Income.objects.create(income_date=expence_date_formated, income_amount=float(row_header_set[2]),
                              income_description=str(row_header_set[3]))
            except: print("error!")
            print("done adding" + str(row_header_set[3]))

        except:
            pass

    '''
    #Adding Accounts
    sheet_account = book.sheet_by_name('Accounts')

    # printing how many rows the workbook has
    # print(sheet.nrows)

    for i in range(sheet_account.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_account.row_values(i)

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

        except:
            pass


        # Adding Transfers
        sheet_account = book.sheet_by_name('Accounts')

        # printing how many rows the workbook has
        # print(sheet.nrows)

        for i in range(sheet_account.nrows):
            # row_header_set contains all the data as a set
            row_header_set = sheet_account.row_values(i)

            # print each Row
            # print(row_header_set)

            # print nested cells
            # for cell in row:
            # print (cell)

            # This returns the pure data!!
            try:
                # Grabbing Date
                date = int(row_header_set[0])
                # convert exel Date to Python
                date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))

                data = {'Date': date_as_datetime}

                # Datetime Converter to Django Date time
                import datetime
                from django.conf import settings
                from django.utils.timezone import make_aware

                exexpence_date_formated = make_aware(date_as_datetime)

                # Add Expence
                p = Expense(expense_date=exexpence_date_formated, expense_category=str(row_header_set[1]),
                            expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                            expense_note=str(row_header_set[4]))
                p.save()

            except:
                pass'''

    done = "Done adding..."
    context = {'done': done}
    return render(request, 'mymoney/done.html', context)