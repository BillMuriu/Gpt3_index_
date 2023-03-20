from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os

os.envirom["OPENAI_API_KEY"] = ""

def CreatevectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20