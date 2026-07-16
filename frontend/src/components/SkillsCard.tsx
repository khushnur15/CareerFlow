function SkillsCard() {
  const skills = [
    "Python",
    "FastAPI",
    "React",
    "TypeScript",
    "PostgreSQL",
    "Machine Learning",
    "REST API",
    "Git",
    "Docker",
    "AWS"
  ];

  return (
    <div className="bg-white/5 border border-white/10 rounded-3xl p-8">
      <h2 className="text-2xl font-bold mb-6">
        Skills Detected
      </h2>

      <div className="flex flex-wrap gap-3">
        {skills.map((skill) => (
          <div
            key={skill}
            className="bg-purple-600 px-4 py-2 rounded-full"
          >
            {skill}
          </div>
        ))}
      </div>
    </div>
  );
}

export default SkillsCard;