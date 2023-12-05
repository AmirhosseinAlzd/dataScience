import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

flag = True

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi > 30:
        category = "Overfat"
    elif 25 <= bmi <= 30:
        category = "Fat"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 17 <= bmi < 18.5:
        category = "Thin"
    else:
        category = "OverThin"
    return category

# Input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

# Calculate BMI and categorize
bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)

# Calculate the target BMI for the "Normal" category
target_bmi = 22.5  # You can adjust this value as needed for your definition of "Normal" BMI

# Calculate Normal Weight
normal_weight = target_bmi * (height ** 2)

# Calculate extra Weight
extra_weight = abs(weight - normal_weight) if weight > normal_weight else abs(normal_weight - weight)

# Display the recommendation
if category == 'Overfat' or category == 'Fat':
    recommendation = f"To be in the 'Normal' BMI category, you may need to decrease your weight by {extra_weight:.2f} kg."
elif category == 'OverThin' or category == 'Thin':
    flag = False
    recommendation = f"To be in the 'Normal' BMI category, you may need to increase your weight by {extra_weight:.2f} kg."
else:
    recommendation = "You are already in the 'Normal' BMI category."

# Pie chart
labels = ['Overfat', 'Fat', 'Normal', 'Thin', 'Over Thin']
sizes = [10, 20, 40, 20, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

explode = (0.1, 0, 0, 0, 0) if category == "Overfat" else (0, 0.1, 0, 0, 0) if category == "Fat" \
    else (0, 0, 0.1, 0, 0) if category == "Normal" else (0, 0, 0, 0.1, 0) if category == "Thin" else (0, 0, 0, 0, 0.1)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
plt.title('BMI Distribution')

# Save the first page
with PdfPages('report.pdf') as pdf:
    pdf.savefig()
    plt.close()

    # Bar plot for user's information
    user_info = [height * 100, weight, bmi]
    labels_user = ['Height', 'Weight', 'BMI']

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)  # Subplot for user's information

    plt.bar(labels_user, user_info, color=['#66b3ff', '#66b3ff', '#ffcc99'])
    plt.xlabel('User Information')
    plt.ylabel('Values')
    plt.title('User Information')

    # Bar plot for normal person's information
    normal_person_info = [height * 100, weight - extra_weight, target_bmi] if flag \
        else [height * 100, weight + extra_weight, target_bmi]
    labels_normal = ['Height', 'N_Weight', 'N_BMI']

    plt.subplot(1, 2, 2)  # Subplot for normal person's information

    plt.bar(labels_normal, normal_person_info, color=['#66b3ff', '#66b3ff', '#ffcc99'])
    plt.xlabel('Normal Person Information')
    plt.ylabel('Values')
    plt.title('Normal Person Information')

    plt.tight_layout()  # Adjust layout for better spacing

    # Save the second page
    pdf.savefig()
    plt.close()

    # Linear diagram for fitness progress
    months = ['Azar', 'Dey', 'Bahman', 'Esfand', 'Farvardin']
    piece_bmi_difference = extra_weight / 4

    plt.figure()
    plt.ylim(weight - 30, weight + 30)

    if flag:
        fitness_progress = [weight, weight - piece_bmi_difference, weight - 2 * piece_bmi_difference,
                            weight - 3 * piece_bmi_difference, weight - 4 * piece_bmi_difference]

        plt.plot(months, fitness_progress, marker='s', linestyle='--', color='orange')
        plt.xlabel('Months')
        plt.ylabel('BMI Improvement')
        plt.title('Fitness Progress Over 4 Months')

        # Customize y-axis ticks and labels for more detail
        plt.yticks(np.arange(weight - 30, weight + 31, 2.5))
    else:
        fitness_progress = [weight, piece_bmi_difference + weight, 2 * piece_bmi_difference + weight,
                            3 * piece_bmi_difference + weight, 4 * piece_bmi_difference + weight]

        plt.plot(months, fitness_progress, marker='s', linestyle='--', color='orange')
        plt.xlabel('Months')
        plt.ylabel('Your Weight')
        plt.title('Fitness Progress Over 4 Months')

        # Customize y-axis ticks and labels for more detail
        plt.yticks(np.arange(weight - 30, weight + 31, 2.5))

    # Save the third page
    pdf.savefig()
    plt.close()