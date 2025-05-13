# DialoGPT Chatbot

A simple implementation of a chatbot using Microsoft's DialoGPT-medium model with a Gradio interface. This project demonstrates basic conversational AI capabilities while acknowledging the model's limitations.

## Demo Screenshots

Interface demonstration:

![Initial Interface](example/Screenshot%202025-05-13%20133147.png)
*Main interface view*

![Chat Example](example/Screenshot%202025-05-13%20133221.png)
*Example conversation*

![Advanced Interaction](example/Screenshot%202025-05-13%20133324.png)
*Response demonstration*

## Features

- Basic chat interface
- DialoGPT-medium model integration
- Real-time response generation
- Clean web interface
- Preset conversation examples
- Context retention capability

## Installation

1. Clone the repository:
```bash
git clone https://github.com/333william333/Example-Project-AI-Powered-Chatbot.git
cd Example-Project-AI-Powered-Chatbot
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

Launch the application:
```bash
python chatbot.py
```

Access the interface at `http://localhost:7860` in your web browser.

## Technical Details

- **Model**: DialoGPT-medium
- **Framework**: Gradio
- **Language**: Python 3.x
- **Dependencies**: PyTorch, Transformers, Gradio

## Configuration

Parameters in `chatbot.py`:
- `temperature`: 0.8 (Response randomness)
- `top_p`: 0.7 (Output diversity)
- `top_k`: 100 (Vocabulary limitation)
- `max_length`: 1000 (Response length)

## Model Limitations

This implementation uses a basic model suitable for:
- Educational purposes
- Experimentation
- Basic conversation practice

Not suitable for:
- Production environments
- Critical applications
- Professional deployment

## License

MIT License

## Contributing

Contributions and improvements are welcome via pull requests.

## Acknowledgments

- Microsoft DialoGPT
- Hugging Face
- Gradio 