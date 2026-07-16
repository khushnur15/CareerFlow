import Sidebar from "../components/Sidebar";
import ResumeUpload from "../components/ResumeUpload";
import SkillsCard from "../components/SkillsCard";
import JobMatchCard from "../components/JobMatchCard";
import RoadmapCard from "../components/RoadmapCard";

function DashboardPage() {
  return (
    <div className="min-h-screen bg-black text-white flex">
      <Sidebar />

      <main className="flex-1 p-8 overflow-y-auto">

        {/* Header */}
        <div className="mb-10">
          <h1 className="text-5xl font-bold mb-2">
            Welcome Back, Khushnur 👋
          </h1>

          <p className="text-gray-400 text-lg">
            Your AI Career Intelligence Dashboard
          </p>
        </div>

        {/* Metrics */}
        <div className="grid md:grid-cols-4 gap-6 mb-10">

          <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
            <p className="text-gray-400">Resume Score</p>
            <h2 className="text-5xl font-bold text-purple-400">88%</h2>
          </div>

          <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
            <p className="text-gray-400">Skills Found</p>
            <h2 className="text-5xl font-bold text-purple-400">12</h2>
          </div>

          <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
            <p className="text-gray-400">Job Matches</p>
            <h2 className="text-5xl font-bold text-purple-400">8</h2>
          </div>

          <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
            <p className="text-gray-400">Roadmap Steps</p>
            <h2 className="text-5xl font-bold text-purple-400">5</h2>
          </div>

        </div>

        <ResumeUpload />

        <div className="grid lg:grid-cols-2 gap-8 mt-8">
          <SkillsCard />
          <JobMatchCard />
        </div>

        <div className="mt-8">
          <RoadmapCard />
        </div>

      </main>
    </div>
  );
}

export default DashboardPage;