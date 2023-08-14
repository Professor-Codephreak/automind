#!/bin/bash
# Manjaro test for automind
# automind (c) 2023 codephreak MIT license
# checks for conda and installs or updates conda
# actives automind conda environment
# clones automind
# installs automind with default model llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin
# launches boilerplate Gradio instruction response and expose API to localhost and globalhost
# Professor Codephreak is ...

# Add Script Directories to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

#sudo apt-get update
#sudo apt-get upgrade -y

# Check if Miniconda is already installed
if ! command -v conda &> /dev/null; then
    # Download and install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    sudo ./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
    echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    # Change ownership of the miniconda3 directory to the user
    sudo chown -R $USER:$USER $HOME/miniconda3
else
    echo "Miniconda is already installed. Updating Conda..."
    conda update -y conda
fi

source ~/.bashrc

# show details of the conda install
conda --version

# Create and activate the 'automind' conda environment
conda create --name automind python=3.9.1 -y
source ~/.bashrc
conda init zsh
source ~/.bashrc
conda activate automind
conda env list

# Install gradio and psutil
pip install gradio psutil fire

# Clone the 'automind' repository and install its requirements
git clone https://github.com/Professor-Codephreak/automind
cd automind
pip install --upgrade pip
pip --version
pip install -r requirements.txt

# Run UIUX
python uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"

#README
#two terminal inputs for deployment make automind exectuable and open with bash
#chmod +x automind.sh
#./automind.sh