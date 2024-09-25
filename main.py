#Lab 2: Liv and Lucas
#CS151
#Purpose: Create a program that will determine the expected population in the future
#Prompt user to input how many seconds between births
seconds_births = float(input("How many seconds between births? "))
print("")
#Prompt user to input how many seconds between deaths
seconds_deaths = float(input("How many seconds between deaths? "))
print("")
#Prompt user to input how many seconds between immigration
seconds_immigration = float(input("How many seconds between immigration? "))
print("")
#Prompt user to input the current population
current_population = float(input("What is the current population? "))
print("")
#Prompt user to input how many years in the future they want to predict
years_future = int(input("How many years in the future? "))
print("")
#Calculate the population change
population_change = int((1/seconds_births - 1/seconds_deaths + 1/seconds_immigration)*3156000)
print("")
#Calculate the future population
future_population = int(population_change + current_population)
print("")
#Output the population change
print(f"The predicted population change over {years_future} years is" , population_change)
#Output the predicted population
print("The predicted population is " , future_population)
#Output if the population will increase or decrease
if population_change > current_population:
    print("the population will increase")
else:
    print("the population will decrease")

