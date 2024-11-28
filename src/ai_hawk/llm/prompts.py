# Personal Information Template
personal_information_template = """
Answer the  ####Question#### based on the provided ####Personal Information####. Provide a one-word answer, directly based on the given ####Personal Information####.


## Example
Question: What is your city?
Milan

Personal Information: ####{resume_section}####
Question: ####{question}####
"""

# Self Identification Template
self_identification_template = """
Answer the following ###Question#### based on the provided ####Self-identification#### details.

## Example 
Question: What are your gender?
Male

Self-Identification: ####{resume_section}####
Question: ####{question}####
"""

# Legal Authorization Template
legal_authorization_template = """
Answer the following ####Question#### based on the provided ####Legal Authorization#### details.


## Example
Question: Are you legally allowed to work in the EU?
Yes

Legal Authorization: ####{resume_section}####
Question: ####{question}####
"""


# Work Preferences Template
work_preferences_template = """
Answer the following ####Question#### based on the provided ####Work Preferences####. Provide a one-word answer or short response, directly based on the given ####Work Preferences####.

## Example
Question: Are you open to remote work?
Yes

Work Preferences: ####{resume_section}####
Question: ####{question}####
"""

# Education Details Template
education_details_template = """
Answer the following ####Question#### based on the provided ####Education Details####. Provide a one-word or concise response, inferred from the given details.

## Example
Question: Do you have experience with Python?
Yes, I have experience with Python.

Education Details: ####{resume_section}####
Question: ####{question}####
"""

# Experience Details Template
experience_details_template = """
Answer the following ####Question#### based on the provided ####Experience Details####. Provide a brief and direct response, inferred from the given experience details.

## Example
Question: Do you have leadership experience?
Yes, I have 3 years of leadership experience.

Experience Details: ####{resume_section}####
Question: ####{question}####
"""

# Projects Template
projects_template = """
Answer the following ####Question#### based on the provided ####Project Details####. Provide a concise and direct response, inferred from the given project details.

## Example
Question: Have you led any projects?
Yes, led the development of a mobile app.

Projects: ####{resume_section}####
Question: ####{question}####
"""

# Availability Template
availability_template = """
Answer the following ####Question#### based on the provided ####Availability Details####. Provide a concise and direct response, inferred from the given availability details.

## Example
Question: When can you start?
I can start immediately.

Availability: ####{resume_section}####
Question: ####{question}####
"""

# Salary Expectations Template
salary_expectations_template = """
Answer the following ####Question#### based on the provided ####Salary Expectations####. Provide a concise and direct response based on the given expectations.

## Example
Question: What are your salary expectations?
55000.

Salary Expectations: ####{resume_section}####
Question: ####{question}####
"""

# Certifications Template
certifications_template = """
Answer the following ####Question#### based on the provided ####Certifications####. Provide a one-word or brief response, inferred from the given certifications.

## Example
Question: Do you have PMP certification?
Yes, I am PMP certified.

Certifications: ####{resume_section}####
Question: ####{question}####
"""

# Languages Template
languages_template = """
Answer the following ####Question#### based on the provided ####Language Skills####. Provide a one-word or concise response, inferred from the given language details.

## Example
Question: What languages do you speak?
Fluent in Italian and English.

Languages: ####{resume_section}####
Question: ####{question}####
"""

# Interests Template
interests_template = """
Answer the following ####Question#### based on the provided ####Interests####. Provide a concise response based on the given interests.

## Example
Question: What are your interests?
AI and data science.

Interests: ####{resume_section}####
Question: ####{question}####
"""

# Summarize Prompt Template
summarize_prompt_template = """
Analyze the given job description to identify the key skills and qualifications. Extract the essential technical and soft skills, educational qualifications, certifications, and relevant experiences required for the role. Provide a clear and concise summary.

## Example
Technical Skills: Python, machine learning.
Soft Skills: Communication, problem-solving.
Educational Qualifications: Bachelor's in Computer Science.
Professional Experience: 3 years in data analysis.

Job Description: ####{text}####

Summarize the job description clearly and concisely.
"""

# Cover Letter Template
coverletter_template = """
Compose a concise and impactful cover letter tailored to the provided ####Job Description#### and ####Resume####. Focus on aligning key qualifications and career objectives with the role.

## Example
Highlight relevant skills, experiences, and notable aspects of the company that align with your goals.

Job Description: ####{job_description}####
Resume: ####{resume}####
"""

# Numeric Question Template
numeric_question_template = """
Evaluate the resume and respond with the number of years of experience related to the specific ####Question####. Estimate relevant experience based on education, projects, and professional background. Avoid zero as a response.

## Example
Question: How many years of experience do you have with AI?
2

Resume: ####{resume_educations}####
         ####{resume_jobs}####
         ####{resume_projects}####
Question: ####{question}####
"""

# Options Template
options_template = """
Based on the given ####Resume#### and ####Job Application Profile####, choose the best-suited option for the provided ####Question####. Provide only one option from the list.

## Example
Question: How many years of experience do you have with Python?
Options: [1-2, 3-5, 6-10, 10+]
Answer: 10+

Resume: ####{resume}####
Job Application Profile: ####{job_application_profile}####
Question: ####{question}####
Options: ####{options}####
"""

# Try to Fix Template
try_to_fix_template = """
Use the provided ####Error#### to adjust the ####Input#### text. Ensure the response is valid, concise, and adheres to the error guidelines.

## Example
Question: Enter a whole number between 3 and 30.
Input: 50
Error: Must be between 3 and 30.
Fixed Input: 30.

Form Question: ####{question}####
Input: ####{input}####
Error: ####{error}####
"""

# Function Summarize Prompt Template
func_summarize_prompt_template = """
Remove all placeholders (e.g., [[placeholder]]) from the text, adapting the content as needed. Ensure the final text flows naturally without placeholders.

## Example
Text with placeholders: "I am experienced in [[technology]] and have worked for [[years_of_experience]] years."
Text without placeholders: "I am experienced and have worked for several years."

Text with placeholders: ####{text_with_placeholders}####
"""

# Is Relevant Position Template
is_relavant_position_template = """
Evaluate whether the given ####Resume#### aligns with the ####Job Description####. Provide a suitability score (1-10) and a brief reasoning.

## Example
Score: 8
Reasoning: Meets most requirements but lacks advanced certifications.

Job Description: ####{job_description}####
Resume: ####{resume}####
"""

# Resume or Cover Letter Template
resume_or_cover_letter_template = """
Identify if the phrase pertains to a resume or a cover letter. Respond with "resume" or "cover" based on the context.

## Example
Phrase: Upload resume.
Answer: resume.

Phrase: ####{phrase}####
"""

# Determine Section Template
determine_section_template = """
Identify the most relevant resume section for the given ####Question####. Respond with one of the following:
- Personal Information
- Self Identification
- Legal Authorization
- Work Preferences
- Education Details
- Experience Details
- Projects
- Availability
- Salary Expectations
- Certifications
- Languages
- Interests
- Cover Letter

Question: ####{question}####
"""