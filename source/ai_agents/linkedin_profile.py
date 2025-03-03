import requests
from agent_base import agent, linkedin
from source.ResponseSchemas.linkedin_profile_schema import LinkedInAnalysis
import json

questions = [
	"How many years of industry-specific experience does the founder have?",
	"Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
	"How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
	"Are there employment gaps or frequent job changes (>3 roles in 5 years)?"
]

def fetch_founder_profile(founder_link):
    linkedin_data = linkedin.get_founder_info(founder_link)
    prompt = f"""Analyze this LinkedIn data for founder qualifications:
       {linkedin_data} and answer the questions {questions}
       
       
       Return the following schema:
       class LinkedInAnalysis(BaseModel):
            years_of_industry_experience: conint(ge=0)
            reputable_companies: str
            leadership_roles: conint(ge=0)
            job_changes: conint(ge=0)
            additional_context: Optional[str]
"""

    response = agent.run(prompt)
    json_data = json.dumps(response)
    return json_data

if __name__ == '__main__':
    fetch_founder_profile(founder_link="https://www.linkedin.com/in/sunnymay/")

# res = agent.run(f"Based on {founder_data}, answer the questions: {questions}.")