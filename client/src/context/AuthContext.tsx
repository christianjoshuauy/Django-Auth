import { createContext, useState, ReactNode, useEffect } from "react";
import axiosInstance from "../axiosInstance";

interface AuthContextType {
  isAuthenticated: boolean;
  isLoading: boolean;
  setAuthenticated: (authStatus: boolean) => void;
}

export const AuthContext = createContext<AuthContextType>({
  isAuthenticated: false,
  isLoading: true,
  setAuthenticated: () => {},
});

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [isAuthenticated, setAuthenticated] = useState(false);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await axiosInstance.get("/api/token/refresh/");
        if (response.data.access_token) {
          setAuthenticated(true);
          setLoading(false);
        }
      } catch (error) {
        console.error("Auth check failed", error);
      }
    };

    checkAuth();
  }, []);

  return (
    <AuthContext.Provider
      value={{ isAuthenticated, isLoading, setAuthenticated }}
    >
      {children}
    </AuthContext.Provider>
  );
};
