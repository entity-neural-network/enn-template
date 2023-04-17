# ENN Template

Template for creating custom [Entity Gym](https://github.com/entity-neural-network/entity-gym) environments and training agents with [enn-trainer](https://github.com/entity-neural-network/enn-trainer).

## Installation

If using `pip` and GPU:

```
pip install enn-trainer
pip install torch==1.12.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
pip install --no-index torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cu113.html
```

If using `pip` and CPU:

```
pip install enn-trainer
pip install torch==1.12.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install --no-index torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cpu.html
```

If using `poetry` and GPU:

```
poetry install
poetry run pip install torch==1.12.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
poetry run pip --no-index install torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cu113.html
```

If using `poetry` and CPU:

```
poetry install
poetry run pip install torch==1.12.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
poetry run pip --no-index install torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cpu.html
```

## Usage

Run environment interactively in CLI:

```
python enn_template/env.py
```

Run training:

```
python enn_template/train.py
```

