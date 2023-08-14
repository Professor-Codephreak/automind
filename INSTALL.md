# Example loading automind using Ubuntu 22.04LTS<br />
Creates Professor Codephreak<br /><br />
Professor Codephreak is an expert in machine learning, computer science and computer programming<br />
codephreak agenda: to create AUTOMINDx autonomous deployment<br />



default model llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin<br />

# Install conda<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
sudo ./Miniconda3-latest-Linux-x86_64.sh<br />
source ~/.bashrc<br />
conda create --name automind python=3.9.1<br />
conda activate automind<br />

git clone https://github.com/Professor-Codephreak/automind<br />
cd automind<br />
pip install -r requirements.txt<br />

python uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"<br />

model_name.txt in the models folder with your model will autoread. the above overwrites the call to model_name.txt<br />
models folder = models<br />
memory folder = memory<br />


-------

conda env list<br/>
conda list<br/>
conda info package_name<br/>
conda deactivate<br />
