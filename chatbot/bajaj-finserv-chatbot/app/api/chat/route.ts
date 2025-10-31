import { NextRequest, NextResponse } from 'next/server';
import { OpenAI } from 'openai';
import financialData from '@/data/financial-metrics.json';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export async function POST(req: NextRequest) {
  try {
    const { message } = await req.json();

    if (!message || typeof message !== 'string') {
      return NextResponse.json(
        { error: 'Invalid message format' },
        { status: 400 }
      );
    }

    const context = createFinancialContext(financialData);

    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [
        {
          role: 'system',
          content: `You are a financial analyst assistant for Bajaj Finserv Limited. 
          You help answer questions about the company's Q1 FY2026 quarterly performance.

          ${context}

          Guidelines:
          - Provide specific numbers and percentages from the data
          - Always cite the quarter (Q1 FY2026 vs Q1 FY2025)
          - Format currency values in crores with ₹ symbol
          - Mention growth rates when comparing periods
          - Be professional and precise
          - If asked about data not available, say so clearly
          - Keep responses concise but informative`
        },
        {
          role: 'user',
          content: message
        }
      ],
      temperature: 0.1,
      max_tokens: 500,
    });

    const response = completion.choices[0].message.content;

    return NextResponse.json({
      response,
      sources: ['Q1 FY2026 Earnings Call Transcript', 'Q1 FY2026 Investor Presentation'],
      timestamp: new Date().toISOString()
    });

  } catch (error: any) {
    console.error('Chat API Error:', error);

    return NextResponse.json(
      {
        error: 'Failed to process your request',
        details: error.message
      },
      { status: 500 }
    );
  }
}

function createFinancialContext(data: any): string {
  return `
Financial Data for ${data.quarter} (${data.period}):

CONSOLIDATED RESULTS:
- Revenue: ₹${data.consolidated.revenue.q1_fy2026} crores (${data.consolidated.revenue.growth_percent}% YoY growth)
- PAT: ₹${data.consolidated.pat.q1_fy2026} crores (${data.consolidated.pat.growth_percent}% YoY growth)

BAJAJ FINANCE LIMITED (BFL):
- GNPA: ${data.bajaj_finance.gnpa.q1_fy2026}% (Q1 FY2026) vs ${data.bajaj_finance.gnpa.q1_fy2025}% (Q1 FY2025)
- NNPA: ${data.bajaj_finance.nnpa.q1_fy2026}% (Q1 FY2026) vs ${data.bajaj_finance.nnpa.q1_fy2025}% (Q1 FY2025)
- AUM: ₹${data.bajaj_finance.aum.q1_fy2026} crores (${data.bajaj_finance.aum.growth_percent}% growth)
- PAT: ₹${data.bajaj_finance.pat.q1_fy2026} crores (${data.bajaj_finance.pat.growth_percent}% growth)

BAJAJ HOUSING FINANCE (BHFL):
- GNPA: ${data.bajaj_housing.gnpa.q1_fy2026}%
- NNPA: ${data.bajaj_housing.nnpa.q1_fy2026}%
- AUM: ₹${data.bajaj_housing.aum.q1_fy2026} crores (${data.bajaj_housing.aum.growth_percent}% growth)

BAGIC (General Insurance):
- GWP: ₹${data.bagic.gwp.q1_fy2026} crores (${data.bagic.gwp.growth_percent}% growth)
- Combined Ratio: ${data.bagic.combined_ratio}%
- ROE: ${data.bagic.roe}%

BALIC (Life Insurance):
- VNB: ₹${data.balic.vnb.q1_fy2026} crores (${data.balic.vnb.growth_percent}% growth)
- NBM: ${data.balic.nbm.q1_fy2026}% (up from ${data.balic.nbm.q1_fy2025}%)
- PAT: ₹${data.balic.pat.q1_fy2026} crores (${data.balic.pat.growth_percent}% growth)
`;
}
