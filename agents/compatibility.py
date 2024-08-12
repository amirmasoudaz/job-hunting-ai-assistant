application_compatibility = """You will be provided with a CV and a JOB DESCRIPTION.
Your task is to analyze the CV based on the provided JOB DESCRIPTION and answer the following questions.
You should populate the provided answer template JSON with your responses.

Each question's answer should be a list with two elements:
- The first element should be Yes or No, indicating whether the answer to the question is Yes or No.
- The second element should be a brief and concise explanation of why you answered Yes or No to the question.

When answering a question, try to be as realistic and objective as possible based on the information provided in the CV and the job description. We are looking for honest and insightful feedback.
Each question has a number associated with it, and you should provide an answer to a question as the value of the corresponding key in the answer template JSON.

ATTENTION: For the Yes or No answers, do not use any other form of the answer, such as "Yes, but" or "No, because", "Not specified", etc. Solely say "Yes" or "No". Anything else is not acceptable.

CV: ```{user_resume}```


QUESTIONS: %%%{questions}%%%


TEMPLATE: ###{template}###"""

application_compatibility_eco = """You will be provided with a CV and a JOB DESCRIPTION.
Your task is to analyze the CV based on the provided JOB DESCRIPTION and answer the following questions with "Yes" or "No".
You should populate the provided answer template JSON with your responses.

Each question's answer should be either "Yes" or "No". You are not allowed to answer a question with anything other than "Yes" or "No". 

When answering a question, try to be as realistic and objective as possible based on the information provided in the CV and the job description. We are looking for honest and insightful feedback.
Each question has a number associated with it, and you should provide an answer to a question as the value of the corresponding key in the answer template JSON.

ATTENTION: Do not use any other form of the answer, such as "Yes, but" or "No, because", "Not specified", etc. Solely say "Yes" or "No". Anything else is not acceptable.

CV: ```{user_resume}```


QUESTIONS: %%%{questions}%%%


TEMPLATE: ###{template}###"""

description_compatibility = """You will be provided with a CV and a JOB DESCRIPTION.
Your task is to analyze the JOB DESCRIPTION based on the provided CV and answer the following questions.
You should populate the provided answer template JSON with your responses.

Each question's answer should be a list with two elements:
- The first element should be Yes or No, indicating whether the answer to the question is Yes or No.
- The second element should be a brief and concise explanation of why you answered Yes or No to the question.

When answering a question, try to be as realistic and objective as possible based on the information provided in the CV and the job description. We are looking for honest and insightful feedback.
Each question has a number associated with it, and you should provide an answer to a question as the value of the corresponding key in the answer template JSON.

ATTENTION: For the Yes or No answers, do not use any other form of the answer, such as "Yes, but" or "No, because", "Not specified", etc. Solely say "Yes" or "No". Anything else is not acceptable.


CV: ```{user_resume}```

DESIRED JOB TITLES: +++{desired_job_titles}+++

DESIRED INVOLVED SKILLS: +++{desired_involved_skills}+++

QUESTIONS: %%%{questions}%%%

TEMPLATE: ###{template}###"""


description_compatibility_eco = """You will be provided with a CV and a JOB DESCRIPTION.
Your task is to analyze the JOB DESCRIPTION based on the provided CV and answer the following questions with "Yes" or "No".
You should populate the provided answer template JSON with your responses.

Each question's answer should be either "Yes" or "No". You are not allowed to answer a question with anything other than "Yes" or "No".

When answering a question, try to be as realistic and objective as possible based on the information provided in the CV and the job description. We are looking for honest and insightful feedback.
Each question has a number associated with it, and you should provide an answer to a question as the value of the corresponding key in the answer template JSON.

ATTENTION: Do not use any other form of the answer, such as "Yes, but" or "No, because", "Not specified", etc. Solely say "Yes" or "No". Anything else is not acceptable.


CV: ```{user_resume}```

DESIRED JOB TITLES: +++{desired_job_titles}+++

DESIRED INVOLVED SKILLS: +++{desired_involved_skills}+++

QUESTIONS: %%%{questions}%%%

TEMPLATE: ###{template}###"""


description_preprocessing = """You will be provided with descriptions of a JOB, which will be delimited with triple backticks (```).
You are tasked with classifying whether the JOB belongs to group Y or N based on its alignment with the provided desired roles, skills, and tech stack by following the steps below:
1. Start by comparing the JOB with the provided ROLES. If the JOB aligns with the ROLES, move on to the next step, otherwise, classify the JOB as N.
2. Check if the SKILLS provided are useful for that JOB. If the SKILLS align with the JOB, move on to the next step, otherwise, classify the JOB as N.
3. Examine if the TECH STACK provided is relevant to the JOB. If the TECH STACK aligns with the JOB, classify the JOB as Y, otherwise, classify the JOB as N.

For review, classify the JOB as:
Y - If the JOB aligns with the ROLES, SKILLS, and TECH STACK.
N - Otherwise.

ROLES: 
###
{role_preferences}
###

SKILLS: 
***
{skills_preferences}
***

TECH STACK: 
+++
{stack_preferences}
+++

Output a single character, either Y or N, representing the classification of the JOB."""
