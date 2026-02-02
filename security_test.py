import os
import random
import hashlib

def process_user_data(user_input):
    # --- HIGH SEVERITY: Command Injection ---
    # Using user input directly in a system command.
    # A user could enter: "; rm -rf /" to cause damage.
    os.system("echo Processing data for: " + user_input)

    # --- MEDIUM SEVERITY: Hardcoded Secret ---
    # Storing sensitive credentials in plain text.
    # Anyone with access to the code can steal this key.
    API_SECRET_KEY = "1a2b3c4d5e6f7g8h9i0j"

    # --- LOW SEVERITY: Insecure Randomness ---
    # 'random' is not cryptographically secure. 
    # It shouldn't be used for security tokens or passwords.
    session_id = random.random()

    # --- LOW SEVERITY: Weak Hash Algorithm ---
    # MD5 is outdated and easily cracked by modern computers.
    weak_hash = hashlib.md5(b"password123").hexdigest()

    return f"Done with session {session_id}"

# Example usage
process_user_data("Assignment_User")
