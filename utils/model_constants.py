# -*- coding: utf-8 -*-
"""Contains the constants that control model parameters.

Note: Please don't add keys directly here, refer to environment variables
"""
import os


# GRU
BATCH_SIZE_PROB_SEC_GRU = os.environ.get("BATCH_SIZE_PROB_SEC_GRU", 1024)
BATCH_SIZE_PROB_CVE_GRU = os.environ.get("BATCH_SIZE_PROB_GRU", 1024)

# BERT
BATCH_SIZE_PROB_SEC_BERT = os.environ.get("BATCH_SIZE_PROB_SEC_BERT", 32)
BATCH_SIZE_PROB_CVE_BERT = os.environ.get("BATCH_SIZE_PROB_CVE_BERT", 32)

# Transformers-pytorch-bert
TOKENIZER_CONVERT_LOWER_CASE = True
TASK_NAME = "sst-2"
MAX_SEQ_LENGTH = 512
GUID_PREFIX_INFERENCE = "dev"
BATCH_SIZE_PROB_CVE_BERT_TORCH = 64
BERT_CVE_PROB_THRESHOLD_LEGACY = 0.5
GRU_SEC_MODEL_PROB_THRESHOLD = 0.4
