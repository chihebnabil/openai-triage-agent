# Medical Triage System with OpenAI Agent SDK

A demonstration of building an intelligent medical triage system using the OpenAI Agent SDK. This project showcases how to create a multi-agent system that handles medical inquiries, appointments, and emergencies.

## 🏥 Features

- Automated medical triage with multiple specialized agents
- Real-time symptom analysis and emergency detection
- Appointment scheduling coordination
- Prescription management
- HIPAA-compliant interaction patterns

## 🚀 Quick Start

1. Clone the repository
2. Install dependencies:
```bash
pip install agents-sdk python-dotenv colorama pydantic
```

3. Set up your OpenAI API key in `.env`:
```env
OPENAI_API_KEY=your_api_key_here
```

4. Run the demo:
```bash
python demo.py
```

## 🔧 System Architecture

### Agents
- **Primary Triage Agent**: First point of contact, routes patients to specialized agents
- **Symptom Analyzer**: Analyzes medical symptoms and identifies potential conditions
- **Appointment Coordinator**: Manages scheduling and availability
- **Pharmacy Manager**: Handles prescription-related queries
- **Emergency Handler**: Manages urgent medical situations

### Data Models
- `TriageResult`: Tracks urgency levels and recommended actions
- `Diagnosis`: Records possible conditions and confidence levels
- `Prescription`: Manages medication details and instructions

## 💻 Code Examples

### Creating a Specialized Agent
```python
symptom_agent = Agent(
    name="symptom_analyzer",
    instructions="Analyze patient symptoms using medical knowledge base...",
    tools=[check_medical_knowbase],
    output_type=Diagnosis
)
```

### Defining Tool Functions
```python
@function_tool
def check_medical_knowbase(symptoms: str) -> dict:
    """Query medical database for potential conditions"""
    return {
        "possible_conditions": ["Viral upper respiratory infection", "Allergic rhinitis"],
        "red_flags": ["fever >39°C", "difficulty breathing"]
    }
```

## 📝 Example Usage

The system can handle various medical queries:
```python
cases = [
    "I'm experiencing chest pain and shortness of breath",
    "I need a refill for my Fexofenadine prescription",
    "My doctor recommended a follow-up cardiology appointment",
    "I've had a persistent cough for 3 days with mild fever"
]
```

## 🔒 Security & Compliance

- HIPAA compliance built into agent instructions
- Secure handling of medical information
- Clear handoff protocols between agents

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This is a demonstration project and should not be used for actual medical diagnosis or treatment. Always consult with healthcare professionals for medical advice.
