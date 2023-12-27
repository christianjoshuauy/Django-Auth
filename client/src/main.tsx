import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import Landing from "./pages/Landing";
import { AuthProvider } from "./context/AuthContext.tsx";
import PublicRoute from "./components/PublicRoute.tsx";
import AuthenticatedRoute from "./components/AuthenticatedRoute.tsx";
import TestPage from "./pages/TestPage.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route element={<PublicRoute />}>
            <Route path="/" element={<Landing />} />
            <Route path="signup" element={<Signup />} />
            <Route path="login" element={<Login />} />
          </Route>
          <Route element={<AuthenticatedRoute />}>
            <Route path="home" element={<Home />} />
            <Route path="test" element={<TestPage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
