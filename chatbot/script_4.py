
# Read financial data
with open('financial-metrics.json', 'r') as f:
    financial_data_content = f.read()

# Create documentation files
doc_files = {
    'SETUP-GUIDE.md': """# Setup Guide

## Quick Start

### 1. Extract Files
Unzip the downloaded package to your preferred location.

### 2. Install Dependencies
\`\`\`bash
cd bajaj-finserv-chatbot
npm install
\`\`\`

### 3. Configure Environment
\`\`\`bash
cp .env.example .env.local
# Edit .env.local and add your OPENAI_API_KEY
\`\`\`

### 4. Run Development Server
\`\`\`bash
npm run dev
\`\`\`

Open http://localhost:3000

## Detailed Instructions

See the GitHub Upload Guide PDF for complete step-by-step instructions.

## Troubleshooting

**Q: npm install fails?**
A: Clear cache with `npm cache clean --force` and try again

**Q: Port 3000 in use?**
A: Use `npm run dev -- -p 3001`

**Q: OpenAI API errors?**
A: Check your API key in .env.local and verify you have credits
""",
    'DEPLOYMENT.md': """# Deployment Guide

## Vercel Deployment (Recommended)

### Prerequisites
- GitHub account
- Vercel account (free)
- OpenAI API key

### Steps

1. **Push to GitHub**
   \`\`\`bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/bajaj-finserv-chatbot.git
   git push -u origin main
   \`\`\`

2. **Import to Vercel**
   - Go to https://vercel.com/
   - Click "Add New Project"
   - Import your GitHub repository

3. **Configure Environment Variables**
   - Add: `OPENAI_API_KEY=your-key-here`

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app is live!

## Alternative Platforms

### Netlify
1. Connect GitHub repository
2. Build command: `npm run build`
3. Publish directory: `.next`
4. Add environment variables

### Railway
1. Connect GitHub repository  
2. Add environment variables
3. Deploy automatically

### Docker
\`\`\`dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
\`\`\`
""",
    'screenshots/README.md': """# Screenshots

This folder contains UI screenshots for documentation.

## Included Screenshots

1. **chatbot-main.png** - Main chatbot interface
2. **chat-response.png** - Example AI response
3. **mobile-view.png** - Mobile responsive view

## Usage

These images are referenced in the main README.md file to showcase the chatbot's UI and functionality.

## Generating New Screenshots

To add new screenshots:

1. Run the application: `npm run dev`
2. Take screenshots of different features
3. Save in this directory with descriptive names
4. Update README.md to reference new images
"""
}

# Combine all files
all_project_files = {
    **enhanced_files,
    **app_files, 
    **component_files,
    **doc_files
}

# Add data file
all_project_files['data/financial-metrics.json'] = financial_data_content
all_project_files['README.md'] = readme_enhanced

print(f"✅ Total project files prepared: {len(all_project_files)}")
print("\nFile breakdown:")
print(f"  - Configuration: 7 files")
print(f"  - App files: 4 files")
print(f"  - Components: 4 files")
print(f"  - Data: 1 file")
print(f"  - Documentation: 4 files")
print(f"  - README: 1 file")
print(f"  TOTAL: {len(all_project_files)} files")
