from function_stat import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# task 1: load in the spotify dataset
spotify_data = pd.read_csv('./Statistic-Fundamentals/Sampling/data/spotify_data.csv')
# task 2: preview the dataset
print(spotify_data.head())
# # task 3: select the relevant column
# song_tempos = spotify_data['tempo']
# # task 5: plot the population distribution with the mean labeled
# population_distribution(song_tempos)
# # task 6: sampling distribution of the sample mean
# sampling_distribution(song_tempos, 30, "Mean")
# # task 8: sampling distribution of the sample minimum
# sampling_distribution(song_tempos, 30, "Minimum")
# # task 10: sampling distribution of the sample variance
# sampling_distribution(song_tempos, 30, "Variance")
# # task 13: calculate the population mean and standard deviation
# population_mean = np.mean(song_tempos)
# population_std = np.std(song_tempos) 
# # task 14: calculate the standard error
# samp_size = 30
# standard_error = population_std / (samp_size ** 0.5)
# # task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
# prob_avg_140 = stats.norm.cdf(140, population_mean, standard_error) 
# print(prob_avg_140)
# # task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
# prob_greater_150 = 1 - stats.norm.cdf(150, population_mean, standard_error)
# print(prob_greater_150)

# EXTRA

# select the column danceability
dance = spotify_data['danceability']

# plot the population distribution with the mean labeled
population_distribution(dance)

# sampling distribution of the sample mean
sampling_distribution(dance, 50, "Mean")

# check the unique value
print(dance.value_counts)

# calculate the population mean and standard deviation
population_mean = np.mean(dance)
population_std = np.std(dance) 
# calculate the standard error
samp_size = 50
standard_error = population_std / (samp_size ** 0.5)

# # calculate the probability of observing an average danceability of 0.40 or lower from a sample of 30 songs
prob_avg_140 = stats.norm.cdf(0.4, population_mean, standard_error) 
print(prob_avg_140)
# # task 16: calculate the probability of observing an average tempo of 0.60 or higher from a sample of 30 songs
prob_greater_150 = 1 - stats.norm.cdf(0.6, population_mean, standard_error)
print(prob_greater_150)
