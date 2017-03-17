import statistics

def enrollment_stats(list_of_universities):
    # variables
    total_students  = []
    total_tuition   = []

    # iterate through lists, adding values to a new list
    for university in list_of_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])
    # return variables
    return total_students, total_tuition
        

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['MIT', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569 ],
    ['Yale', 11701, 40500]
    ]

totals = enrollment_stats(universities)

student_total = sum(totals[0])
student_mean = int(statistics.mean(totals[0]))
student_median = int(statistics.median(totals[0]))

tuition_total = sum(totals[1])
tuition_median = int(statistics.median(totals[1]))
tuition_mean = int(statistics.mean(totals[1]))

print('*' * 10)
print("Total students: {}".format(student_total))
print("Total tuition: ${}".format(tuition_total))
print()
print("Student mean: {}".format(student_mean))
print("Student median: {}".format(student_median))
print()
print("Tuition mean: ${}".format(tuition_mean))
print("Tuition median: ${}".format(tuition_median))
print('*' * 10)





    
