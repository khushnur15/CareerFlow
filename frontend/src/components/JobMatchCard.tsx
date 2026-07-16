function JobMatchCard() {
  const jobs = [
    { role: "Backend Developer", score: 94 },
    { role: "Python Developer", score: 92 },
    { role: "Full Stack Developer", score: 88 },
    { role: "ML Engineer", score: 81 },
  ];

  return (
    <div className="bg-white/5 border border-white/10 rounded-3xl p-8">
      <h2 className="text-2xl font-bold mb-6">
        Career Matches
      </h2>

      {jobs.map((job) => (
        <div key={job.role} className="mb-6">
          <div className="flex justify-between mb-2">
            <span>{job.role}</span>
            <span>{job.score}%</span>
          </div>

          <div className="w-full bg-gray-800 rounded-full h-3">
            <div
              className="bg-purple-500 h-3 rounded-full"
              style={{ width: `${job.score}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}

export default JobMatchCard;