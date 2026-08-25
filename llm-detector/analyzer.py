# This file decides the final verdict after checking the score
# Take a risk score and decide the final verdict of flag, allow or block
def analyze_score(score: int) -> str:
# If the risk score is 70 or above then block
  if score >= 70:
    return "BLOCK"
# If the risk score is from 70 to 69 then flag it
  if score >= 30:
    return "FLAG"
# If the score is below 30 then allow it
  if score <= 30:
    return "ALLOW"