import yaml  # Loads the YAML reader

with open("config.yml", "r") as file:  # Opens the config file
    config = yaml.safe_load(file)  # Reads YAML values

print(config["app_name"])  # Prints the application name
print(config["app_version"])  # Prints the application version
