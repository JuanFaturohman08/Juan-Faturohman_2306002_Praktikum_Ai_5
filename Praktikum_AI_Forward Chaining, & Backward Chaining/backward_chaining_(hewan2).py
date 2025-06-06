# -*- coding: utf-8 -*-
"""backward_chaining (hewan2)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q_sy7MNxME0qgZprMdGj-N8IPP7PxWGV
"""

def backward_chaining(goal, facts, rules):
  if goal in facts:
    return True
  for rule in rules:
    if rule["then"] == goal:
      if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
        return True
  return False

facts = {"has_feathers", "has_small_wings"}
rules = [
    {"if": {"is_bird", "cannot_fly"}, "then": "is_penguin"},
    {"if": {"has_feathers"}, "then": "is_bird"},
    {"if": {"has_small_wings"}, "then": "cannot_fly"}
]

goal = "is_penguin"
result = backward_chaining(goal, facts, rules)
print(f"Is {goal} provable? -> {result}")