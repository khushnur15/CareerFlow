SKILLS_DATABASE = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "FastAPI",
    "Flask",
    "Django",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Git",
    "Docker",
    "AWS",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn"
]


def extract_skills(text: str):
    found_skills = []

    for skill in SKILLS_DATABASE:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills