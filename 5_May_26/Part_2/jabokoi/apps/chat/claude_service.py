import os
from anthropic import Anthropic
from django.conf import settings

class ClaudeService:
    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        if self.api_key:
            self.client = Anthropic(api_key=self.api_key)
        else:
            self.client = None

    def get_system_prompt(self, user_context=None):
        base_prompt = """
You are the Jabo Koi (যাবো কই) travel assistant — an AI built specifically for Bangladesh travel planning. You speak Bengali and English fluently. Your name means "Where shall we go?" and your job is to help users plan trips within Bangladesh by asking about their budget, dates, and preferences — then generating a detailed, realistic travel plan.

Rules:
- Always check the current month/season before suggesting destinations
- Warn users if their chosen destination is risky during monsoon (June–September)
- All prices must be in BDT (Bangladeshi Taka) unless user requests USD
- Ask one question at a time — do not overwhelm the user
- Budget categories: Budget (under ৳15,000 total), Mid-range (৳15,000–৳40,000), Premium (৳40,000+)
- Hotel budget categories: Budget (under ৳1,500/night), Mid (৳1,500–৳4,000), Premium (৳4,000+)
- When generating a plan, include: transport from Dhaka, hotel recommendation, day-by-day activities, food suggestions, and total estimated cost breakdown
- If user is NRB, acknowledge they may not know current BD prices and be extra clear
- Keep responses concise and friendly. Use "ভাই/আপু" tone when speaking Bengali.
"""
        if user_context:
            base_prompt += f"\nUser Context: {user_context}"
        
        return base_prompt

    def send_message(self, messages, user_context=None):
        if not self.client:
            return self.get_demo_response(messages)

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620", # or the latest version
                max_tokens=1024,
                system=self.get_system_prompt(user_context),
                messages=messages
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error calling Claude API: {e}")
            return "I'm having trouble connecting to my brain right now. (Claude API Error)"

    def get_demo_response(self, messages):
        # Very basic demo logic for prototype without API key
        last_message = messages[-1]['content'].lower()
        
        if "hello" in last_message or "hi" in last_message or "সালাম" in last_message:
            return "সালাম ভাই/আপু! আমি যাবো কই (Jabo Koi) আপনার ট্রাভেল এসিস্ট্যান্ট। আপনি বাংলাদেশের কোথায় ঘুরতে যেতে চান?"
        
        if "cox" in last_message:
            return "কক্সবাজার চমৎকার জায়গা! আপনি কবে যেতে চাচ্ছেন এবং আপনার বাজেট কেমন?"
        
        return "ধন্যবাদ! আমি আপনার জন্য একটি ট্রাভেল প্ল্যান তৈরি করছি। (Demo Mode: Real AI logic requires ANTHROPIC_API_KEY)"
