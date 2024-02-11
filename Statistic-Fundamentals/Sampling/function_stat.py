import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


def choose_statistic(x, sample_stat_text):
    """
    Calculate the statistic based on the input text.

    Parameters:
    x (array-like): Input data
    sample_stat_text (str): The statistic to calculate. Options are "Mean", "Minimum", "Variance", "Median", "Mode", "Maximum".

    Returns:
    float: The calculated statistic
    """
    # Dictionary mapping text to corresponding numpy function
    stats_dict = {
        "Mean" : np.mean,
        "Minimum" : np.min,
        "Variance" : np.var,
        "Median" : np.median,
        "Mode" : np.mod,
        "Maximum" : np.max
    }
    
    # Check if the input text is valid
    if sample_stat_text not in stats_dict:
        raise ValueError(f'Invalid input. Expected one of: {",".join(stats_dict.keys())}')
    
    # Calculate and return the statistic
    return stats_dict[sample_stat_text](x)

def population_distribution(population_data):
    # plot the population distribution
    sns.histplot(population_data, stat="density")
    # informative title for the distribution
    plt.title(f"Population Distribution")
    # remove None label
    plt.xlabel("")
    plt.show()
    plt.clf()


def sampling_distribution(population_data, samp_size, stat):
    
    # list that will hold all the sample statistics
    sample_stats = [choose_statistic(np.random.choice(population_data, samp_size, replace=False), stat) for _ in range(500)]
    
    # calculate population statistic
    pop_statistic = round(choose_statistic(population_data, stat), 2)
    
    # plot the sampling distribution
    sns.histplot(sample_stats, stat="density")
    
    # informative title for the sampling distribution
    plt.title(
        f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}"
    )
    
    # plot the population statistic
    plt.axvline(
        pop_statistic, color="g", linestyle="dashed", label=f"Population {stat}"
    )
    
    # plot the mean of the chosen sample statistic for the sampling distribution
    plt.axvline(
        np.mean(sample_stats),
        color="orange",
        linestyle="dashed",
        label=f"Mean of the Sample {stat}s",
    )
    
    plt.legend()
    plt.show()
    plt.clf()

# ---
import numpy as np
import scipy.stats as st

def simulation_binomial_test(observed_successes, n, p, alternative_hypothesis):
    """
    Perform a binomial test simulation.

    Parameters:
    observed_successes (int): The number of observed successes.
    n (int): The number of trials.
    p (float): The hypothesized probability of success.
    alternative_hypothesis (str): The alternative hypothesis ('less', 'greater', or 'two-sided').

    Returns:
    float: The p-value of the test.
    """

    # Generate the simulated null distribution
    null_outcomes = np.array([np.sum(np.random.choice(['y', 'n'], size=n, p=[p, 1-p]) == 'y') for _ in range(10000)])

    # Calculate a one-sided or two-sided p-value
    if alternative_hypothesis == 'less':
        p_value = np.mean(null_outcomes <= observed_successes)
    elif alternative_hypothesis == 'greater':
        p_value = np.mean(null_outcomes >= observed_successes)
    elif alternative_hypothesis == 'two-sided':
        p_value = 2 * min(np.mean(null_outcomes <= observed_successes), np.mean(null_outcomes >= observed_successes))
    else:
        raise ValueError("alternative_hypothesis must be 'less', 'greater', or 'two-sided'")

    # Return the p-value
    return p_value

if __name__ == "__main__":
    # Test the result using simulation_binomial_test function
    p_value_1 = simulation_binomial_test(45, 500, .1, alternative_hypothesis='less')

    # Test the result using binom_test function from scipy
    binom_result = st.binomtest(45, 500, .1, alternative='less')
    p_value_2 = binom_result.pvalue

    # Display the p-values
    print(f"simulation p-value: {p_value_1}")
    print(f"binom_test p-value: {p_value_2}")