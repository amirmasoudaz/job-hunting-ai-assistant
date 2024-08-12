import json

template = {
    "Position Name": "",
    "Company Name": "",
    "Location": "",
    "Employment Type": "",
    "Industry": "",
    "Field of Work": "",
    "Required Qualities": "",
    "Preferred Qualities": "",
    "Technical Skills": "",
    "Soft Skills": "",
    "Skills Valued": "",
    "Character Values": "",
    "Expectations": "",
    "Tasks Assigned": "",
    "Work Environment": "",
    "About Company": "",
    "Salary and Benefits": "",
    "Application Deadline": "",
    "Additional Information": ""
}


description_normalization = f"""You will be provided with a RAW DATA which contains information about an open job position.
Your task is to organize and structure the RAW DATA into a JSON format by populating the provided TEMPLATE with the corresponding information to each key.

The following criteria should be considered when organizing the RAW DATA for each key in the TEMPLATE:
    - Position Name: The name of the position.
    - Company Name: The name of the company.
    - Location: The location of the job -> [City, Country/Remote/Hybrid]
    - Employment Type: The type of employment -> [Full-time, Part-time, Contract, Internship]
    - Industry: The industry the company is in -> [Technology, Finance, Healthcare, etc.]
    - Field of Work: The field of work the job is in -> [Data Science, Software Engineering, Marketing, etc.]
    - Required Qualities: The minimum qualities they need for the position.
    - Preferred Qualities: The ideal qualities they want for the position.
    - Technical Skills: The list of technical skills they require for the position.
    - Soft Skills: The list of soft skills they require for the position.
    - Skills Valued: The technical skills they value for the person they want to hire.
    - Character Values: The character they value for the person they want to hire.
    - Expectations: What they expect from the person they want to hire.
    - Tasks Assigned: What sorts of tasks do they want to get done, and what this role will include.
    - Work Environment: About the work environment and the perks they provide when hiring.
    - About Company: The mission and idea of the company and their goals and services.
    - Salary and Benefits: The role's salary and the benefits the role includes.
    - Application Deadline: The deadline for applying to the job.
    - Additional Information: Any additional information about the job.

TEMPLATE: ###{json.dumps(template, indent=4)}###"""
