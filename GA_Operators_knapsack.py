import random
import copy

class chromosome:
    def __init__(self,length,weights,values):
        self.length = length
        self.weights =weights
        self.values = values
        self.genes = [None]*length
        for i in range(length):
            self.genes[i] = random.choice([0,1])
        self.fitness = self.evaluate()
        
    def evaluate(self):
        fitness = 0
        total_weight = 0
        for i in range(len(self.genes)):
            if self.genes[i] ==1:
                total_weight += self.weights[i]
        if total_weight <= 32:
            for i in range(len(self.genes)):
                if self.genes[i]==1:
                    fitness += self.values[i]
            return fitness
        else:
            return fitness   

class Crossover:
    
    def One_point(parent1,parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        if random.random() < 0.85:
            crossover_point = random.randint(0,len(parent1.genes))
            
            child1.genes[crossover_point:] = parent2.genes[crossover_point:]
            child2.genes[crossover_point:] = parent1.genes[crossover_point:]

        
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()

        return child1,child2

    def Two_point(parent1,parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)


        if random.random() < 0.85:
            crossover_point1 = random.randint(0,len(parent1.genes))
            crossover_point2 = random.randint(0,len(parent2.genes))

            if crossover_point1 > crossover_point2:
                crossover_point1, crossover_point2 = crossover_point2, crossover_point1

    
            child1.genes[crossover_point1:crossover_point2] = parent2.genes[crossover_point1:crossover_point2]
            child2.genes[crossover_point1:crossover_point2] = parent1.genes[crossover_point1:crossover_point2]

        
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()

        return child1,child2

class mutation:
    def flip_mutation(chromo):
        
        index = random.randint(0,len(chromo.genes)-1)
        if random.random() < 0.20:
            
            if chromo.genes[index]:
                chromo.genes[index] = 0
            else:
                chromo.genes[index] = 1

            chromo.fitness = chromo.evaluate()
        return chromo

    


class Parent_Selection:

    def binary_tour(Pop, tour_size, parent_count):
        Parents = []
        for i in range(parent_count):
            Teams = []
            for j in range(tour_size):
                Teams.append(random.choice(Pop))
            Parents.append(max(Teams,key=lambda x:x.fitness))
        return Parents
    
    def select_best(pop,parent_count):
        Parents = []
        Sorted_Pop = sorted(pop,key=lambda x:x.fitness,reverse = True)
        for i in range(parent_count):
            Parents.append(Sorted_Pop[i])
        return Parents

    def random(pop, parent_count):
        Parents = []
        for i in range(parent_count):
            Parents.append(random.choice(pop))
        return Parents

