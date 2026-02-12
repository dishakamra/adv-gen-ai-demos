from strands import Agent

# Configure the agent with a specific prompting strategy
outline_agent = Agent(
    name="OutlineGenerator",
    system_prompt="""Generate a comprehensive outline for {topic} that includes:
    - Main sections (5-7)
    - Key points for each section
    - Logical flow between sections"""
)

# Generate the initial outline
outline_response = outline_agent.generate(
    messages=[{"role": "user", "content": "Create an outline for a technical guide on AWS Lambda"}]
)

outline = outline_response.message.content
print(f"Generated Outline:\n{outline}")