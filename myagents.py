from agents import Agent, handoff
from models import Diagnosis, TriageResult, Prescription
from tools import (
    check_medical_knowbase, check_appointment_availability,
    check_medication_stock, alert_emergency_team
)

# Specialized medical agents
symptom_agent = Agent(
    name="symptom_analyzer",
    instructions="Analyze patient symptoms using medical knowledge base. Identify red flags and potential conditions.",
    tools=[check_medical_knowbase],
    output_type=Diagnosis
)

appointment_agent = Agent(
    name="appointment_coordinator",
    instructions="Handle appointment scheduling and availability checks. Consider urgency and specialty needs.",
    tools=[check_appointment_availability],
    output_type=TriageResult
)

pharmacy_agent = Agent(
    name="medication_manager",
    instructions="Manage prescription requests and medication availability. Check interactions and alternatives.",
    tools=[check_medication_stock],
    output_type=Prescription
)

emergency_agent = Agent(
    name="emergency_handler",
    instructions="Handle urgent medical situations. Activate emergency protocols when life-threatening symptoms present.",
    tools=[alert_emergency_team],
    output_type=TriageResult
)

# Main triage agent
triage_agent = Agent(
    name="primary_triage",
    instructions="""You are the first point of contact for patients. Assess their condition and:
    1. For non-urgent symptoms: Handoff to symptom analyzer
    2. For prescription questions: Route to pharmacy
    3. For follow-up requests: Connect to appointment coordinator
    4. For emergency symptoms: Immediately escalate to emergency handler
    Always maintain HIPAA compliance and show empathy.""",
    handoffs=[
        handoff(symptom_agent),
        handoff(appointment_agent),
        handoff(pharmacy_agent),
        handoff(emergency_agent)
    ]
)
