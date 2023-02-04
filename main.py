#!/usr/bin/env python3
# Description: Parse user query data into sessions
from collections import defaultdict
import pandas as pd


def read_file(file_name):
    """
    columns: user, timestamp, text
    """
    try:
        df = pd.read_csv(file_name, sep='\t')
        return [(r[0], r[1], r[2]) for _, r in df.iterrows()]
    except FileNotFoundError:
        print(f"File {file_name} not found.")


def parse(inputs):
    """Organize input as list of sessions
    for each user. A session is a list of queries.
    A query is a tuple of (timestamp, text).
    If the difference between the timestamp of
    the current query and the previous query is 
    greater than 3 minutes, then the current query
    is a new session.

    Return dict in the form:
    defaultdict(list,
            {'u1': [[(123, 'q_u1_a'), (124, 'q_u1_b')], [(400, 'q_u1_c')]],
             'u2': [[(1000, 'q_u2_a'), (1001, 'q_u2_b')]],
             'u3': [[(2000, 'q_u3_a')], [(3000, 'q_u3_b')]]})
    """
    # dict: user -> list of sessions
    sessions = defaultdict(list)

    for i in inputs:
        u, ts, t = i  # user, timestamp, text
        q = (ts, t)  # query
        s = sessions[u]  # session list

        if s and ts - s[-1][-1][0] <= 3*60:
            s[-1].append(q)
        else:
            # s[-1][-1][0] always exists
            s.append([q])

    return sessions


# test read_file function
FILE_NAME = 'user_timestamp_query_data.tsv'
inputs = read_file(FILE_NAME)
print(inputs)

# test parse function
inputs = [
    ('u1', 123, 'q_u1_a'),
    ('u2', 1000, 'q_u2_a'),
    ('u2', 1001, 'q_u2_b'),
    ('u1', 124, 'q_u1_b'),
    ('u1', 400, 'q_u1_c'),
    ('u3', 2000, 'q_u3_a'),
    ('u3', 3000, 'q_u3_b')
]
p = parse(inputs)
print(p)

# putting it together
FILE_NAME = 'user_timestamp_query_data.tsv'
inputs = read_file(FILE_NAME)
p = parse(inputs)
print(p)
