"use client";
import { useRef, useState, useEffect } from "react";
import { FaArrowAltCircleUp } from "react-icons/fa";
import { baseUrl } from "@/utils/constants";
import axios from "axios";
import MarkdownRenderer from "@/app/components/MarkdownRenderer";

interface Message {
  senderType: string;
  content: string;
}

const ChatPage = () => {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [textareaHeight, setTextareaHeight] = useState(44);
  const [text, setText] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);

  const handleTextChange = () => {
    const textarea = textareaRef.current;
    if (!textarea) return;
    textarea.style.height = "auto";
    const maxHeight = 200;
    const newHeight = Math.min(maxHeight, textarea.scrollHeight);
    textarea.style.height = `${newHeight}px`;
    setTextareaHeight(newHeight);
    textarea.style.overflowY =
      textarea.scrollHeight > maxHeight ? "auto" : "hidden";
  };

  const formSubmitHandler = async () => {
    try {
      if (!text.trim()) return alert("Input text is empty");
      setMessages((prev) => [...prev, { senderType: "user", content: text }]);
      setText("");
      // Reset textarea height
      if (textareaRef.current) {
        textareaRef.current.style.height = "44px";
        setTextareaHeight(44);
      }

      const response = await axios.post(
        `${baseUrl}/chat/message`,
        {
          message: text,
          user_id: "a4bc04e0-24f3-4916-a167-ac5b51fe303d",
          pesona_id: "6edf44cf-6b93-4d84-8177-5c2b89ddd92a",
          role: "user",
        },
        { withCredentials: true }
      );

      console.log("response of AI -> ", response);
      setMessages((prev) => [
        ...prev,
        { content: response.data.response, senderType: "assistant" },
      ]);
    } catch (error) {
      console.log("ERROR: ", error);
    }
  };

  // Auto scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      formSubmitHandler();
    }
  };

  const inputContainerHeight = textareaHeight + 170; // textarea + padding + button

  return (
    <div className="h-screen flex flex-col bg-white">
      {/* Messages Container - Takes remaining space and scrolls */}
      <div
        className="flex-1 overflow-y-auto"
        style={{
          paddingBottom: `${inputContainerHeight}px`,
          transition: "padding-bottom 0.1s ease-out",
        }}
      >
        <div className="max-w-5xl mx-auto p-4">
          {messages.length === 0 ? (
            <div className="flex items-center justify-center h-full text-gray-400">
              <p>No messages yet. Start a conversation!</p>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div
                key={idx}
                className={`mb-4 flex ${
                  msg.senderType === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`max-w-sm lg:max-w-md px-4 py-2 rounded-lg text-[17px] ${
                    msg.senderType === "user"
                      ? "bg-gray-600 text-white rounded-br-none"
                      : "bg-transparent text-black rounded-bl-none min-w-full"
                  }`}
                >
                  <p className="break-words">
                    {msg.senderType === "user" ? (
                      msg.content
                    ) : (
                      <MarkdownRenderer
                        mdContent={msg.content}
                      ></MarkdownRenderer>
                    )}
                  </p>
                </div>
              </div>
            ))
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Fixed Input Container */}
      <div className="fixed bottom-0 left-0 right-0 w-full z-30">
        {/* Centered wrapper for max-width constraint */}

        <div className="max-w-5xl mx-auto px-4 py-4 flex flex-col items-center relative">
          {/* Video */}
          <video
            src={"/gradient.mp4"}
            className="w-full absolute left-1/2 -translate-x-1/2 bottom-0 rounded-2xl h-44 object-cover z-20 mb-10"
            autoPlay
            loop
            muted
          />

          {/* TextArea - Fixed at bottom */}
          <div
            className=" bottom-0 bg-gray-100 rounded-2xl box-border z-30 mb-11"
            style={{ width: "calc(100% - 2rem)" }}
          >
            <div className="flex flex-col-reverse p-4">
              <textarea
                onInput={handleTextChange}
                ref={textareaRef}
                placeholder="Ask your question to Warren Buffet's Persona"
                className="pt-2 w-full px-4 outline-none resize-none font-sans"
                style={{
                  minHeight: "44px",
                  maxHeight: "200px",
                  overflow: "hidden",
                }}
                value={text}
                onChange={(e) => {
                  setText(e.target.value);
                  handleTextChange();
                }}
                onKeyDown={handleKeyDown}
              />
            </div>
            <div className="flex w-full items-center py-2 sm:py-3 justify-end px-4">
              <button
                onClick={formSubmitHandler}
                className="px-2 py-1 bg-sky-500 hover:bg-sky-600 rounded-md transition-colors"
              >
                <FaArrowAltCircleUp className="text-xl text-white" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;
