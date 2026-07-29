"use client";

export default function ChatSidebar() {
  return (
    <aside className="w-64 border-r border-zinc-800 p-4">

      <button className="w-full rounded-lg bg-zinc-800 p-3 hover:bg-zinc-700">
        + New Chat
      </button>

      <div className="mt-8">

        <div className="mb-3 text-sm text-zinc-500">
          Conversations
        </div>

        <div className="cursor-pointer rounded-lg p-2 hover:bg-zinc-800">
          TMF641 Review
        </div>

        <div className="cursor-pointer rounded-lg p-2 hover:bg-zinc-800">
          Billing Analysis
        </div>

      </div>

    </aside>
  );
}