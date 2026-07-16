import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import FeatureCard from "../components/FeatureCard";

import {
  FileText,
  Briefcase,
  Target,
  Map,
} from "lucide-react";

function LandingPage() {
  return (
    <div className="min-h-screen bg-black text-white">
      <Navbar />

      <HeroSection />

      <section className="grid md:grid-cols-2 xl:grid-cols-4 gap-8 px-10 pb-24">
        <FeatureCard
          icon={<FileText size={40} />}
          title="Resume Analysis"
          description="Extract skills and technologies automatically from uploaded resumes."
        />

        <FeatureCard
          icon={<Briefcase size={40} />}
          title="Career Matching"
          description="Discover the roles that align with your current skill set."
        />

        <FeatureCard
          icon={<Target size={40} />}
          title="Skill Gaps"
          description="Identify missing technologies and competencies."
        />

        <FeatureCard
          icon={<Map size={40} />}
          title="Learning Roadmap"
          description="Receive a personalized growth path for your target role."
        />
      </section>
    </div>
  );
}

export default LandingPage;