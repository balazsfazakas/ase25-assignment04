#simulated database for meals
meals = { 
    1: {"Name": "Tomato Soup", "Ingredients": ["Tomato", 'Onion', "Salt"], "Category": "Vegan"}, 
    2: {"Name": "Muffin", "Ingredients": ["Sugar", "Baking Powder", "Cinnamon", "Flour"], "Category": "Vegan"},
    3: {"Name": "Lentil Soup", "Ingredients": ["Lentil", "Carrot", "Vinegar"], "Category": "Gluten-Free"},
    4: {"Name": "Cheeseburger", "Ingredients": ["Bun", "Cheese", "Beef Patty"], "Category": "Quick Meals"} }

#str for search_by, accepts either str or list for search_for
def search(search_by, search_for):
    result_meals = []
    for meal_id, meal in meals.items():
        if isinstance(search_for, list):
            if set(search_for).issubset(meal[search_by]):
                result_meals.append(meal)
        else:
            if meal[search_by] == search_for:
                result_meals.append(meal)
    return result_meals

def main():
    if (len(meals) == 0):
        return
    first_key = next(iter(meals))
    inner_keys = list(meals[first_key].keys()) #aspects that a meal can be searched by
    while(True):
        search_by = input(f"What would you like to search for? {inner_keys}: ") #list what is valid to search for
        if (not (search_by in inner_keys)):
            print("Invalid Input")
            continue
        if (search_by == "Ingredients"): #input is a list
            search_for = input(f"Enter {search_by} separated by commas: ").split(", ")
        else: #input is a str
            search_for = input(f"Enter {search_by} without commas: ")

        result_meals = search(search_by, search_for)
        #print results of the search
        if len(result_meals) == 0:
            print(f"No such {search_by} found")
        for result in result_meals:
            print(result)
        return

if __name__ == "__main__": #provide main() as entry
    main()