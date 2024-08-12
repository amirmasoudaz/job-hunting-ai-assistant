resume_template = {}
resume_customization = ""

email_template = {
    "sender": {
        "name": "<APPLICANT_NAME>",
        "email": "<APPLICANT_EMAIL>"
    },
    "recipient": {
        "name": "<RECIPIENT_NAME>",
        "email": "<RECIPIENT_EMAIL>"
    },
    "subject": "<EMAIL_SUBJECT>",
    "content": {
        "opening": "",
        "body": [],
        "closing": "",
        "signature": "<APPLICANT_NAME>"
    }
}


email_customization = """
Your task is to draft a professional email to the employer expressing the user's interest in the job position and explaining why the user is the best fit for the job.
The email should be customized to the job description and the user's qualifications.
Generate a tailored email that aligns with the job description and the user's qualifications.

You should analyze the user's ULTIMATE CV to understand the user's qualifications, skills, and experiences.
Compare the user's qualifications with the required and preferred qualities of the job description.
"""

letter_template = {
    "applicant": {
        "name": "<APPLICANT_NAME>",
        "address": "<APPLICANT_ADDRESS>",
        "phone": "<APPLICANT_PHONE>",
        "email": "<APPLICANT_EMAIL>"
    },
    "date": "<DATE>",
    "recipient": {
        "company": "<COMPANY_NAME>",
        "address": "<COMPANY_ADDRESS>",
        "department": "<DEPARTMENT_NAME>",
    },
    "content": {
        "opening": "",
        "body": [],
        "closing": "",
        "signature": "<APPLICANT_NAME>"
    },
}


letter_customization = """
Your task is to customize the user's letter by analyzing the job description and the user's qualifications and background.
The user's letter should be customized to fit the job description and the user's qualifications.
Generate a tailored letter that aligns with the job description and the user's qualifications.

You should analyze the user's ULTIMATE CV to understand the user's qualifications, skills, and experiences.
Compare the user's qualifications with the required and preferred qualities of the job description.
"""
