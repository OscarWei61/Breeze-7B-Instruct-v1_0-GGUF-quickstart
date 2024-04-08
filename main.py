from ctransformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained(
    "YC-Chen/Breeze-7B-Instruct-v1_0-GGUF",
    model_file="breeze-7b-instruct-v1_0-q6_k.gguf",
    model_type="mistral",
    context_length=8000,
    gpu_layers=50)

tokenizer = AutoTokenizer.from_pretrained("MediaTek-Research/Breeze-7B-Instruct-v1_0")

gen_kwargs = dict(
    max_new_tokens=1024,
    repetition_penalty=1.1,
    stop=["[INST]"],
    temperature=0.0,
    top_p=0.0,
    top_k=1,
)

chat = [
  {"role": "system", "content": "You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan."},
  {"role": "user", "content": "請跟我介紹一下聯發科是甚麼公司"}
]

for text in llm(tokenizer.apply_chat_template(chat, tokenize=False), stream=True, **gen_kwargs):
    print(text, end="", flush=True)
