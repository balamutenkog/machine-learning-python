def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age (2049, 1993)
dads_age = calc_age(2049, 1965)
print("«Мне " + str(my_age) + " лет, а моему отцу " + str(dads_age) + " лет»")