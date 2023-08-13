# this will update soon

# Example of loading automind using Ubuntu 22.04LTS<br />
Put the model in the models folder<br />
add the model name to model_name.txt<br />
llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin<br />

git clone https://github.com/Professor-Codephreak/automind<br />
cd automind<br />
pip install -r requirements.txt<br />

# Install conda<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
./Miniconda3-latest-Linux-x86_64.sh<br />
source ~/.bashrc<br />
conda create --name automind python=3.9.1<br />
conda activate automind<br />
#conda deactivate<br />



python uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"

model_name.txt in the models folder with your model will autoread. the above overwrites the call to model_name.txt
