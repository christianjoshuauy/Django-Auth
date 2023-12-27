import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/useAuth";
import axiosInstance from "../axiosInstance";

function Home() {
  const navigate = useNavigate();
  const { setAuthenticated } = useAuth();

  const handleLogout = async () => {
    try {
      await axiosInstance.get("/api/logout");
      setAuthenticated(false);

      navigate("/");
    } catch (error) {
      console.error("Logout failed", error);
    }
  };

  return (
    <div>
      <h1>Home Page</h1>
      <p>This is a simple home page for testing authentication.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Home;
