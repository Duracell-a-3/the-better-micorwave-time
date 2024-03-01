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

if __name__ == "__main__":
    filepath = 'full_state_cities_elevation.pickle'  # Update this path as necessary
    data = load_elevation_data(filepath)
    
    # User inputs
    state = input("Enter the name of the state: ")
    city = input("Enter the name of the city: ")
    
    # Get and display elevation
    elevation = get_city_elevation(data, state, city)
    if elevation is not None:
        print(f"The elevation of {city}, {state} is {elevation} meters.")
    else:
        print("The elevation data for the specified city/state could not be found.")
