
import zipfile
import io
import os
import json

# Create enhanced ZIP with screenshots and documentation

# Previous files
enhanced_files = {}

# Add all the previous source files
enhanced_files['package.json'] = json.dumps({
    "name": "bajaj-finserv-chatbot",
    "version": "1.0.0",
    "description": "AI-powered financial chatbot for Bajaj Finserv quarterly earnings analysis",
    "private": True,
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "next lint"
    },
    "dependencies": {
        "@langchain/openai": "^0.3.0",
        "@pinecone-database/pinecone": "^3.0.0",
        "ai": "^3.4.0",
        "langchain": "^0.3.0",
        "next": "14.2.0",
        "openai": "^4.65.0",
        "pdf-parse": "^1.1.1",
        "react": "^18.3.0",
        "react-dom": "^18.3.0",
        "react-markdown": "^9.0.1",
        "remark-gfm": "^4.0.0"
    },
    "devDependencies": {
        "@types/node": "^20",
        "@types/react": "^18",
        "@types/react-dom": "^18",
        "autoprefixer": "^10.4.20",
        "eslint": "^8",
        "eslint-config-next": "14.2.0",
        "postcss": "^8.4.47",
        "tailwindcss": "^3.4.0",
        "typescript": "^5"
    }
}, indent=2)

enhanced_files['next.config.js'] = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig
"""

enhanced_files['tsconfig.json'] = json.dumps({
    "compilerOptions": {
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": True,
        "skipLibCheck": True,
        "strict": True,
        "noEmit": True,
        "esModuleInterop": True,
        "module": "esnext",
        "moduleResolution": "bundler",
        "resolveJsonModule": True,
        "isolatedModules": True,
        "jsx": "preserve",
        "incremental": True,
        "plugins": [{"name": "next"}],
        "paths": {
            "@/*": ["./*"]
        }
    },
    "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
    "exclude": ["node_modules"]
}, indent=2)

enhanced_files['tailwind.config.ts'] = """import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
};
export default config;
"""

enhanced_files['postcss.config.js'] = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

enhanced_files['.gitignore'] = """# dependencies
/node_modules
/.pnp
.pnp.js
.yarn/install-state.gz

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local
.env

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
"""

enhanced_files['.env.example'] = """# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Pinecone Configuration (Optional)
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_INDEX_NAME=bajaj-finserv-docs
PINECONE_ENVIRONMENT=us-east-1-aws

# Application Configuration
NEXT_PUBLIC_APP_NAME=Bajaj Finserv Financial Chatbot
NEXT_PUBLIC_APP_URL=http://localhost:3000
"""

print("✅ Prepared configuration files")
print(f"Total config files: {len(enhanced_files)}")
