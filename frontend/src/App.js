import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {

      axios.get("users/")
        .then((response) => {
          setMessage(response.data.respond);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          setMessage("Failed to fetch message");
        });
  }, []);

  return (
      <div className="App">
        <h1>Backend Message:</h1>
        <p>{message}</p>
      </div>
  );
}

export default App;
