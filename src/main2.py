import pickle

def load_elevation_data(filepath):
    """Load elevation data from a pickle file."""
    with open(filepath, 'rb') as file:
        data = pickle.load(file)
    return data

def get_city_elevation(data, state, city):
    """Get the elevation of a city from the loaded data."""
    try:
        state_data = data[state]
        elevation = state_data[city]
        return elevation
    except KeyError:
        return None

def adjust_time_for_elevation_and_wattage(min_time, max_time, elevation, wattage):
    """Adjust microwave time based on elevation and wattage."""
    elevation_factor = 1 + (elevation / 1000) * 0.05
    wattage_factor = 1000 / wattage  # Assuming 1000W as standard wattage
    average_time = (min_time + max_time) / 2
    adjusted_time = average_time * elevation_factor * wattage_factor
    return round(adjusted_time)

if __name__ == "__main__":
    filepath = 'full_state_cities_elevation.pickle'  # Update this path as necessary
    data = load_elevation_data(filepath)
    
    # User inputs for location
    state = input("Enter the name of the state: ")
    city = input("Enter the name of the city: ")
    elevation = get_city_elevation(data, state, city)
    
    if elevation is not None:
        # Additional user inputs for microwave adjustment
        wattage = int(input("Enter your microwave's wattage: "))
        min_time = int(input("Enter the minimum recommended time (in seconds): "))
        max_time = int(input("Enter the maximum recommended time (in seconds): "))
        
        # Calculate and display adjusted time
        adjusted_time = adjust_time_for_elevation_and_wattage(min_time, max_time, elevation, wattage)
        print(f"Adjusted microwave time: {adjusted_time} seconds.")
    else:
        print("Elevation data for the specified city/state could not be found.")
