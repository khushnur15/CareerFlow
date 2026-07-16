function RoadmapCard() {
  const roadmap = [
    "Master FastAPI",
    "Learn Docker",
    "Learn Redis",
    "Learn AWS",
    "CI/CD Fundamentals",
  ];

  return (
    <div className="bg-white/5 border border-white/10 rounded-3xl p-8">
      <h2 className="text-2xl font-bold mb-6">
        Learning Roadmap
      </h2>

      <div className="space-y-4">
        {roadmap.map((step, index) => (
          <div
            key={step}
            className="bg-purple-600/20 border border-purple-500/20 rounded-xl p-4"
          >
            Step {index + 1}: {step}
          </div>
        ))}
      </div>
    </div>
  );
}

export default RoadmapCard;