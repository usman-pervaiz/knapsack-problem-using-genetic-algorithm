
#Implementing genetic algorithm to solve knapsack problem
import random
import copy
import GA_Operators_knapsack
weights = []
values = []
for i in range(8):
    weights.append(random.randint(1, 15))
    values.append(random.randint(150, 1200))
print("Items weight and values")
item = 0
for i in range(8):
    item += 1
    print("Items:{}    Weight:{}     value:{}".format(item,weights[i],values[i]))

print()
print("Bag Size:",32)
print("\n")


population = [_ for _ in range(10)]

    
for i in range(0,10):
    population[i] = GA_Operators_knapsack.chromosome(8,weights,values)

print('Initial population is:')
for chromosome in population:
    print(chromosome.genes, chromosome.fitness)
    
generation = 1
for gen in range(0,10):
    print("Generation:",generation)
    new_pop = []
    for i in range(0,len(population),2):
        #parent selection
        #parents = GA_Operators_knapsack.Parent_Selection.select_best(population,2)
        #parents = GA_Operators_knapsack.Parent_Selection.random(population,2)
        parents = GA_Operators_knapsack.Parent_Selection.binary_tour(population,2,2)

        print("Parents")
        for chromosome in parents:
            print(chromosome.genes, chromosome.fitness)

        #crossover
        child1,child2 = GA_Operators_knapsack.Crossover.Two_point(parents[0],parents[1])

        print("cross")
        print(child1.genes, child1.fitness)

        print(child2.genes, child2.fitness)

        #mutation
        child1 = GA_Operators_knapsack.mutation.flip_mutation(child1)
        child2 = GA_Operators_knapsack.mutation.flip_mutation(child2)
        
         

        print("Mutation")
        print(child1.genes, child1.fitness)

        print(child2.genes, child2.fitness)


        new_pop.append(child1)
        new_pop.append(child2)
    print('********************')
            
    for chromo in new_pop:
        print(chromo.genes,"            ",chromo.fitness)

    population = GA_Operators_knapsack.Parent_Selection.binary_tour(population+new_pop, 3, len(population))

    print('*********** after post select **********')

    for chromo in population:
        print(chromo.genes,"            ",chromo.fitness)
    generation += 1

best_items = max(population,key=lambda x:x.fitness)
print("\nBest genes:",best_items.genes)
print("Best items to select:")
for i in range(len(best_items.genes)):
    if best_items.genes[i]==1:
        print("Items:{}     weight{}     values:{}".format(i+1,weights[i],values[i]))

