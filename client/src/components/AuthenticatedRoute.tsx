import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/useAuth";

function AuthenticatedRoute() {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  return <Outlet />;
}

export default AuthenticatedRoute;
