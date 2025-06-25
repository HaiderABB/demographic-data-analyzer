import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("/home/haider/Desktop/Office/Python/Projects/boilerplate-demographic-data-analyzer/adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Higher vs Lower education rich percentage
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_edu['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_edu['salary'] == '>50K').mean() * 100, 1)

    # 5. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich percentage among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_rich_min_workers = len(min_workers[min_workers['salary'] == '>50K'])
    rich_percentage_min_hours = round((num_rich_min_workers / len(min_workers)) * 100, 1)

    # 7. Country with highest percentage of rich
    rich_people = df[df['salary'] == '>50K']
    total_per_country = df['native-country'].value_counts()
    rich_per_country = rich_people['native-country'].value_counts()
    rich_percentage_per_country = (rich_per_country / total_per_country) * 100

    highest_earning_country = rich_percentage_per_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_per_country.max(), 1)

    # 8. Most popular occupation for rich Indians
    top_IN_occupation = rich_people[rich_people['native-country'] == 'India']['occupation'].value_counts().idxmax()

    # Print output if needed
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage_min_hours}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage_min_hours,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
