## Instruction to run CODEMIND:
```cd scripts/ces```

IER Tasks:  
```python ier.py --model $MODEL_ID --dataset $DATASET --cache $CACHE_DIR```

SR Tasks:  
No Test:
```python sr.py --model $MODEL_ID --dataset $DATASET --cache $CACHE_DIR```  
With Test:
```python sr.py --model $MODEL_ID --dataset $DATASET --cache $CACHE_DIR --use_test```  
Misleading Test:
```python sr.py --model $MODEL_ID --dataset $DATASET --cache $CACHE_DIR --misleading```

CSR Taks:  
```python csr.py --model $MODEL_ID --dataset $DATASET --cache $CACHE_DIR```

```MODEL_ID```: Currently our framework supports following OpenAI and huggingface models:  ```codellama/CodeLlama-13b-Instruct-hf```, ```codellama/CodeLlama-13b-hf```,  ```codellama/CodeLlama-13b-Instruct-hf```,```codellama/CodeLlama-7b-hf```,  ```codellama/CodeLlama-7b-Instruct-hf```, ```codellama/CodeLlama-34b-Instruct-hf``` ```codellama/CodeLlama-13b-hf```,```deepseek-ai/deepseek-coder-6.7b-instruct```, ```deepseek-ai/deepseek-coder-33b-instruct```,```deepseek-ai/deepseek-coder-6.7b-base```, ```ise-uiuc/Magicoder-S-DS-6.7B```, ```bigcode/starcoder```, ```bigcode/starcoder2-15b```, ```gpt-4-turbo```,
```gemini/gemini-1.5-pro```, ```semcoder/semcoder_s```

```CACHE_DIR```: the directory to save huggingface checkpoints.

```Dataset```: Avatar, humaneval, classeval, cruxeval
