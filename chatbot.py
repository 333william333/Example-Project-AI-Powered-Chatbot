import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Initialize conversation history
class Chatbot:
    def __init__(self):
        self.chat_history_ids = None
    
    def chat(self, message, history):
        # Encode user input
        new_input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')

        # Append to chat history if it exists
        if self.chat_history_ids is not None:
            bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids

        # Generate response
        self.chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8
        )
        
        # Decode and return the response
        response = tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

# Create Chatbot instance
chatbot = Chatbot()

# Create the Gradio interface
with gr.Blocks(css="footer {visibility: hidden}") as demo:
    gr.Markdown("""# AI Chatbot
    This is a conversational AI powered by DialoGPT. Feel free to start a conversation!
    """)
    
    chatbot_interface = gr.ChatInterface(
        fn=chatbot.chat,
        title="AI Assistant",
        description="Chat with DialoGPT",
        examples=[
            "Hello! How are you today?",
            "What's your favorite book?",
            "Tell me an interesting fact."
        ]
    )

if __name__ == "__main__":
    demo.launch(share=True) 