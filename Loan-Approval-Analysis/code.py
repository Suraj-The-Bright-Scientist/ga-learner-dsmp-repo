# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)





# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())


#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index =['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc = np.mean)


# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status)*100
percentage_nse = (loan_approved_nse/Loan_Status)*100


# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)

big_loan_term = len(banks[(banks['Loan_Amount_Term'] >= 25*12)])




# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()




# code ends here


