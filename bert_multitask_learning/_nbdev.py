# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"BaseParams": "00_params.ipynb",
         "CRFParams": "00_params.ipynb",
         "StaticBatchParams": "00_params.ipynb",
         "DynamicBatchSizeParams": "00_params.ipynb",
         "load_transformer_tokenizer": "01_utils.ipynb",
         "load_transformer_config": "01_utils.ipynb",
         "load_transformer_model": "01_utils.ipynb",
         "LabelEncoder": "01_utils.ipynb",
         "create_path": "01_utils.ipynb",
         "get_or_make_label_encoder": "01_utils.ipynb",
         "cluster_alphnum": "01_utils.ipynb",
         "filter_empty": "01_utils.ipynb",
         "infer_shape_and_type_from_dict": "01_utils.ipynb",
         "get_transformer_main_model": "01_utils.ipynb",
         "get_embedding_table_from_model": "01_utils.ipynb",
         "get_shape_list": "01_utils.ipynb",
         "gather_indexes": "01_utils.ipynb",
         "BOS_TOKEN": "02_special_tokens.ipynb",
         "EOS_TOKEN": "02_special_tokens.ipynb",
         "CLS_TOKEN": "02_special_tokens.ipynb",
         "SPACE_TOKEN": "02_special_tokens.ipynb",
         "UNK_TOKEN": "02_special_tokens.ipynb",
         "SPECIAL_TOKENS": "02_special_tokens.ipynb",
         "TRAIN": "02_special_tokens.ipynb",
         "EVAL": "02_special_tokens.ipynb",
         "PREDICT": "02_special_tokens.ipynb",
         "MODAL_LIST": "02_special_tokens.ipynb",
         "truncate_seq_pair": "03_bert_utils.ipynb",
         "punc_augument": "03_bert_utils.ipynb",
         "create_instances_from_document": "03_bert_utils.ipynb",
         "create_masked_lm_predictions": "03_bert_utils.ipynb",
         "MaskedLmInstance": "03_bert_utils.ipynb",
         "TrainingInstance": "03_bert_utils.ipynb",
         "seq_tag_label_handling": "04_create_bert_features.ipynb",
         "pad_wrapper": "04_create_bert_features.ipynb",
         "convert_labels_to_ids": "04_create_bert_features.ipynb",
         "create_bert_features": "04_create_bert_features.ipynb",
         "create_bert_pretraining": "04_create_bert_features.ipynb",
         "mask_inputs_for_mask_lm": "04_create_bert_features.ipynb",
         "create_multimodal_bert_features": "04_create_bert_features.ipynb",
         "create_bert_features_generator": "04_create_bert_features.ipynb",
         "create_multimodal_bert_features_generator": "04_create_bert_features.ipynb",
         "LOGGER": "14_run_bert_multitask.ipynb",
         "preprocessing_fn": "05_preproc_decorator.ipynb",
         "serialize_fn": "06_read_write_tfrecord.ipynb",
         "make_tfrecord": "06_read_write_tfrecord.ipynb",
         "make_feature_desc": "06_read_write_tfrecord.ipynb",
         "write_single_problem_chunk_tfrecord": "06_read_write_tfrecord.ipynb",
         "write_single_problem_gen_tfrecord": "06_read_write_tfrecord.ipynb",
         "write_tfrecord": "06_read_write_tfrecord.ipynb",
         "reshape_tensors_in_dataset": "06_read_write_tfrecord.ipynb",
         "add_loss_multiplier": "06_read_write_tfrecord.ipynb",
         "set_shape_for_dataset": "06_read_write_tfrecord.ipynb",
         "get_dummy_features": "06_read_write_tfrecord.ipynb",
         "add_dummy_features_to_dataset": "06_read_write_tfrecord.ipynb",
         "read_tfrecord": "06_read_write_tfrecord.ipynb",
         "element_length_func": "07_input_fn.ipynb",
         "train_eval_input_fn": "07_input_fn.ipynb",
         "predict_input_fn": "07_input_fn.ipynb",
         "process_line_msr_pku": "08_predefined_problems_cws.ipynb",
         "process_line_as_training": "08_predefined_problems_cws.ipynb",
         "process_line_cityu": "08_predefined_problems_cws.ipynb",
         "get_process_fn": "08_predefined_problems_cws.ipynb",
         "get_cws_fn": "08_predefined_problems_cws.ipynb",
         "get_as_cws_fn": "08_predefined_problems_cws.ipynb",
         "get_msr_cws_fn": "08_predefined_problems_cws.ipynb",
         "get_pku_cws_fn": "08_predefined_problems_cws.ipynb",
         "get_city_cws_fn": "08_predefined_problems_cws.ipynb",
         "gold_horse_ent_type_process_fn": "09_predefined_problems_ner.ipynb",
         "chinese_literature_ent_type_process_fn": "09_predefined_problems_ner.ipynb",
         "read_ner_data": "09_predefined_problems_ner.ipynb",
         "get_weibo_ner_fn": "09_predefined_problems_ner.ipynb",
         "gold_horse_segment_process_fn": "09_predefined_problems_ner.ipynb",
         "get_weibo_cws_fn": "09_predefined_problems_ner.ipynb",
         "read_bosonnlp_data": "09_predefined_problems_ner.ipynb",
         "read_msra": "09_predefined_problems_ner.ipynb",
         "get_msra_ner_fn": "09_predefined_problems_ner.ipynb",
         "get_boson_ner_fn": "09_predefined_problems_ner.ipynb",
         "NER_TYPE": "09_predefined_problems_ner.ipynb",
         "get_weibo_fake_cls_fn": "10_predefined_problems_test.ipynb",
         "get_weibo_fake_ner_fn": "10_predefined_problems_test.ipynb",
         "get_weibo_pretrain_fn": "10_predefined_problems_test.ipynb",
         "get_weibo_fake_multi_cls_fn": "10_predefined_problems_test.ipynb",
         "get_weibo_masklm": "10_predefined_problems_test.ipynb",
         "MultiModalBertModel": "11_modeling.ipynb",
         "empty_tensor_handling_loss": "12_top.ipynb",
         "nan_loss_handling": "12_top.ipynb",
         "create_dummy_if_empty": "12_top.ipynb",
         "BaseTop": "12_top.ipynb",
         "SequenceLabel": "12_top.ipynb",
         "Classification": "12_top.ipynb",
         "PreTrain": "12_top.ipynb",
         "Seq2Seq": "12_top.ipynb",
         "MultiLabelClassification": "12_top.ipynb",
         "MaskLM": "12_top.ipynb",
         "variable_summaries": "13_model_fn.ipynb",
         "filter_loss": "13_model_fn.ipynb",
         "BertMultiTaskBody": "13_model_fn.ipynb",
         "BertMultiTaskTop": "13_model_fn.ipynb",
         "BertMultiTask": "13_model_fn.ipynb",
         "LOGGER.propagate": "14_run_bert_multitask.ipynb",
         "create_keras_model": "14_run_bert_multitask.ipynb",
         "get_params_ready": "14_run_bert_multitask.ipynb",
         "train_bert_multitask": "14_run_bert_multitask.ipynb",
         "trim_checkpoint_for_prediction": "14_run_bert_multitask.ipynb",
         "eval_bert_multitask": "14_run_bert_multitask.ipynb",
         "predict_bert_multitask": "14_run_bert_multitask.ipynb",
         "TestBase": "99_test_base.ipynb"}

modules = ["params.py",
           "utils.py",
           "special_tokens.py",
           "bert_preprocessing/bert_utils.py",
           "bert_preprocessing/create_bert_features.py",
           "preproc_decorator.py",
           "read_write_tfrecord.py",
           "input_fn.py",
           "predefined_problems/cws_data.py",
           "predefined_problems/ner_data.py",
           "predefined_problems/test_data.py",
           "modeling.py",
           "top.py",
           "model_fn.py",
           "run_bert_multitask.py",
           "test_base.py"]

doc_url = "https://JayYip.github.io/bert_multitask_learning/"

git_url = "https://github.com/JayYip/bert_multitask_learning/tree/master/"

def custom_doc_links(name): return None
