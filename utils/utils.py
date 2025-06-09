import os
import pandas as pd
import pickle as pkl
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference

def save_df(df: pd.DataFrame, filename: str):
    return df.to_csv(os.path.join('../data/', filename))

def load_df(filename: str):
    return pd.read_csv(os.path.join('../data/', filename), index_col=0)

def save_model(model, design_factors: list):
    design_factors_string = ''
    for factor in design_factors:
        design_factors_string += '_' + factor
    with open(f'../models/dds{design_factors_string}.pkl', "wb") as f:
        pkl.dump(model, f)

def load_model(design_factors: list):
    design_factors_string = ''
    for factor in design_factors:
        design_factors_string += '_' + factor
    with open(f'../models/dds{design_factors_string}.pkl', "rb") as f:
        model = pkl.load(f)
    print(f'Successfully loaded model: dds{design_factors_string}')
    return model

def train_model(counts_df, design_df, design_factors: list):
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