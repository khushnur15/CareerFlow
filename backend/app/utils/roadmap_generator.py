ROADMAPS = {
    "Backend Developer": [
        "REST APIs",
        "Docker",
        "Redis",
        "AWS",
        "Microservices"
    ],

    "Python Developer": [
        "Advanced Python",
        "Design Patterns",
        "Docker",
        "Testing",
        "AWS"
    ],

    "Full Stack Developer": [
        "TypeScript",
        "Next.js",
        "Docker",
        "System Design",
        "AWS"
    ],

    "AI Engineer": [
        "LLM",
        "Prompt Engineering",
        "RAG",
        "Vector Databases",
        "LangChain"
    ],

    "Data Scientist": [
        "Pandas",
        "NumPy",
        "Deep Learning",
        "Statistics",
        "MLOps"
    ]
}


def generate_roadmap(job_matches):
    roadmap = []

    if not job_matches:
        return roadmap

    best_role = job_matches[0]["role"]

    if best_role in ROADMAPS:
        for index, skill in enumerate(
            ROADMAPS[best_role],
            start=1
        ):
            roadmap.append(
                {
                    "step": index,
                    "skill": skill
                }
            )

    return roadmap