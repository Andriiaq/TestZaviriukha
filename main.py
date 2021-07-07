import pandas as pd

acme_worksheet = pd.read_csv('acme_worksheet.csv')
list_employee_names = acme_worksheet['Employee Name'].drop_duplicates().to_list()

list_dates = []
for i in list_employee_names:
    list_dates.append(', '.join(acme_worksheet.loc[acme_worksheet['Employee Name'] == i, 'Date']))

list_work_hours = []
for i in list_employee_names:
    list_work_hours.append(round(acme_worksheet.loc[acme_worksheet['Employee Name'] == i, 'Work Hours'].sum(), 1))

new_acme_worksheet = pd.DataFrame({'Employee Name' : list_employee_names, 'Date' : list_dates, 'Work Hours' : list_work_hours})
new_acme_worksheet.to_csv('new_acme_worksheet.csv', index=False)