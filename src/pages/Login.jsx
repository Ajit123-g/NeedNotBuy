import { useState } from "react";
import { supabase } from "../lib/supabase";

function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    const { data, error } =
      await supabase.auth.signInWithPassword({
        email,
        password,
      });

    if (error) {
      alert(error.message);
      return;
    }

    console.log("Logged in:", data.user);

  };

  return (
    <div className="max-w-md mx-auto mt-20 p-8 bg-white rounded-2xl shadow">

      <h1 className="text-2xl font-bold mb-6">
        Welcome Back
      </h1>

      <input
        className="border p-3 w-full rounded-lg mb-4"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        className="border p-3 w-full rounded-lg mb-4"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={handleLogin}
        className="bg-green-600 text-white w-full p-3 rounded-lg"
      >
        Login
      </button>

    </div>
  );
}

export default Login;
