# app/llm_integration.py
import torch
from transformers import pipeline

# Check if GPU is available and print the status
cuda_available = torch.cuda.is_available()
print(f"CUDA is available: {cuda_available}")

# Set the device based on CUDA availability
device = 0 if cuda_available else -1  # Use GPU if available, otherwise CPU

# Specify the model you want to use
model_name = "sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization", model=model_name)

def generate_summary(text):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
