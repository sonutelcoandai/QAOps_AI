"use client";

type Props = {
  metadata: {
    agent?: string;
    provider?: string;
    model?: string;
    workflow?: string;
  };
};

export default function ExecutionDetails({
  metadata,
}: Props) {
  return (
    <div className="mt-4 rounded-xl border border-zinc-700 bg-zinc-900 p-4 text-sm">

      <h3 className="mb-3 font-semibold">
        Execution Details
      </h3>

      <div>
        <strong>Agent:</strong>{" "}
        {metadata.agent || "-"}
      </div>

      <div>
        <strong>Provider:</strong>{" "}
        {metadata.provider || "-"}
      </div>

      <div>
        <strong>Model:</strong>{" "}
        {metadata.model || "-"}
      </div>

      <div>
        <strong>Workflow:</strong>{" "}
        {metadata.workflow || "-"}
      </div>

    </div>
  );
}