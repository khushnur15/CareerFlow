import { ReactNode } from "react";

interface FeatureCardProps {
  icon: ReactNode;
  title: string;
  description: string;
}

function FeatureCard({
  icon,
  title,
  description,
}: FeatureCardProps) {
  return (
    <div
      className="
      bg-white/5
      border border-white/10
      rounded-3xl
      p-8
      backdrop-blur-sm
      hover:scale-105
      hover:border-purple-500/50
      transition-all
      duration-300
      shadow-xl
    "
    >
      <div className="mb-5 text-purple-400">
        {icon}
      </div>

      <h2 className="text-2xl font-semibold mb-4">
        {title}
      </h2>

      <p className="text-gray-400 leading-relaxed">
        {description}
      </p>
    </div>
  );
}

export default FeatureCard;