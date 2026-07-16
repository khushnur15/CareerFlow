function Sidebar() {
  return (
    <aside className="w-72 bg-white/5 border-r border-white/10 p-6">
      <h1 className="text-3xl font-bold text-purple-400 mb-10">
        CareerFlow
      </h1>

      <nav className="space-y-4">
        <div className="p-4 rounded-xl bg-purple-600">
          Dashboard
        </div>

        <div className="p-4 rounded-xl hover:bg-white/10 cursor-pointer transition">
          Resume
        </div>

        <div className="p-4 rounded-xl hover:bg-white/10 cursor-pointer transition">
          Jobs
        </div>

        <div className="p-4 rounded-xl hover:bg-white/10 cursor-pointer transition">
          Roadmap
        </div>
      </nav>
    </aside>
  );
}

export default Sidebar;