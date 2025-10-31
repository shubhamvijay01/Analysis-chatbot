import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Bajaj Finserv Financial Chatbot',
  description: 'AI-powered chatbot for Bajaj Finserv quarterly earnings analysis',
  keywords: ['Bajaj Finserv', 'Financial Chatbot', 'AI', 'Quarterly Earnings'],
  authors: [{ name: 'Your Name' }],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
