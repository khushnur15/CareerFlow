import { useState } from "react";

function ResumeUpload() {
  const [uploaded, setUploaded] = useState(false);

  const handleUpload = () => {
    setTimeout(() => {
      setUploaded(true);
    }, 1500);
  };

  return (
    <div className="bg-white/5 border border-white/10 rounded-3xl p-8 mb-8">
      <h2 className="text-2xl font-bold mb-4">
        Resume Upload
      </h2>

      <input
        type="file"
        onChange={handleUpload}
        className="w-full p-4 rounded-xl bg-black border border-gray-700"
      />

      {uploaded && (
        <div className="mt-6 space-y-3">
          <div className="text-green-400">
            ✅ Resume uploaded successfully
          </div>

          <div className="text-green-400">
            ✅ 12 skills extracted
          </div>

          <div className="text-green-400">
            ✅ 8 matching roles generated
          </div>

          <div className="text-green-400">
            ✅ Personalized roadmap created
          </div>
        </div>
      )}
    </div>
  );
}

export default ResumeUpload;