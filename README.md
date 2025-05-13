# DialoGPT Chatbot

A conversational AI chatbot built with Microsoft's DialoGPT model and Gradio interface.

## Features

- Interactive chat interface
- Powered by DialoGPT-medium model
- Real-time responses
- Modern web interface
- Example conversation starters
- Memory of conversation context

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git
cd ai-chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot:
```bash
python chatbot.py
```

The interface will be available at `http://localhost:7860` in your web browser.

## Technical Details

- **Model**: Microsoft DialoGPT-medium
- **Framework**: Gradio
- **Language**: Python 3.x
- **Dependencies**: PyTorch, Transformers, Gradio

## Configuration

The chatbot's response generation can be customized by adjusting these parameters in `chatbot.py`:

- `temperature`: Controls randomness (0.8 by default)
- `top_p`: Controls diversity (0.7 by default)
- `top_k`: Controls vocabulary size (100 by default)
- `max_length`: Maximum response length (1000 by default)

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [Microsoft DialoGPT](https://github.com/microsoft/DialoGPT)
- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [Gradio](https://github.com/gradio-app/gradio) 