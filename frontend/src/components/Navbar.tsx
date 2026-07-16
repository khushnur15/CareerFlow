import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="flex justify-between items-center px-10 py-6 border-b border-gray-800">
      <h1 className="text-3xl font-bold text-purple-500">
        CareerFlow
      </h1>

      <div className="space-x-4">
        <Link
          to="/login"
          className="px-5 py-2 border border-gray-700 rounded-lg hover:border-purple-500 transition"
        >
          Login
        </Link>

        <Link
          to="/register"
          className="px-5 py-2 bg-purple-600 rounded-lg hover:bg-purple-700 transition"
        >
          Register
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;