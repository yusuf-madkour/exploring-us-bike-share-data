import time
import pandas as pd
import pprint
from os import system
import prompts

CITY_DATA = {
    "Chicago": "data/chicago.csv",
    "New York City": "data/new_york_city.csv",
    "Washington": "data/washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """

    city = prompts.city_prompt.launch()

    _filter = prompts.filter_prompt.launch()

    if _filter == "Month":
        month = prompts.month_prompt.launch()
        day = "All"

    elif _filter == "Day":
        day = prompts.day_prompt.launch()
        month = "All"

    elif _filter == "Both":
        month = prompts.month_prompt.launch()
        day = prompts.day_prompt.launch()

    else:
        month, day = "All", "All"

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and/or day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # drop the unused 'Unnamed' column
    df = df.drop("Unnamed: 0", axis=1)
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # extract month, day of week and hour from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour.astype(str)

    # filter by month if applicable
    if month != "All":
        # filter by month to create the new dataframe
        df = df.loc[df["month"] == month]

    # filter by day of week if applicable
    if day != "All":
        # filter by day of week to create the new dataframe
        df = df.loc[df["day"] == day]

    return df


def get_most_popular(series):
    """
    Gets the most repeated data entry in a pandas Series and its occurrences' count

    Args:
        (Series) series - Pandas Series from which the most repeated data entry is returned
    Returns:
        most_popular - the most common data entry in series
        count - the count of occurrences of most_popular in series
    """
    most_popular = series.mode()[0]
    count = sum(series == most_popular)
    return most_popular, count


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nDisplaying the most frequent times of travel...\n")
    start_time = time.time()

    # Ignoring getting the most popular month when the data is already filtered by month
    if len(df["month"].unique()) > 1:
        most_popular_month, month_count = get_most_popular(df["month"])
        print(f"Most popular month: {most_popular_month}, Count: {month_count}")
    # Ignoring getting the most popular day when the data is already filtered by day
    if len(df["day"].unique()) > 1:
        most_popular_day, day_count = get_most_popular(df["day"])
        print(f"Most popular day: {most_popular_day}, Count: {day_count}")

    most_popular_hour, hour_count = get_most_popular(df["hour"])
    print(f"Most popular trip start hour: {most_popular_hour}, Count: {hour_count}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nDisplaying the most Popular stations\n")
    start_time = time.time()

    most_popular_start_station, start_station_count = get_most_popular(
        df["Start Station"]
    )
    print(f"Most commonly used start station: {most_popular_start_station}")
    print(f"It has been used {start_station_count} times\n")

    most_popular_end_station, end_station_count = get_most_popular(df["End Station"])
    print(f"Most commonly used end station: {most_popular_end_station}")
    print(f"It has been used {end_station_count} times\n")

    df["Combined Stations"] = (
        df["Start Station"].apply(lambda x: x + " and ") + df["End Station"]
    )
    most_popular_combined_station, combined_station_count = get_most_popular(
        df["Combined Stations"]
    )
    print(
        f"Most common combination of start station and end station: {most_popular_combined_station}"
    )
    print(f"They have been used {combined_station_count} times\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating trip duration...\n")
    start_time = time.time()

    print("Total trip duration: {} seconds".format(df["Trip Duration"].sum()))

    print("Average trip duration: {} seconds".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nDisplaying user stats...\n")
    start_time = time.time()

    subscribers = len(df[df["User Type"] == "Subscriber"])
    customers = len(df[df["User Type"] == "Customer"])

    print(f"Subscribers: {subscribers}")
    print(f"Customers: {customers}\n")

    if "Gender" in df.columns:
        males = len(df[df["Gender"] == "Male"])
        females = len(df[df["Gender"] == "Female"])
        print(f"Males: {males}")
        print(f"Females: {females}\n")

    if "Birth Year" in df.columns:
        print(f"Earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"Most common year of birth: {int(df['Birth Year'].mode()[0])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def display_records(df):
    """
    Displays individual data records from DataFrame by pretty printing

    Args:
        (DataFrame) df - dataframe to display records from
    """
    i = 0
    pretty_printer = pprint.PrettyPrinter(indent=2)
    while True:
        _display = prompts.yes_no_prompt(
            "\nWould you like to view individual trip data?\n"
        ).launch()
        if not _display:
            break
        pretty_printer.pprint(df.iloc[i : i + 5].to_dict(orient="records"))
        i += 5


def main():
    """Runs an interactive session to get input from the user and display requested data"""

    while True:
        print("Let's explore some US bikeshare data!")
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # printing filter
        print(f"Month: {month}, Day: {day}")
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_records(df)
        restart = prompts.yes_no_prompt("\nWould you like to restart?\n").launch()
        if not restart:
            break
        system("clear")


if __name__ == "__main__":
    main()
