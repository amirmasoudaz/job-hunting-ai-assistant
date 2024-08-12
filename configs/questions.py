from configs.question_sets import administrative
from configs.question_sets import creative
from configs.question_sets import customer_service
from configs.question_sets import education_teaching
from configs.question_sets import executive
from configs.question_sets import operational
from configs.question_sets import professional
from configs.question_sets import research_development
from configs.question_sets import sales_marketing
from configs.question_sets import social_work_nonprofit
from configs.question_sets import technical

from configs.question_sets import role_compatibility

from configs.question_sets import swot


application_questions = {
    "Administrative": administrative.questions,
    "Creative": creative.questions,
    "Customer Service": customer_service.questions,
    "Education and Training": education_teaching.questions,
    "Executive": executive.questions,
    "Operational": operational.questions,
    "Professional": professional.questions,
    "Research and Development": research_development.questions,
    "Sales and Marketing": sales_marketing.questions,
    "Non-Profit and Social Services": social_work_nonprofit.questions,
    "Technical": technical.questions
}
description_questions = role_compatibility.questions
swot_analysis = swot.questions
