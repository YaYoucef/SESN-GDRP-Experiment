"""Simulate workloads from 100 to 10,000 requests."""

import csv
import random
from mongodb_client import users_col
from gdpr_operations import *

users = list(users_col.find())
levels = [100, 1000, 5000, 10000]

with open('results/latency_logs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['operation', 'requests', 'latency'])

    for r in levels:
        for _ in range(r):
            u = random.choice(users)
            writer.writerow(['RTBF', r, right_to_be_forgotten(u['user_id'])])
            lat, _ = data_access_request(u['user_id'])
            writer.writerow(['DAR', r, lat])
            writer.writerow(['CONSENT', r, consent_management(u['user_id'], u['consent'])])