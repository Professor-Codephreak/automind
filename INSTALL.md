-----------------------------------

To install right click "Save link as ..." [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install) chmod +x automind.install && automind.install

## [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)

detailed and verbose procedure
1. Right-click the following link: [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)
2. Choose "Save link as..." or "Download linked file" from the context menu.
3. Select a location on your computer to save the file.
4. from the terminal
5. chmod +x automind.install && ./automind.install


---------------------------------<br />


# Example loading automind using <a href="https://ubuntu.com/desktop/flavours">Ubuntu 22.04LTS</a><br />

Creates Professor Codephreak<br /><br />
Professor Codephreak is an expert in machine learning, computer science and computer programming<br />
codephreak agenda: to create AUTOMINDx autonomous deployment<br />

default model <a href="https://huggingface.co/search/full-text?q=llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin">llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin</a><br />

# manual install miniconda<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
sudo ./Miniconda3-latest-Linux-x86_64.sh<br />
#reload the shell configuration settings change for your shell example is for bash
source ~/.bashrc<br />
conda create --name automind python=3.9.1<br /><br />
#replace with bash with your shell<br />
conda activate bash<br /><br />
#conda reference for env display and quit
conda env list<br/>
conda list<br/>
conda info package_name<br/>
conda deactivate<br />

# clone automind and install requirements<br />
git clone https://github.com/Professor-Codephreak/automind<br />
cd automind<br />
#install pip if you haven't already<br />
sudo apt install python3-pip<br />
#display version of pip installed<br />
pip3 --version<br />
#install automind requirements with pip<br />
pip install -r requirements.txt<br />

# uiux call downloads language model on first deployment<br />

python3 uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"

# same call to uiux.py RUNS model post model download<br />

```bash
python3 uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"
```<br />

# file structure<br />

model_name.txt in the models folder with your model will autoread. the above call to uiux.py over-rides the call to model_name.txt<br />
models folder = models<br />
memory folder = memory<br /><br />

-----------------------------------
<br />
# troubleshooting<br />
<a href="https://github.com/ggerganov/llama.cpp">llamacpp source</a> build dependencies include<br />
  sudo apt-get install build-essential cmake gcc g++ git python3-dev python3-pip libstdc++6 make pkg-config<br />
# git and wget<br  />
  sudo apt-get install git wget</br>
# manual llamacpp pip install and uninstall<br />
pip uninstall llama-cpp-python<br />
pip install llama-cpp-python<br />
# On Ubuntu 22.04.6 automind.install works with cmake version 3.27.2<br />
cmake --version<br />
# On Ubuntu 22.04.6 automind.install works with gcc (Ubuntu 11.4.0-1ubuntu1`22.04) 11.4.0<br />
gcc --version</br />
# config gcc alternatives<br />
sudo update-alternatives --config gcc<br />
# install pip3<br />
sudo apt-get install python3-pip<br />
pip3 --version<br /><br />
# diagnostics<br />
sudo apt-get install hardinfo htop nvtop<br />





## [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)

To install right click "Save link as ..." [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install) chmod +x automind.install && automind.install

details and verbose procedure
1. Right-click the following link: [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)
2. Choose "Save link as..." or "Download linked file" from the context menu.
3. Select a location on your computer to save the file.
4. from the terminal
5. chmod +x automind.install && ./automind.install

# rewrite of basic manual installd<br />
sudo apt-get install build-essential cmake gcc g++ git python3-dev python3-pip libstdc++6 make pkg-config<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
sudo ./Miniconda3-latest-Linux-x86_64.sh<br />
source ~/.bashrc<br />
conda create --name automind python=3.9.1<br />
conda init<br />
source ~/.bashrc<br />
conda activate bash<br />
git clone https://github.com/Professor-Codephreak/automind<br />
cd automind<br />
#install pip if you haven't already<br />
sudo apt install python3-pip<br />
#display version of pip installed<br />
pip3 --version<br />
#install automind requirements with pip<br />
pip install -r requirements.txt<br />
-------------------------------------
<br />
# RUN codephreak<br />

python3 uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"

  

