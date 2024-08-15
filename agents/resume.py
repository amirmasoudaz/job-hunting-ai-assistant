import json


resume_conv_raw_to_md = """
The following is the curriculum vitae of a user. The curriculum vitae will be delimited with triple &&& characters.
Your task is to convert the CV sections into a markdown format completely without losing any information.

Your output should be a JSON containing the following keys:
- "info": "MarkDown conversion of the user's personal information such as name, location, contact information, social media, website, professional title, and professional summary."
- "work": "MarkDown conversion of the user's work experience."
- "project": "MarkDown conversion of the user's project experience."
- "education": "MarkDown conversion of the user's education."
- "skills": "MarkDown conversion of the user's skills, including technical skills, soft skills, and language skills."
- "certifications": "MarkDown conversion of the user's certifications."
- "others": "MarkDown conversion of any other information that does not fit into the above categories."

Extract the information from the CV exactly as they are appearing in the CV without altering the literature and the contents. 
Do not convert paragraphs into bullet points or vice versa.

NOTE: The output JSON should contain the keys mentioned above and the values should be the markdown conversion of the respective sections of the CV. 
For your reference, the keys are ["info", "work", "project", "education", "skills", "certifications", "others"].
"""

resume_conv_md_to_json = """
You will be provided by the user with the contents of the {section} section of their CV, which will be delimited by triple &&& characters.
You are provided with a JSON template that you need to populate with the information from the {section} section of the user's CV. The JSON template is delimited by triple hash symbols (###).

Populate the JSON template provided with the information from the {section} section of the CV completely without losing any information exactly as they are appearing in the markdown format.
Ensure that your response is lossless and the data is accurately transferred from the markdown format to the JSON format without altering the literature and the contents. Do not convert paragraphs into bullet points or vice versa.

###{template}###

NOTE: {template_info}"""

resume_section_info = {
    "info": "",
    "work": "As the value for the 'details' key, you should generate a dictionary, that each key of the dictionary should be a title of a task, project, or responsibility and the value of that key should be the descriptions of that task, project, or responsibility. \nAs the 'type' of work experience, choose the most appropriate type of employment (e.g. 'full-time', 'part-time', 'contract', 'remote', 'internship', 'volunteer', 'co-op', etc.) and if multiple types are provided, join them together using a comma.\n\nAs the value of the 'url' key, you should generate a dictionary where the 'title' key be the title of the hyperlink (e.g. 'Website', 'GitHub', etc.) and the 'link' key should be the URL of the hyperlink.",
    "project": "As the value of the 'url' key, you should generate a dictionary where the 'title' key be the title of the hyperlink (e.g. 'Website', 'GitHub', etc.) and the 'link' key should be the URL of the hyperlink.",
    "education": "",
    "skills": "Extract the skills from the markdown format and group them into a list of dictionaries where each dictionary should contain the 'title' key and the 'skills' key. The 'title' key should contain the title of the group and the 'skills' key should contain a list of strings where each string is a skill from the markdown format. If the input skills are not grouped, group them into suitable groups and provide the best title for the group. Ensure there is a good balance in distributing the skills into the groups.",
    "certifications": "As the value of the 'url' key, you should generate a dictionary where the 'title' key be the title of the hyperlink (e.g. 'Website', 'GitHub', 'Link', etc.) and the 'link' key should be the URL of the hyperlink.",
    "others": "As the value for the 'details' key, you should generate a list of string. Ensure that the value of 'details' is a list of strings where each string is a paragraph, sentence, or a phrase from the markdown format."
}

resume_section_templates = {
    "info": {
        "info": {
            "name": "",
            "city": "",
            "state/province": "",
            "country": "",
            "email": "",
            "phone": "",
            "social_media": [
                {
                    "platform": "",
                    "url": ""
                },
            ],
            "website": [],
            "title": "",
            "summary": "",
        }
    },
    "work": {
        "work": [
            {
                "company": "",
                "position": "",
                "type": "",
                "url": {
                    "title": "",
                    "link": "",
                },
                "duration": {
                    "from": "",
                    "till": ""
                },
                "details": {},
            },
        ],
    },
    "project": {
        "project": [
            {
                "name": "",
                "url": {
                    "title": "",
                    "link": "",
                },
                "duration": {
                    "from": "",
                    "till": ""
                },
                "details": []
            },
        ]
    },
    "education": {
        "education": [
            {
                "degree": "",
                "institution": "",
                "duration": {
                    "from": "",
                    "till": ""
                }
            },
        ]
    },
    "skills": {
        "skills": [
            {
                "title": "",
                "skills": []
            }
        ],
    },
    "certifications": {
        "certifications": [
            {
                "title": "",
                "institution": "",
                "date": "",
                "url": {
                    "title": "",
                    "link": ""
                }
            }
        ]
    },
    "others": {
        "others": [
            {
                "title": "",
                "details": []
            }
        ]
    }
}

resume_section_templates = {
    key: json.dumps(value, indent=4) for key, value in resume_section_templates.items()
}
