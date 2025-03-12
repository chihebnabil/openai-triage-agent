from agents import Runner, RunConfig, set_default_openai_key
from dotenv import load_dotenv
from myagents import triage_agent
from colorama import init, Fore, Style
import os

init()  # Initialize colorama for Windows

# Color constants for different message types
PATIENT_COLOR = Fore.CYAN
RESULT_COLOR = Fore.GREEN
SEPARATOR_COLOR = Fore.YELLOW
RESET = Style.RESET_ALL

load_dotenv()
set_default_openai_key(os.getenv('OPENAI_API_KEY'))

async def run_healthcare_demo():
    cases = [
        "I'm experiencing chest pain and shortness of breath",
        "I need a refill for my Fexofenadine prescription",
        "My doctor recommended a follow-up cardiology appointment",
        "I've had a persistent cough for 3 days with mild fever"
    ]
    
    for case in cases:
        print(f"\n{SEPARATOR_COLOR}{'='*50}{RESET}")
        print(f"{PATIENT_COLOR}Patient Query: {Style.BRIGHT}{case}{RESET}")
        print(f"{SEPARATOR_COLOR}{'-'*50}{RESET}")
        
        config = RunConfig(model="gpt-4o")
        messages = [{"role": "user", "content": case}]
        output = await Runner.run(triage_agent, messages, run_config=config)
        
        print(f"{RESULT_COLOR}Triage Result:{Style.BRIGHT}")
        print(f"{output.final_output}{RESET}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_healthcare_demo())