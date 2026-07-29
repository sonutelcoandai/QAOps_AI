"use client";

export default function LoadingBubble() {
  return (
    <div className="mb-8 flex justify-start">

      <div className="rounded-2xl bg-zinc-800 p-4">

        <div className="animate-pulse">
          QAOps‑AI is thinking...
        </div>

      </div>

    </div>
  );
}