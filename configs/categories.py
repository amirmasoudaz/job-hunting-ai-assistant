categories = {
    "Technical": {
        "definition": "Technical roles require specialized knowledge in science, technology, engineering, and mathematics (STEM) to develop, maintain, or improve technical systems and products.",
        "keywords": ["software", "engineering", "developer", "data science", "IT", "artificial intelligence", "programming", "cybersecurity", "system architecture", "STEM", "technical", "hardware"]
    },
    "Creative": {
        "definition": "Creative roles primarily involve artistic creativity or content creation, including design, media production, writing, and advertising.",
        "keywords": ["design", "advertising", "media", "arts", "content", "writing", "creative", "graphic design", "video production", "copy writing", "photography"]
    },
    "Administrative": {
        "definition": "Administrative roles are mainly focused on supporting businesses through clerical work, organization, and management of daily office operations.",
        "keywords": ["administrative", "clerical", "support", "office management", "secretary", "coordinator", "assistant", "receptionist", "data entry", "office operations"]
    },
    "Professional": {
        "definition": "Professional positions are specialized roles that typically require advanced education and qualifications in fields such as law, finance, healthcare, and academia.",
        "keywords": ["legal", "financial", "healthcare", "academic", "professional services", "consultancy", "lawyer", "doctor", "nurse", "accountant", "professor", "expert", "specialist"]
    },
    "Operational": {
        "definition": "Operational jobs involve the operation, maintenance, and management of processes in industries like manufacturing, logistics, and construction.",
        "keywords": ["manufacturing", "logistics", "operations", "construction", "facilities", "warehouse", "production", "maintenance", "supply chain", "process management"]
    },
    "Customer Service": {
        "definition": "Customer Service roles are focused on assisting customers by providing information, resolving issues, and ensuring a satisfactory customer experience.",
        "keywords": ["customer service", "support", "retail", "hospitality", "help desk", "client relations", "call center", "customer experience", "complaint resolution"]
    },
    "Executive": {
        "definition": "Executive roles are high-level management positions responsible for making strategic decisions and overseeing the operations of a company or organization.",
        "keywords": ["executive", "C-suite", "director", "management", "leadership", "strategic", "decision-making", "CEO", "CFO", "COO", "CTO", "president"]
    },
    "Sales and Marketing": {
        "definition": "Sales and Marketing positions drive business growth through sales strategies, market research, and promotional activities.",
        "keywords": ["sales", "marketing", "business development", "market research", "promotions", "advertising", "branding", "public relations", "salesforce"]
    },
    "Research and Development": {
        "definition": "Research and Development roles mainly focus on the creation of knowledge, products, and technologies through systematic research.",
        "keywords": ["research", "development", "innovation", "scientific", "product development", "biotech", "R&D", "experimentation", "discovery", "invention"]
    },
    "Education and Training": {
        "definition": "Education and Training positions are primarily involved in the education and training of individuals, including academic, vocational, and corporate settings.",
        "keywords": ["education", "training", "teaching", "academic", "curriculum", "pedagogy", "instructor", "e-learning", "corporate training", "coaching"]
    },
    "Non-Profit and Social Services": {
        "definition": "Non-Profit and Social Services roles are dedicated to improving societal issues, providing community service, and supporting advocacy efforts through various non-profit organizations.",
        "keywords": ["non-profit", "NGO", "social services", "community service", "advocacy", "charity", "humanitarian", "volunteer", "social justice", "community development"]
    }
}


category_list = [
    "Technical",
    "Creative",
    "Administrative",
    "Professional",
    "Operational",
    "Customer Service",
    "Executive",
    "Sales and Marketing",
    "Research and Development",
    "Education and Training",
    "Non-Profit and Social Services"
]

category_keymap = [(key, value["definition"], " ".join(value["keywords"])) for key, value in categories.items()]