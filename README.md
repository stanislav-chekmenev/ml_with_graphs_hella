![alt-text](https://github.com/stanislav-chekmenev/ml_with_graphs_hella/blob/main/assets/graph.jpg)

# Machine learning with graphs for Hella

- Connect to your desktop linux machine via ssh.
- Clone the repo
```bash
proxy git clone https://github.com/stanislav-chekmenev/ml_with_graphs_hella
```
- Install virtualenv inside the repo

```bash
cd ml_with_graphs_hella
sudo apt install virtualenv python3.8-venv
python3.8 -m venv venv
source venv/bin/activate
```
- Install requirements.txt
```bash
pip install -r requirements.txt
```
- Install Pytorch Geometric
1. Find out your torch version by running it in python console:
```python
import torch
print(torch.__version__)
```
2. Install PyG
```bash
export TORCH=your_torch_version
proxy pip install -q torch-scatter -f https://data.pyg.org/whl/torch-${TORCH}.html
proxy pip install -q torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}.html
proxy pip install -q git+https://github.com/pyg-team/pytorch_geometric.git
```
- Start jupyter-lab
```bash
jupyter-lab &
```
- Configure an ssh tunneling to your windows machine. JupyterLab is running on 127.0.0.1:8888 and it also prints a token ID which you'll be asked to provide on the first login.
