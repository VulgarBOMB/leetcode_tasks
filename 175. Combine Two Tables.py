import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, how='left', on='personId')[['firstName', 'lastName', 'city', 'state']]


person = pd.DataFrame([[1, 'Wang', 'Allen'],
                       [2, 'Alice', 'Bob']],
                      columns=['personId',
                               'lastName',
                               'firstName'])
address = pd.DataFrame([[1, 2, 'New York City', 'New York'],
                        [2, 3, 'Leetcode', 'California']],
                       columns=['addressId',
                                'personId',
                                'city',
                                'state'])

print(combine_two_tables(person, address))
