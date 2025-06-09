# deseq2_amaranth
This repo contains code concerning differential expression analysis (DEA) with bulk RNA-seq data for the amaranth species hypocondriacus and cadautus.

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/b10l0gy/deseq2_amaranth_hypochondriacus_caudatus
cd deseq2_amaranth_hypochondriacus_caudatus
```

### 2. Install Poetry (if not already installed)
This project is based on poetry.
First, install poetry following the documentation (provided by https://python-poetry.org/docs/)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

> Or see: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

### 3. Install Dependencies

```bash
poetry install
```

### 4. Activate the Virtual Environment

```bash
poetry shell
```

### 5. Install Jupyter Kernel for the Project

```bash
python -m ipykernel install --user --name deseq2-amaranth --display-name "Deseq2 Amaranth"
```

## Add Raw Data
At first, put the counts data in ``./data/raw``.
