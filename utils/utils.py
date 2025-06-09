import os
import pandas as pd
import pickle as pkl
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pathlib import Path

def get_root_path() -> Path:
    """
    Get the root path of the project directory.

    Returns:
        Path: The parent directory of the script file.
    """
    return Path(__file__).resolve().parent.parent

def find_file(filename: str, search_dir: str) -> str | None:
    """
    Recursively search for a file in a directory.

    Args:
        filename (str): Name of the file to search for.
        search_dir (str): Directory path to start searching.

    Returns:
        str | None: Full path to the file if found, else None.
    """
    for root, _, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

def save_df(df: pd.DataFrame, filename: str):
    """
    Save a pandas DataFrame to a CSV file in the data directory.

    Args:
        df (pd.DataFrame): DataFrame to save.
        filename (str): Name of the output file.

    Returns:
        None
    """
    return df.to_csv(os.path.join('../data/', filename))

def load_df(filename: str):
    """
    Load a pandas DataFrame from a CSV file located in the data directory.

    Args:
        filename (str): Name of the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame with index column set.
    """
    file_path = find_file(filename, os.path.join(get_root_path(), 'data'))
    return pd.read_csv(file_path, index_col=0)

def save_model(model, design_factors: list):
    """
    Save a trained model to a pickle file, named according to design factors.

    Args:
        model: Trained model object (DeseqDataSet).
        design_factors (list): List of design factor strings used in model.

    Returns:
        None
    """
    design_factors_string = ''
    for factor in design_factors:
        design_factors_string += '_' + factor
    with open(f'../models/dds{design_factors_string}.pkl', "wb") as f:
        pkl.dump(model, f)

def load_model(design_factors: list):
    """
    Load a trained model from a pickle file based on design factors.

    Args:
        design_factors (list): List of design factor strings used in model.

    Returns:
        DeseqDataSet: Loaded model object.
    """
    design_factors_string = ''
    for factor in design_factors:
        design_factors_string += '_' + factor
    with open(f'../models/dds{design_factors_string}.pkl', "rb") as f:
        model = pkl.load(f)
    print(f'Successfully loaded model: dds{design_factors_string}')
    return model

def train_model(counts_df, design_df, design_factors: list):
    """
    Train a DESeq2 model with given count and metadata tables.

    Args:
        counts_df (pd.DataFrame): Raw counts table (genes x samples).
        design_df (pd.DataFrame): Metadata table (samples x conditions).
        design_factors (list): List of design factors to include.

    Returns:
        None
    """
    inference = DefaultInference(n_cpus=8)

    dds = DeseqDataSet(
        counts=counts_df,
        metadata=design_df,
        design_factors=design_factors,
        refit_cooks=True,
        inference=inference,
        n_cpus=4
        )
    
    dds.deseq2()

    # save model
    save_model(dds, design_factors)

def train_model_with_batch(counts_df, design_df, design_factors):
    """
    Train a DESeq2 model including batch information in design factors.

    Args:
        counts_df (pd.DataFrame): Raw counts table (genes x samples).
        design_df (pd.DataFrame): Metadata table (samples x conditions).
        design_factors (list): List of design factors including batch.

    Returns:
        None
    """
    inference = DefaultInference(n_cpus=8)

    dds = DeseqDataSet(
        counts=counts_df,
        metadata=design_df,
        design_factors=design_factors,
        refit_cooks=True,
        inference=inference,
        n_cpus=4
        )
    
    dds.deseq2()

    # save model
    save_model(dds, design_factors)