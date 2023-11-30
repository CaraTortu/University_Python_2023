from os.path import exists, isdir
from typing import Dict, Optional
from pandas.errors import ParserError
import pandas as pd
import json
import io

# Constants
CSV_MOVIES = "./assignment_files/top1000Films.csv"


def write_to_file(filename: str, contents: str) -> None:
    """
    Writes some contents to a file.

    Parameters:
        filename: The file to write to.
        contents: The string to write into the file.

    Returns: None
    """

    try:
        with open(filename, "w") as f:
            f.write(contents)
    except FileNotFoundError:
        print("[-] ERROR: File path is invalid.")


def get_file_contents(filename: str, extension: str) -> Optional[str]:
    """
    Returns the contents of a file if found.
    If the file does not exist, it will return "None"

    Parameters:
        filename: The file path
        extension: The expected file extension

    Returns: Optional[str]
    """

    # Check if file exists so no Exceptions are raised.
    if not exists(filename):
        print("[-] ERROR: File does not exist. Please try again")
        return

    # Check that it is a file and not a folder
    if isdir(filename):
        print("[-] ERROR: Path supplied is a folder. Please supply a file")
        return

    if not filename.endswith(extension):
        print(f"[-] ERROR: File is not a valid {extension} file")
        return

    with open(filename) as file:
        return file.read()


def convert_csv_file_to_json(filename: str) -> Optional[Dict[str, str]]:
    """
    Reads CSV file content and translates it to JSON (dict).

    If the file does not exist, it will return None

    Parameters:
        filename: The CSV file path

    Returns: Dictionary with the CSV contents translated if the file exists, else None.
    """

    csv_file_contents = get_file_contents(filename, "csv")

    # Check to see if we could read the file
    if not csv_file_contents:
        return

    # Read the CSV and translate to JSON
    try:
        csv_dataframe = pd.read_csv(io.StringIO(csv_file_contents))
    except ParserError:
        print("[-] ERROR: invalid CSV file.")
        return

    json_string = csv_dataframe.to_json(orient='records', indent=4)

    # Conversion may fail so we make sure to check if it went well.
    if not json_string:
        print("[-] ERROR: Couldn't translate to JSON.'")
        return

    # Return the dictionary
    return json.loads(json_string)


def print_menu() -> None:
    """
    Prints the selection menu to stdout.
    """

    print()
    print("1. Display contents of any csv file on screen")
    print("2. Display contents of any text file on screen")
    print("3. Display contents of any JSON file on screen")
    print("4. Read the contents of top1000Films.csv and write to json file top1000Films.json")
    print("5. Create a list of unique actors")
    print("6. Search on keyword")
    print("7. Write top films of a given year to file")
    print("8. Generate frequency distribution report")
    print("0. Quit")


def main() -> None:
    """
    Main function of the program.
    """

    print_menu()

    option_chosen = input("Choose an option: ")

    # Validate input
    if not option_chosen.isdigit() or int(option_chosen) < 0 or int(option_chosen) > 9:
        print("[-] Invalid option.")
        return

    # Make it a number
    option_chosen = int(option_chosen)

    # Option 0. Quit
    if option_chosen == 0:
        exit(0)

    # Option 1, 2, 3. Read file and print its contents
    if option_chosen in [1, 2, 3]:
        file_to_read = input("What file would you like to read?: ")
        
        # Check for the extension the user selected
        number_to_extension = ["csv", "txt", "json"]

        # Get the file contents
        file_contents = get_file_contents(file_to_read, number_to_extension[option_chosen-1])

        # Print the contents if the file exists
        if file_contents:
            print(file_contents)

    # Option 4. Read the CSV and write to JSON
    if option_chosen == 4:
        # Get the file contents and convert it to a string
        json_contents = convert_csv_file_to_json(CSV_MOVIES)
        json_string = json.dumps(json_contents)

        # Write the string to a file
        write_to_file("top1000Films.json", json_string)
        print("[+] top1000Films.json was successfully written!")
        return

    # Option 5. Create a list of unique actors
    if option_chosen == 5:
        actors = set()
        json_contents = convert_csv_file_to_json(CSV_MOVIES)

        # We know that the contents are not None since we checked at the start of the program.
        assert json_contents

        for movie in json_contents:
            for actor in movie.get("Actors").split(","):  # pyright: ignore
                actors.add(actor.strip())

        # Print all the actors
        print(actors)
        return

    # Option 6. Search on keyword
    if option_chosen == 6:
        found = 0
        json_contents = convert_csv_file_to_json(CSV_MOVIES)
        needle = input("Keyword to look for: ")

        # We know that the contents are not None since we checked at the start of the program.
        assert json_contents

        for movie in json_contents:
            # Map all the values from the dictionary to a string,
            # then join it all together to find the needle in the haystack
            haystack = "".join(map(str, movie.values()))  # pyright: ignore

            if needle in haystack:
                found += 1
                # Print the beautified version of the JSON
                print(json.dumps(movie, indent=4))

        if found == 0:
            print("[i] No results found.")

        return

    # Option 7. Write top films of a given year to file
    if option_chosen == 7:
        top_films_of_year = {"Title": [], "Director": [], "Rank": []}
        json_contents = convert_csv_file_to_json(CSV_MOVIES)
        year_to_find = input("What year would you like to look for?: ")

        # We know that the contents are not None since we checked at the start of the program.
        assert json_contents

        # Check if its a digit or not
        if not year_to_find.isdigit():
            print("[-] ERROR: Invalid year supplied")
            return

        year_to_find = int(year_to_find)

        # Find the movies with such year
        for movie in json_contents:
            if year_to_find == movie["Year"]:  # pyright: ignore
                top_films_of_year["Title"].append(movie["Title"])  # pyright: ignore
                top_films_of_year["Director"].append(movie["Director"])  # pyright: ignore
                top_films_of_year["Rank"].append(movie["Rank"])  # pyright: ignore

        # Translate the dictionary to a pandas DataFrame
        top_films_of_year = pd.DataFrame(top_films_of_year)

        # If we have no results then inform the user
        if len(top_films_of_year) == 0:
            print("[i] No results found")
            return

        # Add the contents to a file
        string_top_films = f"Top Films {year_to_find}\n"
        string_top_films += top_films_of_year.to_string(index=False, justify="left")
        filename = f"topFilms{year_to_find}.txt"
        write_to_file(filename, string_top_films)
        print(f"[i] Wrote results to {filename}")
        return

    # Option 8. Generate a frequency distribution report
    if option_chosen == 8:
        json_contents = convert_csv_file_to_json(CSV_MOVIES)

        # We know that the contents are not None since we checked at the start of the program.
        assert json_contents

        # Add the statistics for each director
        directors_statistics = {}
        for movie in json_contents:
            if not directors_statistics.get(movie["Director"]): # pyright: ignore
                directors_statistics[movie["Director"]] = 1     # pyright: ignore
                continue

            directors_statistics[movie["Director"]] += 1        # pyright: ignore

        
        write_to_file("freqDist.json", json.dumps(directors_statistics, indent=4))
        print("[i] freqDist.json written!")
        return


if __name__ == "__main__":
    # Make sure the CSV file exists before runnning
    if not exists(CSV_MOVIES):
        print("[-] ERROR: The CSV film dataset could not be found")
        exit(1)

    while True:
        main()

