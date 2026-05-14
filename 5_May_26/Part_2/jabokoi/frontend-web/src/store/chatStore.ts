import { create } from 'zustand';
import apiClient from '../api/apiClient';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

interface ChatState {
  currentConversationId: string | null;
  messages: Message[];
  isLoading: boolean;
  setConversation: (id: string, messages: Message[]) => void;
  addMessage: (message: Message) => void;
  sendMessage: (content: string) => Promise<void>;
}

export const useChatStore = create<ChatState>((set, get) => ({
  currentConversationId: null,
  messages: [],
  isLoading: false,
  setConversation: (id, messages) => set({ currentConversationId: id, messages }),
  addMessage: (message) => set((state) => ({ messages: [...state.messages, message] })),
  sendMessage: async (content) => {
    const { currentConversationId, addMessage } = get();
    addMessage({ role: 'user', content });
    
    set({ isLoading: true });
    try {
      const response = await apiClient.post('/chat/send/', {
        conversation_id: currentConversationId,
        message: content
      });
      addMessage({ role: 'assistant', content: response.data.message });
    } catch (error) {
      console.error('Failed to send message', error);
      addMessage({ role: 'assistant', content: 'Sorry, something went wrong. Please try again.' });
    } finally {
      set({ isLoading: false });
    }
  },
}));
