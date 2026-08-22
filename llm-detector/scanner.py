# This file scans a user prompt for attack patterns
# imports - pull in the pattern list from patterns.py
from patterns import JAILBREAK_PATTERNS, LEAKAGE_PATTERN, OVERRRIDE_PATTERNS
# function to take the user prompt and check it against the attack patterns list and return matches
def scan_prompt(prompt: str) -> list:
# create an empty list to store all matches
# inside the function:
# - convert prompt to lowercase so that match is case insensitive
    prompt_lower = prompt.lower()
# - check each pattern list one by one
# check jailbreak pattern
for pattern in JAILBREAK_PATTERNS:
    if pattern in prompt_lower:
        matches.append({"type":"jailbreak","pattern":pattern})
# check system prompt leakage pattern
for pattern in LEAKAGE_PATTERN:
    if pattern in prompt_lower:
        matches.append({"type":"system prompt leakage","pattern":pattern})
# check instruction override pattern
for pattern in OVERRRIDE_PATTERNS:
    if pattern in prompt.lower:
        matches.append({"type":"Instructionn Override","pattern":pattern})
# - Return all matches as a list
return matches