import { Link } from "react-router-dom";

function Landing() {
  return (
    <div>
      <h1>Welcome to Our App</h1>
      <Link to="/signup">Signup</Link>
      <Link to="/login">Login</Link>
    </div>
  );
}

export default Landing;
