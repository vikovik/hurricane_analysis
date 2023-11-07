from variables import *
# 1       
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

"""
    The function `damages_update` takes a list of damage values and converts them to a standardized
    format.
    
    :param damages: A list of damages, where each element is a string representing the amount of damage
    :return: a list of updated damages.
"""
def damages_update(damages):
    updated_damages = []

    for damage in damages:

        if damage == "Damages not recorded":
            updated_damages.append(damage)

        elif damage[-1] == "M":
            updated_damages.append(float(damage[:-1]) * conversion["M"])

        elif damage[-1] == "B":
            updated_damages.append(float(damage[:-1]) * conversion["B"])

    return updated_damages

# 2 
# Create a Table
"""
    The function "hurricanes_table" creates a dictionary of hurricane data using the provided lists as
    keys and values.
    
    :param names: A list of names of hurricanes
    :param months: A list of the months in which the hurricanes occurred
    :param years: A list of the years in which the hurricanes occurred
    :param max_sustained_winds: The parameter "max_sustained_winds" represents the maximum sustained
    wind speed of each hurricane
    :param areas_affected: The "areas_affected" parameter is a list that contains the areas affected by
    each hurricane. Each element in the list corresponds to a specific hurricane and contains a string
    or a list of strings representing the areas affected by that hurricane
    :param updated_damages: The parameter "updated_damages" is a list that contains the updated damage
    values for each hurricane
    :param deaths: The "deaths" parameter is a list that contains the number of deaths caused by each
    hurricane
    :return: a dictionary called "hurricanes" which contains information about different hurricanes.
"""
def hurricanes_table(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i],
                        "Month": months[i],
                        "Year": years[i],
                        "Max Sustained Wind": max_sustained_winds[i],
                        "Areas Affected": areas_affected[i],
                        "Damage": updated_damages[i],
                        "Deaths": deaths[i]}
        
    return hurricanes

# 3
# Organizing by Year
"""
    The function "hurricanes_by_year" takes a dictionary of hurricanes and organizes them by year.
    
    :param hurricanes: The hurricanes parameter is a dictionary where the keys are the names of
    hurricanes and the values are dictionaries containing information about each hurricane. Each
    hurricane dictionary contains a "Year" key that represents the year the hurricane occurred
    :return: a dictionary where the keys are the years of the hurricanes and the values are lists of
    hurricane data for each year.
"""
def hurricanes_by_year(hurricanes):
    hurricanes_by_year = {}

    for key, value in hurricanes.items():
        current_year = value["Year"]
        current_hurricane = value

        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_hurricane]
            
        else:
            hurricanes_by_year[current_year].append(current_hurricane)

    return hurricanes_by_year

# 4
# Counting Damaged Areas
"""
    The function "counting_damaged_areas" takes a dictionary of hurricanes and returns a dictionary of
    the count of damaged areas for each hurricane.
    
    :param hurricanes: A dictionary containing information about different hurricanes. Each key in the
    dictionary represents the name of a hurricane, and the corresponding value is another dictionary
    containing information about that hurricane. One of the keys in the inner dictionary is "Areas
    Affected", which contains a list of areas that were affected by the hurricane
    :return: a dictionary called "damaged_areas" which contains the count of how many times each area
    has been affected by hurricanes.
"""
def counting_damaged_areas(hurricanes):
    damaged_areas = {}

    for key, value in hurricanes.items():
        current_area = value["Areas Affected"]

        for area in current_area:

            if area not in damaged_areas:
                damaged_areas[area] = 1

            else:
                damaged_areas[area] += 1

    return damaged_areas

# 5 
# Calculating Maximum Hurricane Count
"""
    The function `max_hurricane_count` takes a dictionary `areas_affected_count` as input and returns
    the maximum number of hurricanes and the corresponding area with the maximum count.
    
    :param areas_affected_count: The parameter `areas_affected_count` is a dictionary that contains the
    count of hurricanes in different areas. The keys of the dictionary represent the areas affected by
    hurricanes, and the values represent the count of hurricanes in each area
    :return: a tuple containing the maximum hurricane count and the corresponding area affected.
"""
def max_hurricane_count(areas_affected_count):
    max_hurricane_count = 0
    max_area_affected = ""

    for key, value in areas_affected_count.items():

        if value > max_hurricane_count:
            max_hurricane_count = value
            max_area_affected = key

        else:
            continue

    return max_hurricane_count, max_area_affected

# 6
# Calculating the Deadliest Hurricane
"""
    The function `deadliest_hurricane_count` takes a dictionary of hurricanes and their corresponding
    death tolls, and returns the name of the deadliest hurricane and the number of deaths it caused.
    
    :param hurricanes: The hurricanes parameter is a dictionary where the keys are the names of
    hurricanes and the values are dictionaries containing information about each hurricane. Each inner
    dictionary contains a "Deaths" key with the number of deaths caused by that hurricane
    :return: a tuple containing the name of the deadliest hurricane and the number of deaths caused by
    that hurricane.
"""
def deadliest_hurricane_count(hurricanes):
    max_deaths = 0
    deadliest_hurricane = ""

    for key, value in hurricanes.items():
        current_deaths = value["Deaths"]

        if current_deaths > max_deaths:
            max_deaths = current_deaths
            deadliest_hurricane = key

        else:
            continue

    return deadliest_hurricane, max_deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

"""
    The function "hurricanes_mortality_scale" categorizes hurricanes based on their mortality rating
    using a predefined scale.
    
    :param hurricanes: The hurricanes parameter is a dictionary where the keys are the names of
    hurricanes and the values are dictionaries containing information about each hurricane. Each
    hurricane dictionary should have a 'Deaths' key that represents the number of deaths caused by that
    hurricane
    :return: a dictionary called "rated_hurricanes". This dictionary contains lists of hurricanes
    categorized by their mortality rating. The mortality rating is determined based on the number of
    deaths caused by each hurricane, using a predefined mortality scale.
"""
def hurricanes_mortality_scale(hurricanes):
    rated_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: []}
    
    for key, value in hurricanes.items():
        deaths = value['Deaths']
        mortality_rating = max(
            rating for rating, upper_bound in mortality_scale.items() if deaths > upper_bound
        )
        rated_hurricanes[mortality_rating].append({key: value})

    return rated_hurricanes

# 8 Calculating Hurricane Maximum Damage

"""
    The function calculates the hurricane with the maximum recorded damage from a dictionary of
    hurricanes.
    
    :param hurricanes: The hurricanes parameter is a dictionary where the keys are the names of
    hurricanes and the values are dictionaries containing information about each hurricane. Each inner
    dictionary contains a key "Damage" which represents the recorded damage caused by the hurricane
    :return: a tuple containing the name of the hurricane with the maximum damage and the maximum damage
    value.
"""
def calculate_max_damage(hurricanes):
    max_damage = 0
    max_damage_hurricane = ""

    for key, value in hurricanes.items():
        current_damage = value["Damage"]

        if current_damage == "Damages not recorded":
            continue

        elif int(current_damage) > max_damage:
            max_damage = current_damage
            max_damage_hurricane = key

        else:
            continue

    return max_damage_hurricane, max_damage

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

"""
    The function `hurricane_damage_scale` categorizes hurricanes based on their recorded damage into
    different damage rating levels.
    
    :param hurricanes: The "hurricanes" parameter is a dictionary that contains information about
    different hurricanes. Each key in the dictionary represents the name of a hurricane, and the
    corresponding value is another dictionary that contains information about that hurricane, including
    the damage caused by the hurricane
    :return: a dictionary called "rated_hurricanes". This dictionary contains lists of hurricanes
    categorized by their damage rating. The keys of the dictionary represent the damage rating, ranging
    from 0 to 4. The values of the dictionary are lists of dictionaries, where each dictionary
    represents a hurricane and its corresponding information.
"""
def hurricane_damage_scale(hurricanes):
    rated_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: []}

    for key, value in hurricanes.items():
        damage = value['Damage']    

        if damage == "Damages not recorded":
            damage_rating = 0

        else:
            damage_amount = int(damage)
            damage_rating = max(
                rating for rating, upper_bound in damage_scale.items() if damage_amount > upper_bound
            )    

        rated_hurricanes[damage_rating].append({key: value}) 

    return rated_hurricanes