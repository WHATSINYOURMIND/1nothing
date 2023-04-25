import random
print("Create a list of random integers:")
population = range(0, 100) #defining range from 0 to 100
nums_list = random.sample(population, 10) #generating 10  nos in popultaion variable
print(nums_list)
no_elements = 4
print("\nRandomly select",no_elements,"multiple items from the said list:")
result_elements = random.sample(nums_list, no_elements) #selecting 4 elemenets from numslist
print(result_elements)
no_elements = 8
print("\nRandomly select",no_elements,"multiple items from the said list:")
result_elements = random.sample(nums_list, no_elements)
print(result_elements)
