from pydantic import BaseModel
from fastapi import APIRouter

from portal.adapters.chat_adapter import ChatAdapter

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
def chat(request: ChatRequest):

    return ChatAdapter.ask(request.query)
