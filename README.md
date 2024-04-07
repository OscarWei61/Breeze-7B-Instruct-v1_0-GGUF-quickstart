# Breeze-7B-Instruct-v1_0-GGUF-quickstart
This repository helps users quickly get started with the Breeze-7B-Instruct-v1_0-GGUF language model and install related packages.

# Model information

Huggingface : https://huggingface.co/YC-Chen/Breeze-7B-Instruct-v1_0-GGUF

# Parameter Runtime Comparison Table

Set gpu_layers to the number of layers to offload to the GPU. If no GPU acceleration is available on your system, set it to 0. Below is a comparison of how different parameters affect runtime

Hardware Specifications:
- CPU: 8 vCPU
- RAM: 90 GB
- GPU: NVIDIA Tesla V100/32GB

| Parameter   | Runtime (seconds) |
|:------------:|:-------------------:|
| gpu_layers = 0 | 13.1                |
| gpu_layers = 50 | 103.3                |

# How to install

Install Anaconda (If you have already installed Anaconda, please jump to next step.)
```Shell Script
# 1.Download Anaconda
wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 2.Install Anaconda
bash /tmp/Anaconda3-2020.02-Linux-x86_64.sh
```
 
Run the following command to set up the environment:  
```Shell Script
# git clone
git clone https://github.com/OscarWei61/Breeze-7B-Instruct-v1_0-GGUF-quickstart.git
cd Breeze-7B-Instruct-v1_0-GGUF-quickstart
```
_Note: Using Python 3.7 may encounter errors, whereas Python 3.9 works smoothly. Default install python 3.9 version._
```Shell Script
# 2.Run env setup script
# default to install ctransformers with no GPU acceleration.
conda create --name Breeze --file ./requirements.txt
```
<details>
<summary>
If you want to install ctransformers with CUDA GPU acceleration, you need to uninstall ctransform and replace with:
</summary>

```Shell Script
pip install ctransformers[cuda]
```
</details>

# How to run the program
```Shell Script
# 1.Activate Conda env
conda activate Breeze
python main.py
```

# Modifying Input Content

You can customize the instructions in `main.py` by modifying the content below.


For example, I want to ask "請跟我介紹一下聯發科是甚麼公司".
```python
chat = [
  {"role": "system", "content": "You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan."},
  {"role": "user", "content": "請跟我介紹一下聯發科是甚麼公司"}
]
```

Answer:
```
聯發科技（MediaTek Inc.），是一家成立於1997年的半導體設計公司。主要業務包括行動通訊、智慧家庭、車用電子等領域的晶片設計與研發。聯發科技在全球各地都有分支機構，致力於提供高品質且具競爭力的產品給客戶。

聯發科技的核心業務是開發各種晶片，如應用處理器（AP）、基頻晶片（Baseband Chip）、無線網路晶片（Wi-Fi、Bluetooth等）、多媒體處理器（DSP）、電源管理晶片（PMIC）等。這些晶片廣泛應用於智慧型手機、平板電腦、電視、路由器、車用電子等產品，為客戶提供完整的解決方案。

聯發科技在行動通訊領域具有豐富的經驗，其晶片被全球知名品牌廠商採用，如華為、小米、OPPO、vivo、三星等。此外，聯發科技也積極拓展智慧家庭、物聯網、人工智慧等新興市場，為客戶提供更全面的解決方案。

聯發科技在技術創新方面不遺餘力，每年投入大量資金用於研發，以保持競爭力並滿足客戶需求。截至目前，聯發科技已獲得超過10,000
```