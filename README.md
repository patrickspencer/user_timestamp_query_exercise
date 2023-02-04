# TSV Parse exercise

Given an input file with columns user, timestamp, and query text Organize input
as list of sessions for each user. A session is a list of queries. A query is a
tuple of (timestamp, text). If the difference between the timestamp of the
current query and the previous query is greater than 3 minutes, then the current
query is a new session.

Return dict in the form:
```
defaultdict(list,
        {'u1': [[(123, 'q_u1_a'), (124, 'q_u1_b')], [(400, 'q_u1_c')]],
            'u2': [[(1000, 'q_u2_a'), (1001, 'q_u2_b')]],
            'u3': [[(2000, 'q_u3_a')], [(3000, 'q_u3_b')]]})
```