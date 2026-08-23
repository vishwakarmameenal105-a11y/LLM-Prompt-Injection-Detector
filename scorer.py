# this module calculates a risk score (0-100) from scanner matches
# Points for each attack type
POINTS = {"jailbreak": 35,
          "system prompt leakage": 35,
          "instruction override": 30} 
# Takes matches from scanner and returns total risk score
def calculate_score(matches: list)-> int:
# - Start with score 0
  score = 0
# - For each match add points based on attack type
  for match in matches:
    attack_type = match.get("type":"")
    score += POINTS.get(attack_type, 0)
# - If score goes above 100, cap it at 100
  if score > 100:
    score = 100
# - Return the final score
  return score