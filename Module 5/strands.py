import boto3

class Agent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        self.client = boto3.client('bedrock-runtime')
    
    def generate(self, messages):
        response = self.client.converse(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            messages=messages,
            system=[{"text": self.system_prompt}]
        )
        
        class Message:
            def __init__(self, content):
                self.content = content
        
        class Response:
            def __init__(self, message):
                self.message = message
        
        content = response['output']['message']['content'][0]['text']
        return Response(Message(content))
