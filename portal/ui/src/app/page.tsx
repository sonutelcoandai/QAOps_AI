"use client";

import {
  useEffect,
  useRef,
  useState,
} from "react";

import ChatBubble from "@/components/ChatBubble";
import ChatSidebar from "@/components/ChatSidebar";
import LoadingBubble from "@/components/LoadingBubble";

import { sendChat } from "@/services/chatService";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function Home() {
  const [query, setQuery] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [messages, setMessages] =
    useState<Message[]>([]);

  const bottomRef =
    useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const handleSend = async () => {

    const trimmedQuery =
      query.trim();

    if (!trimmedQuery) {
      return;
    }

    setMessages(prev => [
      ...prev,
      {
        role: "user",
        content: trimmedQuery,
      },
    ]);

    setQuery("");

    setLoading(true);

    try {

      const result =
        await sendChat(
          trimmedQuery
        );

      const answer =
        result.success
          ? (
              result.answer ??
              JSON.stringify(
                result,
                null,
                2
              )
            )
          : `⚠️ QAOps-AI could not complete the request.

Reason:
${result.error}`;

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content: answer,
        },
      ]);

    } catch {

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content:
            "⚠️ Unable to connect to QAOps-AI backend.",
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="flex h-screen bg-[#212121] text-white">

      <ChatSidebar />

      <main className="flex flex-1 flex-col">

        <div className="flex-1 overflow-y-auto">

          {messages.length === 0 ? (

            <div className="mt-24 text-center">

              <h1 className="text-5xl font-bold">
                QAOps-AI Enterprise
              </h1>

              <p className="mt-4 text-lg text-zinc-400">
                What can I help you with today?
              </p>

            </div>

          ) : (

            <div className="mx-auto max-w-5xl p-6">

              {messages.map(
                (
                  message,
                  index
                ) => (
                  <ChatBubble
                    key={index}
                    role={message.role}
                    content={message.content}
                  />
                )
              )}

              {loading && (
                <LoadingBubble />
              )}

              <div ref={bottomRef} />

            </div>

          )}

        </div>

        <div className="border-t border-zinc-800 p-6">

          <div className="mx-auto flex max-w-5xl gap-3">

            <input
              value={query}
              onChange={(e) =>
                setQuery(
                  e.target.value
                )
              }
              placeholder="Ask QAOps-AI..."
              className="flex-1 rounded-xl bg-zinc-800 p-4 outline-none"
              onKeyDown={(e) => {
                if (
                  e.key === "Enter"
                ) {
                  handleSend();
                }
              }}
            />

            <button
              disabled={loading}
              onClick={handleSend}
              className="rounded-xl bg-blue-600 px-6 hover:bg-blue-500"
            >
              {loading
                ? "Thinking..."
                : "Send"}
            </button>

          </div>

        </div>

      </main>

    </div>
  );
}