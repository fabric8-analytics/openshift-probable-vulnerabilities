# -*- coding: utf-8 -*-
"""This file contains the constants for interaction with AWS/Minio."""

import os

# Please make sure you have your AWS envt variables setup
AWS_S3_REGION = os.environ.get("AWS_S3_REGION", "ap-south-1")
AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
S3_BUCKET_NAME_MODEL = os.environ.get("AWS_BUCKET_NAME_MODEL",
                                      "avgupta-dev-gokube-triage")
S3_BUCKET_NAME_INFERENCE = os.environ.get("AWS_BUCKET_NAME_INFERENCE",
                                          "avgupta-dev-gokube-triage")

# Please set the following to point to your BQ auth credentials JSON
BIGQUERY_CREDENTIALS_FILEPATH = os.environ.get(
    "BIGQUERY_CREDENTIALS_FILEPATH", "../../auth/bq_key.json"
)

GOKUBE_REPO_LIST = os.environ.get("GOKUBE_REPO_LIST",
                                  "/utils/data_assets/golang-repo-list.txt")
KNATIVE_REPO_LIST = os.environ.get("KNATIVE_REPO_LIST",
                                   "/utils/data_assets/knative-repo-list.txt")
KUBEVIRT_REPO_LIST = os.environ.get(
    "KUBEVIRT_REPO_LIST", "/utils/data_assets/kubevirt-repo-list.txt"
)

P1GRU_SEC_MODEL_TOKENIZER_PATH = os.environ.get(
    "P1GRU_SEC_MODEL_TOKENIZER_PATH",
    "/model_assets/gokube-phase1-jun19/embeddings/security_tokenizer_word2idx_fulldata.pkl",  # noqa
)
P1GRU_SEC_MODEL_WEIGHTS_PATH = os.environ.get(
    "P1GRU_SEC_MODEL_WEIGHTS_PATH",
    "/model_assets/gokube-phase1-jun19/saved_models/security_model_train99-jun19_weights.h5",  # noqa
)

P1GRU_CVE_MODEL_TOKENIZER_PATH = os.environ.get(
    "P1GRU_CVE_MODEL_TOKENIZER_PATH",
    "/model_assets/gokube-phase1-jun19/embeddings/cve_tokenizer_word2idx_fulldata.pkl",  # noqa
)
P1GRU_CVE_MODEL_WEIGHTS_PATH = os.environ.get(
    "P1GRU_CVE_MODEL_WEIGHTS_PATH",
    "/model_assets/gokube-phase1-jun19/saved_models/cve_model_train99-jun19_weights.h5",  # noqa
)

BASE_BERT_UNCASED_PATH = os.environ.get(
    "BASE_BERT_UNCASED_PATH",
    "/model_assets/gokube-phase2/base_bert_tfhub_models/bert_uncased_L12_H768_A12",  # noqa
)
P2BERT_CVE_MODEL_WEIGHTS_PATH = os.environ.get(
    "P2BERT_CVE_MODEL_WEIGHTS_PATH",
    "/model_assets/gokube-phase2/saved_models/bert_cve75_weights-ep:02-trn_loss:0.172-trn_acc:0.957-val_loss:0.164-val_acc:0.978.h5",  # noqa
)

P2_PYTORCH_CVE_BERT_CLASSIFIER_PATH = os.environ.get(
    "P2_PYTORCH_CVE_BERT_CLASSIFIER_PATH",
    "/model_assets/gokube-phase2/pytorch-cve-warmup-2020_05_14_07_41_38/",
)

S3_MODEL_REFRESH = os.environ.get("S3_MODEL_REFRESH", "True")

# TODO: Use this constant later to not download everything to disk,
# leave it for now disk is not a problem.
MODEL_ASSETS = {
    "sec_model": [
        P1GRU_SEC_MODEL_TOKENIZER_PATH.lstrip("/"),
        P1GRU_SEC_MODEL_WEIGHTS_PATH.lstrip("/"),
    ],
    "gru": [P1GRU_CVE_MODEL_TOKENIZER_PATH.lstrip("/"),
            P1GRU_CVE_MODEL_WEIGHTS_PATH.lstrip("/")],
    "bert": [P2BERT_CVE_MODEL_WEIGHTS_PATH.lstrip("/"),
             BASE_BERT_UNCASED_PATH.lstrip("/")],
    "bert_torch": [P2_PYTORCH_CVE_BERT_CLASSIFIER_PATH.lstrip("/")],
}

INFERENCE_DROP_DESCRIPTIONS = os.environ.get("INFERENCE_DROP_DESCRIPTIONS",
                                             "True")
