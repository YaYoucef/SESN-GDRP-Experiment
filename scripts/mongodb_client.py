"""MongoDB interface for mutable user data."""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.sesn
users_col = db.users


def insert_user(user: dict):
    users_col.insert_one(user)


def get_user(user_id: str):
    return users_col.find_one(
        {"user_id": user_id},
        {"_id": 0, "private_key": 0}
    )



def update_user_consent(user_id: str, consent: dict):
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"consent": consent}}
    )



def delete_user(user_id: str):
    users_col.delete_one({"user_id": user_id})

def store_user_asset(user_id: str, consent: dict):
    tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=bdb_keypair.public_key,
        asset={'data': {'user_id': user_id}},
        metadata={'consent': consent}
    )
    signed = bdb.transactions.fulfill(tx, private_keys=bdb_keypair.private_key)
    return bdb.transactions.send_commit(signed)
