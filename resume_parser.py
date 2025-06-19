import fitz  


CSE_SKILLS = [
    
    "Python", "Java", "C++", "C", "JavaScript", "TypeScript", "C#", "Go", "Kotlin", "Swift",

    
    "HTML", "CSS", "React", "Angular", "Vue.js", "Bootstrap", "Tailwind CSS", "Next.js", "jQuery", "SASS",

    
    "Node.js", "Express.js", "Django", "Flask", "FastAPI", "Spring Boot", "Laravel", ".NET", "Ruby on Rails", "Ktor",

   
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "Redis", "Firebase", "Cassandra", "DynamoDB", "MariaDB",

    
    "Git", "Docker", "Kubernetes", "Jenkins", "GitHub Actions", "AWS", "Azure", "GCP", "CI/CD", "Terraform",

    
    "REST", "GraphQL", "SOAP", "WebSockets", "OAuth",

    
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "OpenCV", "NLP", "XGBoost", "Computer Vision",

   
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Jupyter", "Google Colab", "Tableau", "Power BI", "Data Wrangling",

    
    "Flutter", "React Native", "Android", "iOS", "SwiftUI",

   
    "OOP", "Data Structures", "Algorithms", "Operating Systems", "Computer Networks", "DBMS", "CN", "Software Engineering", "Compiler Design", "TOC",

    "VS Code", "GitHub", "Postman", "Linux", "Shell Scripting", "UML", "Agile", "Scrum", "Problem Solving", "Communication"
]


def extract_text(file_bytes):
    try:
        text = ""
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print("Error extracting text from resume:", e)
        return ""

def extract_skills_from_jd(job_desc_text):
    jd_text = job_desc_text.lower()
    found_skills = [skill for skill in CSE_SKILLS if skill.lower() in jd_text]
    return found_skills

def match_skills(resume_text, job_desc_text):
    required_skills = extract_skills_from_jd(job_desc_text)
    resume_text = resume_text.lower()
    matched = [skill for skill in required_skills if skill.lower() in resume_text]
    score = (len(matched) / len(required_skills)) * 100 if required_skills else 0
    return score, matched, required_skills
