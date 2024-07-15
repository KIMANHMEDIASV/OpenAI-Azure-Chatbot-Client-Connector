from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import json

from chatbot_client.client import ChatbotClient
from chatbot_client.exceptions import ChatbotClientError, ResourceNotFoundError

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the ChatbotClient
API_KEY = "your-api-key"  # Replace with your actual API key
client = ChatbotClient("https://chatbot-dev.example.com", api_key=API_KEY)
print("ChatbotClient initialized")

class ChatCreateByBotCodeRequest(BaseModel):
    bot_id: str

class ChatCompletionRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    chat_id: str

class MessageResponse(BaseModel):
    assistant_message: str

async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.post("/api/chats/create/bybotcode", response_model=ChatResponse)
async def create_chat_by_bot_code(request: ChatCreateByBotCodeRequest):
    print(f"Creating chat with bot ID: {request.bot_id}")
    try:
        chat = client.create_chat(request.bot_id)
        print(f"Created chat: {json.dumps(chat, indent=2)}")
        return ChatResponse(chat_id=chat['chatId'])
    except ChatbotClientError as e:
        print(f"Error creating chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chats/{chat_id}/completions", response_model=MessageResponse)
async def chat_completion(chat_id: str, request: ChatCompletionRequest):
    print(f"Sending message to chat ID: {chat_id}")
    print(f"Message content: {request.message}")
    try:
        response = client.chat_completion(chat_id, request.message)
        print(f"Received full response: {json.dumps(response, indent=2)}")
        assistant_message = response['assistantMessage']
        print(f"Extracted assistant message: {assistant_message}")
        return MessageResponse(assistant_message=assistant_message)
    except ResourceNotFoundError:
        print(f"Chat not found: {chat_id}")
        raise HTTPException(status_code=404, detail="Chat not found")
    except ChatbotClientError as e:
        print(f"Error in chat completion: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return FileResponse("index.html")

if __name__ == "__main__":
    print("Starting server...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)