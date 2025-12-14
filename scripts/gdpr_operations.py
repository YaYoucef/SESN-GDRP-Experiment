"""
GDPR Operations Module for SESN Experimental Framework
-----------------------------------------------------
This module implements GDPR-compliant operations required in a
Spontaneous and Ephemeral Social Network (SESN):

1. Right to be Forgotten (Art. 17 GDPR)
2. Data Access Request (Art. 15 GDPR)
3. Consent Management (Art. 7 & Art. 21 GDPR)

Each operation:
- Interacts with MongoDB (mutable encrypted user data)
- Interacts with BigchainDB (immutable consent metadata)
- Measures execution latency for performance evaluation

The design explicitly avoids modifying blockchain history and instead
relies on cryptographic key destruction (crypto-shredding) to ensure
GDPR compliance.
"""

import time
from typing import Tuple, Dict, Any

from crypto_utils import crypto_shred
from mongodb_client import (
    get_user,
    update_user_consent,
    delete_user
)
from bigchaindb_client import store_user_asset


# -------------------------------------------------------------------
# Right to be Forgotten (Art. 17 GDPR)
# -------------------------------------------------------------------

def right_to_be_forgotten(user_id: str) -> float:
    """
    Enforces the Right to be Forgotten using crypto-shredding.

    GDPR rationale:
    ----------------
    Instead of deleting immutable blockchain data, this operation:
    1. Permanently destroys the user's cryptographic keys
    2. Deletes the encrypted personal data from MongoDB

    Once keys are destroyed, any remaining encrypted data
    becomes computationally irrecoverable.

    Parameters
    ----------
    user_id : str
        Unique identifier of the user

    Returns
    -------
    float
        Latency (in seconds) of the operation
    """

    start_time = time.perf_counter()

    # Step 1: Destroy cryptographic keys (crypto-shredding)
    crypto_shred(user_id)

    # Step 2: Remove mutable encrypted data from MongoDB
    delete_user(user_id)

    latency = time.perf_counter() - start_time
    return latency


# -------------------------------------------------------------------
# Data Access Request (Art. 15 GDPR)
# -------------------------------------------------------------------

def data_access_request(user_id: str) -> Tuple[float, Dict[str, Any]]:
    """
    Handles a GDPR Data Access Request.

    GDPR rationale:
    ----------------
    The user has the right to access their personal data.
    This operation retrieves encrypted data from MongoDB.
    (Decryption is assumed to occur client-side using the user's keys.)

    Parameters
    ----------
    user_id : str
        Unique identifier of the user

    Returns
    -------
    Tuple[float, dict]
        - Latency (in seconds)
        - Retrieved user document (encrypted)
    """

    start_time = time.perf_counter()

    # Retrieve encrypted user data
    user_data = get_user(user_id)

    latency = time.perf_counter() - start_time
    return latency, user_data


# -------------------------------------------------------------------
# Consent Management (Art. 7 & Art. 21 GDPR)
# -------------------------------------------------------------------

def consent_management(user_id: str, consent: Dict[str, bool]) -> float:
    """
    Adds, updates, or revokes user consent.

    GDPR rationale:
    ----------------
    - Consent must be explicit, revocable, and auditable
    - MongoDB stores the current (mutable) consent state
    - BigchainDB stores an immutable consent event log

    This dual-storage approach ensures:
    - Fast operational access
    - Tamper-proof auditability

    Parameters
    ----------
    user_id : str
        Unique identifier of the user
    consent : dict
        Dictionary of consent flags (e.g., processing, profiling, sharing)

    Returns
    -------
    float
        Latency (in seconds) of the consent operation
    """

    start_time = time.perf_counter()

    # Step 1: Update mutable consent state in MongoDB
    update_user_consent(user_id, consent)

    # Step 2: Record immutable consent transaction in BigchainDB
    store_user_asset(user_id, consent)

    latency = time.perf_counter() - start_time
    return latency

"""Implements GDPR-compliant operations with latency measurement."""

import time
from crypto_utils import crypto_shred
from mongodb_client import get_user, update_user_consent, delete_user
from bigchaindb_client import store_user_asset


def right_to_be_forgotten(user_id: str) -> float:
    start = time.perf_counter()
    crypto_shred(user_id)
    delete_user(user_id)
    return time.perf_counter() - start


def data_access_request(user_id: str):
    start = time.perf_counter()
    user = get_user(user_id)
    return time.perf_counter() - start, user


def consent_management(user_id: str, consent: dict) -> float:
    start = time.perf_counter()
    update_user_consent(user_id, consent)
    store_user_asset(user_id, consent)
    return time.perf_counter() - start