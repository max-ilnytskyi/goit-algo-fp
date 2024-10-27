import random
import matplotlib.pyplot as plt
import pandas as pd


def monte_carlo_simulation(num_trials):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    probabilities = {k: (v / num_trials) * 100 for k, v in sum_counts.items()}

    return sum_counts, probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color="skyblue", edgecolor="black")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability (%)")
    plt.title("Monte Carlo Simulation of Dice Roll Sums")
    plt.xticks(sums)
    plt.grid(True)
    plt.show()


# Number of trials for the simulation
num_trials = 100000

sum_counts, probabilities = monte_carlo_simulation(num_trials)

df = pd.DataFrame(list(probabilities.items()), columns=["Sum", "Probability (%)"])

print(df)

plot_probabilities(probabilities)

analytical_probs = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

df["Analytical Probability (%)"] = df["Sum"].map(analytical_probs)

print("\nComparison of Monte Carlo and Analytical Probabilities:")
print(df)
