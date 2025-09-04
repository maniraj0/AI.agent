# scoring.py
from typing import List, Dict
import json, math

RUBRIC = {
  "dimensions": {
    "communication": {"weight": 0.20, "anchors": ["unclear", "basic", "good", "strong", "exceptional"]},
    "problem_solving": {"weight": 0.25, "anchors": ["-", "-", "identifies root cause", "structured hypotheses", "data-driven & iterative"]},
    "role_knowledge": {"weight": 0.30, "anchors": ["-", "theory only", "applies patterns", "adapts patterns", "innovates"]},
    "values_alignment": {"weight": 0.15, "anchors": ["-", "inconsistent", "neutral", "positive", "exemplary"]},
    "integrity": {"weight": 0.10, "anchors": ["-", "concerns", "ok", "clear", "role model"]}
  }
}

def weighted_score(scores: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    total = 0.0
    details = {}
    for dim, s in scores.items():
        w = RUBRIC["dimensions"][dim]["weight"]
        val = s["score"] * w
        total += val
        details[dim] = {"score": s["score"], "confidence": s.get("confidence", 0.7), "weight": w}
    return {"overall": round(total, 2), "details": details}
