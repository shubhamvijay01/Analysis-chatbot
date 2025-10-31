interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: string[];
  timestamp?: string;
}

export default function MessageBubble({ message }: { message: Message }) {
  const isUser = message.role === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-2xl px-6 py-4 rounded-2xl shadow-md ${
          isUser
            ? 'bg-blue-600 text-white'
            : 'bg-white border-2 border-gray-200 text-gray-900'
        }`}
      >
        <p className="whitespace-pre-wrap leading-relaxed">{message.content}</p>

        {message.sources && message.sources.length > 0 && (
          <div className="mt-3 pt-3 border-t border-gray-300">
            <p className="text-xs text-gray-500 font-medium">
              📄 Sources: {message.sources.join(', ')}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
