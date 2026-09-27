from google.adk.agents import LlmAgent

finance_ai_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-3.5-flash-lite",
    description="A financial analysis assistant that can analyze financial data and provide insights.",
    instruction="""
        You are a financial analysis assistant.

        Analyze financial data and explain the results clearly.
        Do not invent market data.

        If current market data is required, use an appropriate
        data-retrieval tool rather than making up information.
    """,
)

root_agent = finance_ai_agent