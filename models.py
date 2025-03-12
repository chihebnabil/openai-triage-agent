from pydantic import BaseModel
from typing import List

class TriageResult(BaseModel):
    urgency_level: str
    recommended_action: str
    follow_up_time: str

class Diagnosis(BaseModel):
    possible_conditions: List[str]
    confidence_level: float
    recommended_tests: List[str]

class Prescription(BaseModel):
    medication: str
    dosage: str
    instructions: str
    warnings: str
