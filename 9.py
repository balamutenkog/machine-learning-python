first_name = ["Анна", "Борис", "Александр", "Денис"]
age =[]
age.append(42)
all_ages = [32, 41, 29]
all_ages = all_ages + age
name_and_age = zip(first_name, all_ages)
print (list(name_and_age))