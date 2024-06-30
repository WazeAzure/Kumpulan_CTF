"use client";
import React, { useState } from "react";
import axios from "axios";

export default function Home() {
  const [messages, setMessages] = useState([
    { text: "Teman bercakap, kirimkan aku pesan.", isSentByUser: false }
  ]);
  const [inputText, setInputText] = useState("");

  const sendMessage = async () => {
    if (inputText.trim() === "") return;

    const newSentMessage = { text: inputText, isSentByUser: true };
    setMessages(prevMessages => [...prevMessages, newSentMessage]);
    setInputText("");

    try {
      // const response = await axios.get(`/api/chat?pesan=${inputText}`);
      const response = await axios.get(`http://localhost:1204/api.php?pesan=${inputText}`);
      if (response.data) {
        const receivedMessage = { text: response.data.response, isSentByUser: false };
        setMessages(prevMessages => [...prevMessages, receivedMessage]);
      } else {
        console.error(response.data.message);
      }
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="flex flex-col flex-grow w-full max-w-xl bg-white shadow-xl rounded-lg overflow-hidden">
        <div className="flex flex-col flex-grow h-0 p-4 overflow-auto">
          {messages.map((message, index) => (
            <div key={index} className={`flex w-full mt-2 max-w-xs ${message.isSentByUser ? "ml-auto justify-end" : ""}`}>
              <div className={`${message.isSentByUser ? "bg-blue-600 text-white rounded-l-lg rounded-br-lg" : "bg-gray-300 rounded-r-lg rounded-bl-lg"} p-3`}>
                <p className="text-sm">{message.text}</p>
              </div>
            </div>
          ))}
        </div>
        <div className="bg-gray-300 p-4">
          <input
            className="flex items-center h-10 w-full rounded px-3 text-sm"
            type="text"
            placeholder="Type your message…"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
          />
        </div>
      </div>
    </main>
  );
}
