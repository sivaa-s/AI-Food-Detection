import json
import pickle

if __name__ == '__main__':
    #Initializing a list of dishes
    dishes = {}
    # Opening the pickle file and loading the data
    with open('recipe1m_small.pkl', 'rb') as f:
        data = pickle.load(f)
    # Opening the given input file
    with open("input_file.json") as input_file:
        input = json.load(input_file)
    # Initializing a recipe list to store recipes
    recipes_list = []
    for recipe in data:
        if input.get("dish type") in recipe.get('title'):
            recipes_list.append(recipe)
    # Initializing an ingredients list to store ingredients
    ingredients_list = []
    for each_recipe in recipes_list:
        for ingredient in each_recipe.get("ingredients"):
            if ingredient not in ingredients_list and ingredient not in input.get("ingredients"):
                ingredients_list.append(ingredient)
    length = len(recipes_list)
    # Initializing a dictionary to return each ingredient probability
    probability_dict = {}
    to_check = input.get("ingredients")
    for ingredient in ingredients_list:
        count = 0
        count1 = 0
        input.get("ingredients").append(ingredient)
        for recipe in recipes_list:
            if ingredient in recipe.get("ingredients"):
                count +=1
            if(set(input.get("ingredients")).issubset(set(recipe.get("ingredients")))):
                count1 +=1
        input.get("ingredients").pop()
        probability = count1/length
        probability_dict[ingredient] = probability
    max_probability = max(probability_dict, key=probability_dict.__getitem__)
    print(f'Ingredient with the highest probability is:', max_probability)
    print(f'Probability of the highest ingredient is:', probability_dict.get(max_probability))