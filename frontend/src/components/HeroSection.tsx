function HeroSection() {
  return (
    <section className="flex flex-col items-center justify-center text-center py-32 px-6">
      <h1 className="text-6xl font-bold max-w-5xl leading-tight">
        AI Career Intelligence
        <br />
        for Developers 🚀
      </h1>

      <p className="text-gray-400 text-xl mt-8 max-w-3xl">
        Upload your resume, discover your strengths,
        identify missing skills, and generate a personalized
        roadmap to your dream role.
      </p>

      <div className="flex gap-4 mt-10">
        <button className="bg-purple-600 hover:bg-purple-700 px-8 py-4 rounded-xl text-lg font-semibold">
          Analyze Resume
        </button>

        <button className="border border-gray-700 hover:border-purple-500 px-8 py-4 rounded-xl text-lg font-semibold">
          View Demo
        </button>
      </div>
    </section>
  );
}

export default HeroSection;