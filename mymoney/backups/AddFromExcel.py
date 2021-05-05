#the url pattern
urlpatterns = [
    path('adddata', views.addFromExel, name="addfromexel"),
]


#done.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Done</title>
</head>
<body>
{{ done }}
{% for data in added_data %}
    <ul> <li>{{ data }}</li></ul>
{% endfor %}
</body>
</html>


#the adding function
def addFromExel(request):
    import xlrd
    import datetime
    from .models import Expense

    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'templates/mymoney/../templates/mymoney/MoneyData.xls')
    book = xlrd.open_workbook(file_path)

    added_data = []

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
            my_expence_account = models.MoneyAccount.objects.filter(account_name="Cash")

            models.Expense.objects.create(expense_date = exexpence_date_formated, expense_category=str(row_header_set[1]),
                         expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                         expense_note=str(row_header_set[4]),expense_account=my_expence_account[0])
            print("done adding Expence" + str(row_header_set[3]))
            added_data.append("done adding Expence :" + str(row_header_set[3]))

        except Exception as e:
            print(e)
            pass

    #Adding Income
    sheet_income = book.sheet_by_name('Income')

    # printing how many rows the workbook has
    print(sheet_income.nrows)

    for j in range(sheet_income.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_income.row_values(j)

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
            my_income_account = models.MoneyAccount.objects.filter(account_name=str(row_header_set[1]))

            models.Income.objects.create(income_date=expence_date_formated, income_amount=float(row_header_set[2]),
                              income_description=str(row_header_set[3]),income_account=my_income_account[0])
            print("done adding" + str(row_header_set[3]))
            added_data.append("done adding Income :" + str(row_header_set[3]))

        except Exception as e:
            print(e)
            pass

    #Adding Transfers
    sheet_transfers = book.sheet_by_name('Transfers')

    # printing how many rows the workbook has
    print(sheet_transfers.nrows)

    for k in range(sheet_transfers.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_transfers.row_values(k)

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
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware

            exexpence_date_formated = make_aware(date_as_datetime)

            # Add Transfer
            transferedfrom = models.MoneyAccount.objects.filter(account_name=str(row_header_set[1]))
            transferedto = models.MoneyAccount.objects.filter(account_name=str(row_header_set[2]))

            #print(str(row_header_set[3])+' From : '+transferedfrom[0].account_name+' to: '+transferedto[0].account_name)
            #print(exexpence_date_formated)
            models.Transfers.objects.create(transfer_date=exexpence_date_formated,
                                            transfer_from=transferedfrom[0],
                                            transfer_to=transferedto[0],
                                            transfer_amount=float(row_header_set[3]),
                                            transfer_reason=str(row_header_set[4]))
            print('done!')
            added_data.append("done adding Transfer :" + str(row_header_set[3])+' From : '+transferedfrom[0].account_name+' to: '+transferedto[0].account_name)
        except Exception as e:
            print(e)
            pass

    print ("Done adding...")
    context = {'added_data': added_data}
    return render(request, 'mymoney/done.html', context)