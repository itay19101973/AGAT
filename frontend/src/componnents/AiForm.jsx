// src/components/ChatForm.jsx
import React, { useState } from "react";
import axios from "axios";

const ChatForm = () => {
    const [question, setQuestion] = useState("");
    const [response, setResponse] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [privateDataId , setPrivateDataId] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError("");
        setResponse("");
        try {
            let data;
            if (privateDataId !== "") {
                data = {Prompt: question ,PrivateDataID: privateDataId.trim() };
            }
            else{
                data = {Prompt: question}
            }

            const res = await axios.post("MyProxy/", data);
            setResponse(res.data.response);
        } catch (err) {
            console.error(err);
            setError("Failed to get response from backend.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ maxWidth: "500px", margin: "50px auto" }}>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Ask a question..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    style={{width: "100%", padding: "10px", marginBottom: "10px"}}
                    required
                />
                <input
                    type="text"
                    placeholder="add private document id"
                    value={privateDataId}
                    onChange={(e) => setPrivateDataId(e.target.value)}
                    style={{width: "100%", padding: "10px", marginBottom: "10px"}}
                />
                <button type="submit" disabled={loading} style={{padding: "10px 20px"}}>
                    {loading ? "Sending..." : "Submit"}
                </button>
            </form>

            {response && (
                <div style={{marginTop: "20px", padding: "10px", background: "#f0f0f0"}}>
                    <strong>Response:</strong>
                    <p>{response}</p>
                </div>
            )}

            {error && (
                <div style={{marginTop: "20px", color: "red" }}>
                    <p>{error}</p>
                </div>
            )}
        </div>
    );
};

export default ChatForm;