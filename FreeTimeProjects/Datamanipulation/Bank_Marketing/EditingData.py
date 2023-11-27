import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo


class FilteringData:
    # fetch dataset
    # https://archive.ics.uci.edu/dataset/222/bank+marketing
    bank_marketing = fetch_ucirepo(id=222)

    # data (as pandas dataframes)
    X = bank_marketing.data.features
    y = bank_marketing.data.targets

    # Noted to be not needed and should be removed, thinking about removing month
    drop = ["duration", "day_of_week", "contact"]
    X = X.drop(drop, axis=1)

    # filtering and editing whole dataset
    # Convert features and targets to Pandas DataFrames
    X_df = pd.DataFrame(X, columns=bank_marketing.feature_names)
    y_df = pd.DataFrame(y, columns=bank_marketing.targets_names)

    # Combine X and y into a single DataFrame
    combined_df = pd.concat([X_df, y_df], axis=1)

    # Job.
    # 3 categories: retired, unemployed, working.
    # Remove unknown ones
    working = ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'self-employed', 'services',
               'technician']
    unemployed = ["unemployed", "student"]
    combined_df["job"].replace(working, "working", inplace=True)
    combined_df["job"].replace(unemployed, "unemployed", inplace=True)
    combined_df["job"].replace("unknown", np.nan, inplace=True)
    combined_df = combined_df.dropna(subset=['job'])

    # marital
    # Single or married and once again remove unknown ones
    single = ["divorced", "single"]
    combined_df["marital"].replace(single, "single", inplace=True)
    combined_df["marital"].replace("unknown", np.nan, inplace=True)
    combined_df = combined_df.dropna(subset=['marital'])

    # Education
    # 'basic.4y','basic.6y','basic.9y' all these to same category basic.
    # Remove unknown once's
    basic = ['basic.4y', 'basic.6y', 'basic.9y']
    combined_df["education"].replace(basic, "basic", inplace=True)
    combined_df["education"].replace("unknown", np.nan, inplace=True)
    combined_df = combined_df.dropna(subset=['education'])

    # Poutcome
    # Just remove nan values and nonexistent
    combined_df["poutcome"].replace("nonexistent", np.nan, inplace=True)
    combined_df = combined_df.dropna(subset=['poutcome'])

    # Age
    # Instead of exact age. We should but them into age groups
    # Teen:18-25, Young_adult:26-35, adult:36-50, senior:51-65,	retired:66+
    # BUT. this does affect the accuracy of the model.
    # And also means that when doing single prediction, the value has to be categorized
    # Define conditions for each age group
    conditions = [
        (combined_df['age'].between(18, 25)),
        (combined_df['age'].between(26, 35)),
        (combined_df['age'].between(36, 50)),
        (combined_df['age'].between(51, 65)),
        (combined_df['age'] >= 66)
    ]

    # Define corresponding labels for each condition
    labels = ['teen', 'young_adult', 'adult', 'senior', 'retired']

    # Apply conditions and assign labels
    combined_df['age'] = np.select(conditions, labels, default='Unknown')

    # Pdays
    # Found that some pdays values go over 800 so decided to do few more groups than originally (4 groups)
    # Groups. I mean you can see the groups below.
    # BUT. this does affect the accuracy of the model.
    # Define conditions for each pdays group
    conditions = [
        (combined_df['pdays'] == -1),
        (combined_df['pdays'].between(0, 90)),
        (combined_df['pdays'].between(91, 180)),
        (combined_df['pdays'].between(181, 270)),
        (combined_df['pdays'].between(271, 365)),
        (combined_df['pdays'].between(366, 730)),
        (combined_df['pdays'] >= 731)
    ]

    # Define corresponding labels for each condition
    labels = [
        'no_contact',
        'within_3_months',
        'within_3_to_6_months',
        'within_6_to_9_months',
        'within_9_to_12_months',
        'within_second_year',
        'within_third_year_and_over'
    ]

    # Apply conditions and assign labels
    combined_df['pdays'] = np.select(conditions, labels, default='Unknown')

    # Balance average yearly balance
    # Adding groups
    # persons making <=25000 count is 7800 ish so almost whole dataset
    # So making groups whit 5k difference up to 30k
    conditions = [
        (combined_df['balance'] < 0),
        (combined_df['balance'].between(0, 5000)),
        (combined_df['balance'].between(5001, 10000)),
        (combined_df['balance'].between(10001, 15000)),
        (combined_df['balance'].between(15001, 20000)),
        (combined_df['balance'].between(20001, 25000)),
        (combined_df['balance'].between(25001, 30000)),
        (combined_df['balance'] >= 30001)
    ]

    # Define corresponding labels for each condition
    labels = [
        'negative_balance',
        '0-5k_balance',
        '5k-10k_balance',
        '10k-15k_balance',
        '15k-20k_balance',
        '20k-25k_balance',
        '25k-30k_balance',
        'over-30k_balance',
    ]

    # Apply conditions and assign labels
    combined_df['balance'] = np.select(conditions, labels, default='Unknown')

    # campaign
    # grouping whit difference of 5 up to 15
    conditions = [
        (combined_df['campaign'] == 0),
        (combined_df['campaign'].between(1, 5)),
        (combined_df['campaign'].between(6, 10)),
        (combined_df['campaign'].between(11, 15)),
        (combined_df['campaign'] >= 16)
    ]

    # Define corresponding labels for each condition
    labels = [
        '0_contacts',
        '1-5_contacts',
        '6-10_contacts',
        '11-15_contacts',
        '16-over_contacts',
    ]

    # Apply conditions and assign labels
    combined_df['campaign'] = np.select(conditions, labels, default='Unknown')

    # previous number of contacts performed before this campaign and for this client
    # same range as campaign
    conditions = [
        (combined_df['previous'] == 0),
        (combined_df['previous'].between(1, 5)),
        (combined_df['previous'].between(6, 10)),
        (combined_df['previous'].between(11, 15)),
        (combined_df['previous'] >= 16)
    ]

    # Define corresponding labels for each condition
    labels = [
        '0_previous',
        '1-5_previous',
        '6-10_previous',
        '11-15_previous',
        '16-over_previous',
    ]

    # Apply conditions and assign labels
    combined_df['previous'] = np.select(conditions, labels, default='Unknown')

    # Filtering proces result
    # from 45211 x 16
    # to [7907 rows x 50 columns]

    to_CSV = combined_df
    to_CSV.to_csv("training_data/whole_dataset.csv", index=False)
