import numpy as np

# تعداد خیابان‌ها
num_streets = 10

# طول و تراکم خیابان‌ها
lengths = np.array([10, 5, 5, 10, 10, 7, 7, 9, 8, 20])
densities = np.array([17.03, 32.90, 18.09, 35.73, 52.20, 90.25, 79.67, 21.41, 18.50, 4.81])

def calculate_fitness(population):
    fitness_scores = []
    for individual in population:
        fitness_score = np.sum(individual * densities * lengths)
        fitness_scores.append(fitness_score)
    return fitness_scores

def selection(population, fitness_scores):
    probabilities = fitness_scores / np.sum(fitness_scores)
    selected_indices = np.random.choice(range(len(population)), size=len(population), p=probabilities)
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutation(individual):
    for i in range(len(individual)):
        if np.random.random() < mutation_rate:
            individual[i] = np.random.randint(1, 3)
    return individual

# پارامترهای الگوریتم ژنتیک
population_size = 5000
num_generations = 100
mutation_rate = 0.01

# دریافت ورودی از کاربر
band_types_input = input("\nplease enter your 10 streets lanes number 1 or 2 to show best solution and fitness score. (example 1,1,2,2,1,2): ")
band_types = [int(band_type) for band_type in band_types_input.split(",")]

# تولید جمعیت اولیه
population = []
for _ in range(population_size):
    individual = np.random.choice(band_types, size=num_streets)
    population.append(individual)

# اجرای الگوریتم ژنتیک
for generation in range(num_generations):
    fitness_scores = calculate_fitness(population)
    population = selection(population, fitness_scores)
    new_population = []
    while len(new_population) < population_size:
        parent1 = population[np.random.randint(0, len(population))]
        parent2 = population[np.random.randint(0, len(population))]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_population.append(child1)
        new_population.append(child2)
    population = new_population

# یافتن بهترین راه حل
fitness_scores = calculate_fitness(population)
best_solution = population[np.argmax(fitness_scores)]

print("Best Solution:")
print(best_solution)
print("\nFitness Score:")
print(np.max(fitness_scores))
y_or_n = input("please enter to exit")
if y_or_n.lower() != 'y':
    continue_program = False
