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


# Example loading automind using Ubuntu 22.04LTS<br />
Creates Professor Codephreak<br /><br />
Professor Codephreak is an expert in machine learning, computer science and computer programming<br />
codephreak agenda: to create AUTOMINDx autonomous deployment<br />

default model llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin<br />

# manual install miniconda<br />
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh<br />
chmod +x Miniconda3-latest-Linux-x86_64.sh<br />
sudo ./Miniconda3-latest-Linux-x86_64.sh<br />
#reload the shell configuration settings change for your shell example is for bash
source ~/.bashrc<br />
conda create --name automind python=3.9.1<br /><br />
#replace with your shell here<br />
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

# uiux download language model<br />
and run or run uiux.py if models folder is already populated<br />

python uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"<br />

model_name.txt in the models folder with your model will autoread. the above overwrites the call to model_name.txt<br />
models folder = models<br />
memory folder = memory<br /><br />

-----------------------------------

## [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)

To install right click "Save link as ..." [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install) chmod +x automind.install && automind.install

details and verbose procedure
1. Right-click the following link: [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)
2. Choose "Save link as..." or "Download linked file" from the context menu.
3. Select a location on your computer to save the file.
4. from the terminal
5. chmod +x automind.install && ./automind.install


---------------------------------

