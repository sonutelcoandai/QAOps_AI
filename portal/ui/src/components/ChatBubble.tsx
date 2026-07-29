"use client";

import ReactMarkdown from "react-markdown";

type Props = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatBubble({
  role,
  content,
}: Props) {
  const isUser = role === "user";

  return (
    <div
      className={`mb-8 flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >
      <div
        className={`max-w-4xl rounded-2xl p-4 ${
          isUser
            ? "bg-blue-600"
            : "bg-zinc-800"
        }`}
      >
        {isUser ? (
          <div>{content}</div>
        ) : (
          <div className="prose prose-invert max-w-none">
            <ReactMarkdown>
              {content}
            </ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}