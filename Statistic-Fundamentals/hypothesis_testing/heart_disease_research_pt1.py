# import libraries
import pandas as pd
import numpy as np
import scipy.stats as st

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

print("Patient with heart disease: \n")
# save cholesterol level for patient with heart disease
chol_hd = yes_hd.chol
# print(chol_hd.head())

# calculate mean of the cholesterol level for patient with heart disease
mean_chol_hd = np.mean(chol_hd)
print(f"The mean of cholesterol level for patient with heart disease is: {mean_chol_hd}")
# output: 251.48. This considered a high cholesterol level because it is over 240 mg/dl

# test the hypothesis
# H0: average cholesterol level for people with hd is equal to 240 
# H1: average cholesterol level for people with hd is not equal to 240

# test using two-sample t-test
tstat, pval = st.ttest_1samp(chol_hd, 240)
print(f"The pvalue for patient with heart disease: {round(pval/2, 3)}")
# output: 0.004

"""
Conclusion:
Based on the pval output, the pval is less than the significant threshold (pval < 0.05), so the H0 is rejected and the H1 is accepted (alternative hypothesis) and the average cholesterol for people with heart disease is not equal to 240.
"""

print("\nPatient with no heart disease: \n")
# save the cholesterol level for the patient with no heart disease
chol_no_hd = no_hd.chol

# calculate the mean cholesterol level for patient with no heart disease
mean_chol_no_hd = np.mean(chol_no_hd)
print(f"The mean of cholesterol level for patient with no heart disease is: {mean_chol_no_hd}")
# output: 242.64. This considered a high cholesterol level because it is over 240 mg/dl

# test the hypothesis
# H0: average cholesterol level for people with no hd is equal to 240 
# H1: average cholesterol level for people with no hd is not equal to 240

# test using two-sample t-test
tstat, pval = st.ttest_1samp(chol_no_hd, 240)
print(f"The pvalue for patient with no heart disease: {round(pval/2, 3)}")
# output: 0.264

"""
Conclusion:
Based on the pval output, the pval is higher than the significant threshold (pval > 0.05), so the H0 is accepted and the H1 is rejected (alternative hypothesis) and the average cholesterol for people with no heart disease is equal to 240.
"""

print("\nFasting Blood Sugar (fbs) Analysis\n")

# count the num of patient
num_patients = len(heart)
print(f"The total number of patients is: {num_patients}")
# output: 303

# save the patient with high fbs
high_fbs = heart[heart.fbs == 1]

# calculate the num of patient with high fbs (fbs > 120 mg/dl)
num_high_fbs_patients = len(high_fbs)
print(f"Total patients with high fbs is: {num_high_fbs_patients}")
# output: 45

# calculate expected num of people diagnosed diabetes using the 8% from population
sample_diabetes = round(0.08*303)
print(f"The expected number of patient with a resting blood sugar above 120 mg/dl is {sample_diabetes} people")
# output: 24

# Test the sample taken 
# H0: The sample was drawn from a population where 8% of people have fbs > 120 mg/dl
# H1: The sample was drawn from a population where more than 8% of people have fbs > 120 mg/dl

pval = st.binom_test(x = num_high_fbs_patients, n = num_patients, p = 0.08, alternative='greater')
print(f"The p-value from the binomial test is: {pval}")

"""
Conclusion:
Based on the result of pval, the pval is less than the significant threshold (pval < 0.05), meanings that the null hypothesis (H0) is rejected and the alternative hypothesis (H1) is accepted, so the sample was drawn from the population with more than 8% of people have fbs > 120 mg/dl.
"""