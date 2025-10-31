
import json

# Recreate financial data
financial_data = {
    "quarter": "Q1 FY2026",
    "period": "April - June 2025",
    "report_date": "July 25, 2025",
    "consolidated": {
        "revenue": {
            "q1_fy2026": 35451,
            "q1_fy2025": 31480,
            "growth_percent": 13,
            "unit": "crores"
        },
        "pat": {
            "q1_fy2026": 2789,
            "q1_fy2025": 2138,
            "growth_percent": 30,
            "unit": "crores",
            "note": "All-time high quarterly PAT"
        }
    },
    "bajaj_finance": {
        "gnpa": {
            "q1_fy2026": 1.03,
            "q1_fy2025": 0.86,
            "change": 0.17,
            "unit": "percent"
        },
        "nnpa": {
            "q1_fy2026": 0.50,
            "q1_fy2025": 0.38,
            "unit": "percent"
        },
        "aum": {
            "q1_fy2026": 441450,
            "growth_percent": 25,
            "unit": "crores"
        },
        "pat": {
            "q1_fy2026": 4765,
            "q1_fy2025": 3912,
            "growth_percent": 22,
            "unit": "crores"
        }
    },
    "bajaj_housing": {
        "gnpa": {
            "q1_fy2026": 0.30,
            "q1_fy2025": 0.28,
            "unit": "percent"
        },
        "nnpa": {
            "q1_fy2026": 0.13,
            "unit": "percent"
        },
        "aum": {
            "q1_fy2026": 120420,
            "growth_percent": 24,
            "unit": "crores"
        }
    },
    "bagic": {
        "name": "Bajaj Allianz General Insurance",
        "gwp": {
            "q1_fy2026": 5202,
            "q1_fy2025": 4761,
            "growth_percent": 9,
            "unit": "crores"
        },
        "combined_ratio": 103.6,
        "roe": 21.4,
        "solvency": 334
    },
    "balic": {
        "name": "Bajaj Allianz Life Insurance",
        "vnb": {
            "q1_fy2026": 145,
            "q1_fy2025": 104,
            "growth_percent": 39,
            "unit": "crores"
        },
        "nbm": {
            "q1_fy2026": 11.1,
            "q1_fy2025": 6.9,
            "unit": "percent"
        },
        "pat": {
            "q1_fy2026": 171,
            "q1_fy2025": 97,
            "growth_percent": 76,
            "unit": "crores"
        }
    }
}

financial_data_content = json.dumps(financial_data, indent=2)

# Documentation files
doc_files = {
    'SETUP-GUIDE.md': """# Setup Guide

## Quick Start

### 1. Extract Files
Unzip the downloaded package to your preferred location.

### 2. Install Dependencies
```bash
cd bajaj-finserv-chatbot
npm install
```

### 3. Configure Environment
```bash
cp .env.example .env.local
# Edit .env.local and add your OPENAI_API_KEY
```

### 4. Run Development Server
```bash
npm run dev
```

Open http://localhost:3000

## Detailed Instructions

See the GitHub Upload Guide PDF for complete step-by-step instructions.
""",
    'DEPLOYMENT.md': """# Deployment Guide

## Vercel Deployment (Recommended)

### Steps

1. **Push to GitHub**
2. **Import to Vercel** 
3. **Add Environment Variables**: OPENAI_API_KEY
4. **Deploy**

Your app will be live in 2-3 minutes!
""",
    'screenshots/README.md': """# Screenshots

This folder contains UI screenshots for documentation.

## Included Screenshots

1. **chatbot-main.png** - Main chatbot interface
2. **chat-response.png** - Example AI response  
3. **mobile-view.png** - Mobile responsive view

These images are referenced in the main README.md file.
"""
}

# Combine all files
with open('README-enhanced.md', 'r', encoding='utf-8') as f:
    readme_enhanced = f.read()

all_project_files = {
    **enhanced_files,
    **app_files,
    **component_files,
    **doc_files
}

all_project_files['data/financial-metrics.json'] = financial_data_content
all_project_files['README.md'] = readme_enhanced

print(f"✅ Total project files prepared: {len(all_project_files)}")
