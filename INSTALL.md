Example of loading automind using Ubuntu<br />
Put the model in the models folder<br />
add the model name to model_name.txt<br />
llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin<br />

git clone https://github.com/Professor-Codephreak/automind<br />
cd automind<br />
pip install -r requirements.txt<br />
huggingface-cli login<br />
https://huggingface.co/settings/tokens<br /><br />

Install conda<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
./Miniconda3-latest-Linux-x86_64.sh<br />
source ~/.bashrc<br />
conda create --name automind<br />
conda activate automind<br />
#conda deactivate<br />



python uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"
