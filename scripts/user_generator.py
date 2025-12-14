"""Generate 10,000 synthetic users with GDPR consent flags."""

import uuid
import random
import json
from crypto_utils import generate_keypair
from mongodb_client import insert_user

users = []

for _ in range(10000):
    user_id = str(uuid.uuid4())
    priv, pub = generate_keypair(user_id)

    user = {
        'user_id': user_id,
        'name': f'User{random.randint(1000,9999)}',
        'email': f'user{random.randint(1,100000)}@sesn.org',
        'public_key': pub,
        'private_key': priv,
        'consent': {
            'data_processing': True,
            'profiling': random.choice([True, False]),
            'sharing': random.choice([True, False])
        }
    }

    insert_user(user)
    users.append(user)

with open('data/users.json', 'w') as f:
    json.dump(users, f, indent=2)