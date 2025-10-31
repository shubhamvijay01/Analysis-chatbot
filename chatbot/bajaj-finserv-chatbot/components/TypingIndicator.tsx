export default function TypingIndicator() {
  return (
    <div className="flex justify-start">
      <div className="bg-white border-2 border-gray-200 px-6 py-4 rounded-2xl shadow-md">
        <div className="flex space-x-2 items-center">
          <span className="text-sm text-gray-600 mr-2">AI is thinking</span>
          <div className="w-2 h-2 bg-blue-500 rounded-full animate-bounce"></div>
          <div
            className="w-2 h-2 bg-blue-500 rounded-full animate-bounce"
            style={{ animationDelay: '0.2s' }}
          ></div>
          <div
            className="w-2 h-2 bg-blue-500 rounded-full animate-bounce"
            style={{ animationDelay: '0.4s' }}
          ></div>
        </div>
      </div>
    </div>
  );
}
