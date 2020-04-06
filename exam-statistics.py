grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for grade in grades_input:
        print grade 

print_grades(grades)

def grades_sum(scores):
    total = 0 
    for score in scores:
        total += score 
    return total 

def grades_average(grades_input):
    sumTotal = grades_sum(grades_input)
    averageTotal = sumTotal / float(len(grades_input))
    return averageTotal

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0 
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)