# backend/ai_agent.py
import openai
from typing import List, Dict, Any, Optional
import logging
from shared.config import config

logger = logging.getLogger(__name__)


class AIAgent:
    """AI Agent for processing user messages"""

    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=config.OPENAI_API_KEY)
        self.model = config.OPENAI_MODEL
        self.system_prompt = self._get_system_prompt()

    def _get_system_prompt(self) -> str:
        """System prompt for AI assistant"""
        return """You are an experienced AI assistant specializing in helping developers.
Your capabilities include:
- Explaining programming concepts in simple terms
- Assisting with debugging and code optimization
- Providing architectural advice and best practices
- Answering technical questions
- Helping choose the right technologies and tools

Communication rules:
- Respond clearly and to the point
- Include code examples when helpful
- Break down complex topics step by step
- If unsure about the answer, say so honestly
- Use emojis moderately to enhance readability
- Respond in the same language the question was asked
Remember the context of previous messages in the conversation."""

    async def process_message(
            self,
            message: str,
            user_id: int,
            conversation_history: List[Dict[str, Any]] = None
    ) -> str:
        """Process a user's message"""
        try:
            # Build conversation context
            messages = [{"role": "system", "content": self.system_prompt}]

            # Add conversation history (last 10 messages)
            if conversation_history:
                for item in conversation_history[-10:]:
                    messages.append({"role": "user", "content": item["user_message"]})
                    messages.append({"role": "assistant", "content": item["ai_response"]})

            # Add current message
            messages.append({"role": "user", "content": message})

            # Send request to OpenAI
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=2000,
                temperature=0.7,
                top_p=0.9,
                frequency_penalty=0.1,
                presence_penalty=0.1
            )

            ai_response = response.choices[0].message.content.strip()
            logger.info(f"AI response generated for user {user_id}")

            return ai_response

        except Exception as e:
            logger.error(f"Error in AI processing: {e}")
            return "❌ Sorry, an error occurred while processing your request. Please try again."
