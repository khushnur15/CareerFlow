JOB_ROLE_SKILLS = {
    "Python Developer": [
        "Python",
        "SQL",
        "Git"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "REST API"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "FastAPI"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "LLM",
        "Prompt Engineering"
    ],

    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ]
}


def match_jobs(user_skills):
    matched_roles = []

    for role, required_skills in JOB_ROLE_SKILLS.items():

        matched_count = 0

        for skill in required_skills:
            if skill in user_skills:
                matched_count += 1

        match_percentage = (
            matched_count / len(required_skills)
        ) * 100

        if match_percentage >= 50:
            matched_roles.append(
                {
                    "role": role,
                    "match_percentage": round(
                        match_percentage,
                        2
                    )
                }
            )

    matched_roles.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return matched_roles