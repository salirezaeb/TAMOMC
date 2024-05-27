import numpy as np

# تعداد خیابان‌ها
num_streets = 10

# طول و تراکم خیابان‌ها
lengths = np.array([10, 5, 5, 10, 10, 7, 7, 9, 8, 20])
densities = np.array([17.03, 32.90, 18.09, 35.73, 52.20, 90.25, 79.67, 21.41, 18.50, 4.81])

# پارامترهای الگوریتم ژنتیک
population_size = 5000
mutation_rate = 0.01

# تابع محاسبه امتیاز فیتنس
def calculate_fitness(population):
    fitness_scores = []
    for individual in population:
        fitness_score = np.sum(individual * densities * lengths)
        fitness_scores.append(fitness_score)
    return fitness_scores

# تابع تولید جمعیت اولیه
def generate_initial_population():
    population = []
    for _ in range(population_size):
        individual = np.random.randint(1, 3, size=num_streets)
        population.append(individual)
    return population

# تابع تکامل جمعیت
def evolve_population(population):
    fitness_scores = calculate_fitness(population)
    best_fitness = np.max(fitness_scores)
    new_population = selection(population, fitness_scores)
    while True:
        population = new_population
        fitness_scores = calculate_fitness(population)
        new_population = selection(population, fitness_scores)
        if np.max(fitness_scores) == best_fitness:
            break
        else:
            best_fitness = np.max(fitness_scores)
    return population

# تابع انتخاب جمعیت
def selection(population, fitness_scores):
    probabilities = fitness_scores / np.sum(fitness_scores)
    selected_indices = np.random.choice(range(len(population)), size=len(population), p=probabilities)
    return [population[i] for i in selected_indices]

# تابع اجرای الگوریتم ژنتیک
def run_genetic_algorithm():
    population = generate_initial_population()
    population = evolve_population(population)
    fitness_scores = calculate_fitness(population)
    best_solution = population[np.argmax(fitness_scores)]
    best_fitness = np.max(fitness_scores)
    return best_solution, best_fitness

# تکرار حل مسئله تا نیل به حالت پایدار تراکم
previous_best_fitness = 0
while True:
    best_solution, best_fitness = run_genetic_algorithm()
    if best_fitness == previous_best_fitness:
        break
    else:
        previous_best_fitness = best_fitness

# نمایش نتایج
print("Best Solution:")
print(best_solution)
print("Best Fitness:")
print(best_fitness)
input('\n please enter to exit...')