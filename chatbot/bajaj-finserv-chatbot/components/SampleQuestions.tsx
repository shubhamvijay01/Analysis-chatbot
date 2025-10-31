const SAMPLE_QUESTIONS = [
  "What is Gross NPAs for Bajaj Finance?",
  "Show me consolidated PAT growth for Q1",
  "How did BAGIC perform this quarter?",
  "What is BALIC's VNB growth rate?",
  "Tell me about Bajaj Housing Finance's asset quality",
  "Compare solvency ratios across insurance subsidiaries",
];

export default function SampleQuestions({
  onQuestionClick
}: {
  onQuestionClick: (question: string) => void
}) {
  return (
    <div>
      <h3 className="font-semibold text-gray-800 mb-4 text-lg">
        💡 Sample Questions
      </h3>
      <div className="space-y-2">
        {SAMPLE_QUESTIONS.map((question, index) => (
          <button
            key={index}
            onClick={() => onQuestionClick(question)}
            className="w-full text-left px-4 py-3 text-sm bg-gray-50 hover:bg-blue-50 hover:border-blue-200 border border-gray-200 rounded-lg transition-all duration-200 text-gray-700 hover:text-blue-900"
          >
            <span className="block truncate">{question}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
