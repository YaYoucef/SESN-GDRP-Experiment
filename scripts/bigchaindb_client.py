"""BigchainDB client for immutable consent metadata."""

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB('http://localhost:9984')
bdb_keypair = generate_keypair()


def store_user_asset(user_id: str, consent: dict):
    tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=bdb_keypair.public_key,
        asset={'data': {'user_id': user_id}},
        metadata={'consent': consent}
    )
    signed = bdb.transactions.fulfill(tx, private_keys=bdb_keypair.private_key)
    return bdb.transactions.send_commit(signed)