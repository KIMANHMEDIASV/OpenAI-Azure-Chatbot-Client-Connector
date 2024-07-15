from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class ChatCreateRequest(BaseModel):
    botId: str

class ChatCreateResponse(BaseModel):
    chatId: str
    botId: str
    botDisplayName: str
    botDisplayMessage: str
    botDescription: str
    botSampleQuestion1: Optional[str] = None
    botSampleQuestion2: Optional[str] = None
    isUserSystemMessageSupported: bool

class ChatCompletionRequest(BaseModel):
    userMessage: str
    ignoreChatHistory: bool = False
    isAdminChat: bool = False
    isTraceLogEnabled: bool = False

class ChatCompletionMetaData(BaseModel):
    tags: Optional[List[str]] = None
    sources: Optional[List[Dict[str, str]]] = None

class ChatCompletionResponse(BaseModel):
    completionId: str
    chatId: str
    userMessage: str
    assistantMessage: str
    promptTokens: int
    completionTokens: int
    totalTokens: int
    botId: str
    botDisplayName: str
    botDisplayMessage: str
    botDescription: str
    chatDisplayName: Optional[str] = None
    metaData: Optional[ChatCompletionMetaData] = None
    traceLog: Optional[str] = None

class BotFeedbackRequest(BaseModel):
    chatId: str
    userMessage: str
    assistantMessage: str
    messageCreatedUtc: datetime
    userComment: Optional[str] = None
    voteId: int

class BotFeedbackResponse(BaseModel):
    feedbackId: str

class GetBotsResponseItem(BaseModel):
    botId: str
    code: str
    displayName: str
    displayMessage: str
    sampleQuestion1: Optional[str] = None
    sampleQuestion2: Optional[str] = None
    description: str
    modelName: Optional[str] = None
    isStartBot: bool
    createdUtc: datetime
    updatedUtc: datetime

class PagingResult(BaseModel):
    pageNumber: int
    totalPageCount: int
    pageSize: int
    totalItemCount: int
    hasPrevious: bool
    hasNext: bool

class GetBotsResponse(PagingResult):
    items: List[GetBotsResponseItem]

class UserSystemMessage(BaseModel):
    userSystemMessageId: str
    displayName: str
    systemMessage: str

class CurrentUser(BaseModel):
    id: int
    login: str
    roles: List[str]
    isTermsAccepted: bool
    isKeepChatHistory: bool
    keepChatHistoryForDays: int
    isKeepFavoritesForever: bool

class UpdateUserRequest(BaseModel):
    isKeepChatHistory: bool
    keepChatHistoryForDays: int
    isKeepFavoritesForever: bool

class SystemMessage(BaseModel):
    value: str

class TokenUsageStatistic(BaseModel):
    requestDate: datetime
    botId: str
    botDisplayName: str
    tokenUsageTypeId: int
    userCount: int
    requestCount: int
    promptTokens: int
    completionTokens: int
    totalTokens: int

# Add more models as needed for other operations