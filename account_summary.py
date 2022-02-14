from datetime import timedelta, date

#Account summary
#Average date of transaction
def transaction_summary(start_date, end_date):
    for n in range (int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date =  date(2022, 1, 1)
end_date = date(2022, 2, 1)
for transac_date in transaction_summary(start_date, end_date):



    print(transac_date.strftime("%D"))
