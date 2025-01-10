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

## Transformation Operations

1. AddNestedFor
```
+   checker1 = 465
+   checker2= 464
+   for index in range(checker1 // checker2):
        for H in Hs:
            maxH = H
```
2. AddNestedIf
```
+    checker1 = 352
+    checker2 = 647
+    if checker1 & checker2:
         if X > t:
             answer = X - t
```
3. CreatFunctions
```
+   def AddElements(h, H, w, W):
+       return H * W - (h * W + w * H - h * w)

-   ans = H * W - (h * W + w * H - h * w)
+   ans = AddElements(h, H, w, W)
```

4. Third-Party API Calls (AddBase64)
```
import base64
base64.b64encode(b'Random String')
```

5. TransformLoopToRecursion
```
+    def recursive_function(i):
+        if i >= 5:
+            return None
+        if str(a[i])[-1] == '0': \
+            dic.update({i: 0})
+        else:
+            dic.update({i: \
+           int(str(a[i])[-1]) - 10})
+        recursive_function(i + 1)

-   for i in range(5):
-   if str(a[i])[-1] == "0":
-       dic.update({i: 0})
-   else:
-       dic.update({i: int(str(a[i])
- [-1]) - 10})

+   recursive_function(0)
```


