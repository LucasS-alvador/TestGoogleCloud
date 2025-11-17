// pages/auth/callback.jsx
"use client";
import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export default function AuthCallback() {
  const router = useRouter();
  const params = useSearchParams();
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = params.get("token");
    
    if (token) {
      try {
        // Store JWT token in localStorage
        localStorage.setItem("jwt", token);
        
        // Redirect to dashboard
        router.push("/dashboard");
      } catch (err) {
        setError("Failed to save authentication token");
        console.error("Token save error:", err);
      }
    } else {
      setError("No authentication token received");
    }
  }, [params, router]);

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-red-600 mb-4">Authentication Error</h1>
          <p className="text-gray-600">{error}</p>
          <a
            href="http://localhost:3000"
            className="mt-4 inline-block px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Back to Login
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <p className="text-xl text-gray-600">Signing you in...</p>
    </div>
  );
}
