
# Add component files
component_files = {
    'components/ChatInterface.tsx': """'use client';

import { useState } from 'react';
import MessageBubble from './MessageBubble';
import SampleQuestions from './SampleQuestions';
import TypingIndicator from './TypingIndicator';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: string[];
  timestamp?: string;
}

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = async (text?: string) => {
    const messageText = text || input;
    if (!messageText.trim()) return;

    const userMessage: Message = {
      role: 'user',
      content: messageText,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: messageText }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const data = await response.json();

      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response,
        sources: data.sources,
        timestamp: data.timestamp
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      
      const errorMessage: Message = {
        role: 'assistant',
        content: 'I apologize, but I encountered an error processing your request. Please try again.',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="w-80 bg-white border-r border-gray-200 shadow-lg">
        <div className="p-6 border-b border-gray-200">
          <div className="flex items-center space-x-3">
            <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-xl">B</span>
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-900">Bajaj Finserv</h2>
              <p className="text-sm text-gray-600">Financial Assistant</p>
            </div>
          </div>
        </div>
        
        <div className="p-6">
          <SampleQuestions onQuestionClick={sendMessage} />
        </div>
      </div>

      <div className="flex-1 flex flex-col">
        <div className="bg-white border-b border-gray-200 shadow-sm p-4">
          <div className="max-w-4xl mx-auto">
            <h1 className="text-2xl font-bold text-gray-900">Q1 FY2026 Financial Chatbot</h1>
            <p className="text-sm text-gray-600">Ask questions about Bajaj Finserv's quarterly performance</p>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          <div className="max-w-4xl mx-auto space-y-6">
            {messages.length === 0 && (
              <div className="text-center py-20">
                <div className="inline-block p-8 bg-white rounded-2xl shadow-lg">
                  <h2 className="text-3xl font-bold text-gray-900 mb-4">
                    Welcome to Bajaj Finserv Chatbot
                  </h2>
                  <p className="text-gray-600 mb-6">
                    I can help you understand Q1 FY2026 financial performance
                  </p>
                  <div className="flex flex-wrap gap-2 justify-center">
                    <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                      NPAs
                    </span>
                    <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">
                      Growth Metrics
                    </span>
                    <span className="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm">
                      Insurance
                    </span>
                  </div>
                </div>
              </div>
            )}

            {messages.map((message, index) => (
              <MessageBubble key={index} message={message} />
            ))}

            {isLoading && <TypingIndicator />}
          </div>
        </div>

        <div className="border-t border-gray-200 bg-white p-4 shadow-lg">
          <div className="max-w-4xl mx-auto">
            <div className="flex gap-3">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Ask about GNPA, PAT, AUM, or other metrics..."
                className="flex-1 px-6 py-4 border-2 border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900 placeholder-gray-500"
                disabled={isLoading}
              />
              <button
                onClick={() => sendMessage()}
                disabled={isLoading || !input.trim()}
                className="px-8 py-4 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all duration-200 shadow-md hover:shadow-lg"
              >
                {isLoading ? 'Sending...' : 'Send'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
""",
    'components/MessageBubble.tsx': """interface Message {
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
""",
    'components/SampleQuestions.tsx': """const SAMPLE_QUESTIONS = [
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
""",
    'components/TypingIndicator.tsx': """export default function TypingIndicator() {
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
"""
}

print(f"✅ Added {len(component_files)} component files")
