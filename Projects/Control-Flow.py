def analyze_smoker(smoker_status):
    """
    Analyzes the smoker status and provides a recommendation.

    Parameters:
    smoker_status (int): The smoker status of an individual. 1 represents a smoker, 0 represents a non-smoker.

    Returns:
    None
    """
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    """
    Calculates the estimated insurance cost based on the given parameters.

    Parameters:
    - name (str): The name of the person.
    - age (int): The age of the person.
    - sex (int): The sex of the person (0 for female, 1 for male).
    - num_of_children (int): The number of children the person has.
    - smoker (int): Indicates whether the person is a smoker (0 for non-smoker, 1 for smoker).

    Returns:
    - estimated_cost (float): The estimated insurance cost in dollars.
    """
    estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

# My estimate insurance cost
my_insurance_cost = estimate_insurance_cost(name="Stefan", age=21, smoker=0, sex=1, num_of_children=0)