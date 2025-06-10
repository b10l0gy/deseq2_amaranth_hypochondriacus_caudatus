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
At first, put the counts data ``counts.csv`` and ``batches_meta_data.csv`` in ``./data/raw``.

## Preprocess data
Run the notebook ``preprocessing.ipynb`` to preprocess the data.
This should create two .csv files in ``data/preprocessed``

## Train models
Run the notebook ``train_model.ipynb`` to train the model/s.
The trained models are saved to ``data/models`` and can be loaded with ``load_model()`` from utils.

## PCA plot
To assess the data quality, we can apply principal component analysis and plot the resulting data.
At time of writing this the python version of Deseq2 did not provide the functionality of regularized log transformation. Therefore, we used the R package to generate a .csv containing this.
First run the R notebook ``R_dds.ipynb`` which is located in ``/R_code/``.
This should generate ``rlog_transformed_data.csv`` and ``rlog_transformed_data_wo_batch_effect.csv`` in ``/data/``.

Then run ``PCA_plot.ipynb`` to create the PCA plots.

## Differential Gene Analysis
Run ``analysis.ipynb`` which will create the two files ``statistical_results_hypochondriacus_caudatus_df.csv`` (before lfc shrinkage) and ``significant_DEG_results_hypochondriacus_caudatus_df.csv`` (after lfc shrinkage). In the notebook, you can find the difference of the number of DEG before and after lfc. This data is used by the next steps.

## Boxplots of the most DEGs
Run ``boxplot_most_expressed_DEGs.ipynb`` to create box plots for the most DEGs.

## GO enrichment analysis
Run ``go_enrichment_species.ipynb`` to conduct go enrichment analysis. This will create plots for 1) all DEGs, 2) DEGs of hypocondriacus, 3) DEGs of caudatus.

## Finish
Congratulations! You made it through the whole analysis! You can try to build up on this project to conduct DGE-analysis on other species or data.