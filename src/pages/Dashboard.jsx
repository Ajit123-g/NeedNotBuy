import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Dashboard() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBookings();
  }, []);

  const fetchBookings = async () => {
    try {
      const response = await api.get("/api/bookings/my");
      setBookings(response.data);
    } catch (error) {
      console.error("Failed to fetch bookings:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/login");
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div className="min-h-screen p-8 bg-gray-50">

      <h1 className="text-3xl font-bold">
        NeedNotBuy Dashboard
      </h1>

      {/* Welcome card */}
      <div className="bg-white p-6 mt-6 rounded-2xl shadow">
        <h2 className="text-xl font-semibold">Welcome!</h2>

        <p className="mt-3">Logged in as:</p>

        <p className="text-green-600 font-semibold">
          {user?.email}
        </p>

        <button
          onClick={handleLogout}
          className="bg-red-600 text-white px-6 py-3 rounded-xl mt-6"
        >
          Logout
        </button>
      </div>

      {/* Bookings */}
      <h2 className="text-xl font-semibold mt-8">My Bookings</h2>

      {loading ? (
        <p className="mt-4 text-gray-500">Loading bookings...</p>
      ) : bookings.length === 0 ? (
        <p className="mt-4 text-gray-500">
          You don't have any bookings yet.
        </p>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          {bookings.map((booking) => (
            <div
              key={booking.id}
              className="bg-white p-5 rounded-xl shadow"
            >
              <h3 className="font-bold">{booking.item?.title}</h3>

              <p>
                {booking.start_date} → {booking.end_date}
              </p>

              <p className="mt-2">₹{booking.total_amount}</p>

              <p className="mt-2">Status: {booking.status}</p>
            </div>
          ))}
        </div>
      )}

    </div>
  );
}

export default Dashboard;