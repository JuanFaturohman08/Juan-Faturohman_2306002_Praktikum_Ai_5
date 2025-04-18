# -*- coding: utf-8 -*-
"""forward_chaining (Kendaraan)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yG63iCjOqrJmII9N1M4NlOul0VWoja-f
"""

def forward_chaining(facts, rules):
  inferred = set(facts)
  changed = True
  while changed:
    changed = False
    for rule in rules:
      if rule["if"].issubset(inferred) and rule["then"] not in inferred:
        inferred.add(rule["then"])
        changed = True
    return inferred

facts = {"has_wheels", "has_engine", "has_four_wheels"}
rules = [
    {"if": {"has_wheels", "has_engine"}, "then": "is_vehicle"},
    {"if": {"is_vehicle", "has_two_wheels"}, "then": "is_motorcycle"},
    {"if": {"is_vehicle", "has_four_wheels"}, "then": "is_car"},

]

result = forward_chaining(facts, rules)
print("Inferred facts:", result)