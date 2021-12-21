"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions
import wandb.proto.wandb_base_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TelemetryRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMPORTS_INIT_FIELD_NUMBER: builtins.int
    IMPORTS_FINISH_FIELD_NUMBER: builtins.int
    FEATURE_FIELD_NUMBER: builtins.int
    PYTHON_VERSION_FIELD_NUMBER: builtins.int
    CLI_VERSION_FIELD_NUMBER: builtins.int
    HUGGINGFACE_VERSION_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    python_version: typing.Text = ...
    cli_version: typing.Text = ...
    huggingface_version: typing.Text = ...

    @property
    def imports_init(self) -> global___Imports: ...

    @property
    def imports_finish(self) -> global___Imports: ...

    @property
    def feature(self) -> global___Feature: ...

    @property
    def env(self) -> global___Env: ...

    @property
    def label(self) -> global___Labels: ...

    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...

    def __init__(self,
        *,
        imports_init : typing.Optional[global___Imports] = ...,
        imports_finish : typing.Optional[global___Imports] = ...,
        feature : typing.Optional[global___Feature] = ...,
        python_version : typing.Text = ...,
        cli_version : typing.Text = ...,
        huggingface_version : typing.Text = ...,
        env : typing.Optional[global___Env] = ...,
        label : typing.Optional[global___Labels] = ...,
        _info : typing.Optional[wandb.proto.wandb_base_pb2._RecordInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_info",b"_info",u"env",b"env",u"feature",b"feature",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init",u"label",b"label"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_info",b"_info",u"cli_version",b"cli_version",u"env",b"env",u"feature",b"feature",u"huggingface_version",b"huggingface_version",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init",u"label",b"label",u"python_version",b"python_version"]) -> None: ...
global___TelemetryRecord = TelemetryRecord

class TelemetryResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___TelemetryResult = TelemetryResult

class Imports(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TORCH_FIELD_NUMBER: builtins.int
    KERAS_FIELD_NUMBER: builtins.int
    TENSORFLOW_FIELD_NUMBER: builtins.int
    FASTAI_FIELD_NUMBER: builtins.int
    SKLEARN_FIELD_NUMBER: builtins.int
    XGBOOST_FIELD_NUMBER: builtins.int
    CATBOOST_FIELD_NUMBER: builtins.int
    LIGHTGBM_FIELD_NUMBER: builtins.int
    PYTORCH_LIGHTNING_FIELD_NUMBER: builtins.int
    PYTORCH_IGNITE_FIELD_NUMBER: builtins.int
    TRANSFORMERS_HUGGINGFACE_FIELD_NUMBER: builtins.int
    JAX_FIELD_NUMBER: builtins.int
    METAFLOW_FIELD_NUMBER: builtins.int
    ALLENNLP_FIELD_NUMBER: builtins.int
    AUTOGLUON_FIELD_NUMBER: builtins.int
    AUTOKERAS_FIELD_NUMBER: builtins.int
    CATALYST_FIELD_NUMBER: builtins.int
    DEEPCHEM_FIELD_NUMBER: builtins.int
    DEEPCTR_FIELD_NUMBER: builtins.int
    torch: builtins.bool = ...
    keras: builtins.bool = ...
    tensorflow: builtins.bool = ...
    fastai: builtins.bool = ...
    sklearn: builtins.bool = ...
    xgboost: builtins.bool = ...
    catboost: builtins.bool = ...
    lightgbm: builtins.bool = ...
    pytorch_lightning: builtins.bool = ...
    pytorch_ignite: builtins.bool = ...
    transformers_huggingface: builtins.bool = ...
    jax: builtins.bool = ...
    metaflow: builtins.bool = ...
    allennlp: builtins.bool = ...
    autogluon: builtins.bool = ...
    autokeras: builtins.bool = ...
    catalyst: builtins.bool = ...
    deepchem: builtins.bool = ...
    deepctr: builtins.bool = ...

    def __init__(self,
        *,
        torch : builtins.bool = ...,
        keras : builtins.bool = ...,
        tensorflow : builtins.bool = ...,
        fastai : builtins.bool = ...,
        sklearn : builtins.bool = ...,
        xgboost : builtins.bool = ...,
        catboost : builtins.bool = ...,
        lightgbm : builtins.bool = ...,
        pytorch_lightning : builtins.bool = ...,
        pytorch_ignite : builtins.bool = ...,
        transformers_huggingface : builtins.bool = ...,
        jax : builtins.bool = ...,
        metaflow : builtins.bool = ...,
        allennlp : builtins.bool = ...,
        autogluon : builtins.bool = ...,
        autokeras : builtins.bool = ...,
        catalyst : builtins.bool = ...,
        deepchem : builtins.bool = ...,
        deepctr : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"allennlp",b"allennlp",u"autogluon",b"autogluon",u"autokeras",b"autokeras",u"catalyst",b"catalyst",u"catboost",b"catboost",u"deepchem",b"deepchem",u"deepctr",b"deepctr",u"fastai",b"fastai",u"jax",b"jax",u"keras",b"keras",u"lightgbm",b"lightgbm",u"metaflow",b"metaflow",u"pytorch_ignite",b"pytorch_ignite",u"pytorch_lightning",b"pytorch_lightning",u"sklearn",b"sklearn",u"tensorflow",b"tensorflow",u"torch",b"torch",u"transformers_huggingface",b"transformers_huggingface",u"xgboost",b"xgboost"]) -> None: ...
global___Imports = Imports

class Feature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WATCH_FIELD_NUMBER: builtins.int
    FINISH_FIELD_NUMBER: builtins.int
    SAVE_FIELD_NUMBER: builtins.int
    OFFLINE_FIELD_NUMBER: builtins.int
    RESUMED_FIELD_NUMBER: builtins.int
    GRPC_FIELD_NUMBER: builtins.int
    METRIC_FIELD_NUMBER: builtins.int
    KERAS_FIELD_NUMBER: builtins.int
    SAGEMAKER_FIELD_NUMBER: builtins.int
    ARTIFACT_INCREMENTAL_FIELD_NUMBER: builtins.int
    METAFLOW_FIELD_NUMBER: builtins.int
    PRODIGY_FIELD_NUMBER: builtins.int
    SET_INIT_NAME_FIELD_NUMBER: builtins.int
    SET_INIT_ID_FIELD_NUMBER: builtins.int
    SET_INIT_TAGS_FIELD_NUMBER: builtins.int
    SET_INIT_CONFIG_FIELD_NUMBER: builtins.int
    SET_RUN_NAME_FIELD_NUMBER: builtins.int
    SET_RUN_TAGS_FIELD_NUMBER: builtins.int
    SET_CONFIG_ITEM_FIELD_NUMBER: builtins.int
    LAUNCH_FIELD_NUMBER: builtins.int
    TORCH_PROFILER_TRACE_FIELD_NUMBER: builtins.int
    SB3_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    INIT_RETURN_RUN_FIELD_NUMBER: builtins.int
    LIGHTGBM_WANDB_CALLBACK_FIELD_NUMBER: builtins.int
    LIGHTGBM_LOG_SUMMARY_FIELD_NUMBER: builtins.int
    watch: builtins.bool = ...
    finish: builtins.bool = ...
    save: builtins.bool = ...
    offline: builtins.bool = ...
    resumed: builtins.bool = ...
    grpc: builtins.bool = ...
    metric: builtins.bool = ...
    keras: builtins.bool = ...
    sagemaker: builtins.bool = ...
    artifact_incremental: builtins.bool = ...
    metaflow: builtins.bool = ...
    prodigy: builtins.bool = ...
    set_init_name: builtins.bool = ...
    set_init_id: builtins.bool = ...
    set_init_tags: builtins.bool = ...
    set_init_config: builtins.bool = ...
    set_run_name: builtins.bool = ...
    set_run_tags: builtins.bool = ...
    set_config_item: builtins.bool = ...
    launch: builtins.bool = ...
    torch_profiler_trace: builtins.bool = ...
    sb3: builtins.bool = ...
    service: builtins.bool = ...
    init_return_run: builtins.bool = ...
    lightgbm_wandb_callback: builtins.bool = ...
    lightgbm_log_summary: builtins.bool = ...

    def __init__(self,
        *,
        watch : builtins.bool = ...,
        finish : builtins.bool = ...,
        save : builtins.bool = ...,
        offline : builtins.bool = ...,
        resumed : builtins.bool = ...,
        grpc : builtins.bool = ...,
        metric : builtins.bool = ...,
        keras : builtins.bool = ...,
        sagemaker : builtins.bool = ...,
        artifact_incremental : builtins.bool = ...,
        metaflow : builtins.bool = ...,
        prodigy : builtins.bool = ...,
        set_init_name : builtins.bool = ...,
        set_init_id : builtins.bool = ...,
        set_init_tags : builtins.bool = ...,
        set_init_config : builtins.bool = ...,
        set_run_name : builtins.bool = ...,
        set_run_tags : builtins.bool = ...,
        set_config_item : builtins.bool = ...,
        launch : builtins.bool = ...,
        torch_profiler_trace : builtins.bool = ...,
        sb3 : builtins.bool = ...,
        service : builtins.bool = ...,
        init_return_run : builtins.bool = ...,
        lightgbm_wandb_callback : builtins.bool = ...,
        lightgbm_log_summary : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"artifact_incremental",b"artifact_incremental",u"finish",b"finish",u"grpc",b"grpc",u"init_return_run",b"init_return_run",u"keras",b"keras",u"launch",b"launch",u"lightgbm_log_summary",b"lightgbm_log_summary",u"lightgbm_wandb_callback",b"lightgbm_wandb_callback",u"metaflow",b"metaflow",u"metric",b"metric",u"offline",b"offline",u"prodigy",b"prodigy",u"resumed",b"resumed",u"sagemaker",b"sagemaker",u"save",b"save",u"sb3",b"sb3",u"service",b"service",u"set_config_item",b"set_config_item",u"set_init_config",b"set_init_config",u"set_init_id",b"set_init_id",u"set_init_name",b"set_init_name",u"set_init_tags",b"set_init_tags",u"set_run_name",b"set_run_name",u"set_run_tags",b"set_run_tags",u"torch_profiler_trace",b"torch_profiler_trace",u"watch",b"watch"]) -> None: ...
global___Feature = Feature

class Env(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JUPYTER_FIELD_NUMBER: builtins.int
    KAGGLE_FIELD_NUMBER: builtins.int
    WINDOWS_FIELD_NUMBER: builtins.int
    M1_GPU_FIELD_NUMBER: builtins.int
    START_SPAWN_FIELD_NUMBER: builtins.int
    START_FORK_FIELD_NUMBER: builtins.int
    START_FORKSERVER_FIELD_NUMBER: builtins.int
    START_THREAD_FIELD_NUMBER: builtins.int
    MAYBE_MP_FIELD_NUMBER: builtins.int
    jupyter: builtins.bool = ...
    kaggle: builtins.bool = ...
    windows: builtins.bool = ...
    m1_gpu: builtins.bool = ...
    start_spawn: builtins.bool = ...
    start_fork: builtins.bool = ...
    start_forkserver: builtins.bool = ...
    start_thread: builtins.bool = ...
    maybe_mp: builtins.bool = ...

    def __init__(self,
        *,
        jupyter : builtins.bool = ...,
        kaggle : builtins.bool = ...,
        windows : builtins.bool = ...,
        m1_gpu : builtins.bool = ...,
        start_spawn : builtins.bool = ...,
        start_fork : builtins.bool = ...,
        start_forkserver : builtins.bool = ...,
        start_thread : builtins.bool = ...,
        maybe_mp : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"jupyter",b"jupyter",u"kaggle",b"kaggle",u"m1_gpu",b"m1_gpu",u"maybe_mp",b"maybe_mp",u"start_fork",b"start_fork",u"start_forkserver",b"start_forkserver",u"start_spawn",b"start_spawn",u"start_thread",b"start_thread",u"windows",b"windows"]) -> None: ...
global___Env = Env

class Labels(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CODE_STRING_FIELD_NUMBER: builtins.int
    REPO_STRING_FIELD_NUMBER: builtins.int
    CODE_VERSION_FIELD_NUMBER: builtins.int
    code_string: typing.Text = ...
    repo_string: typing.Text = ...
    code_version: typing.Text = ...

    def __init__(self,
        *,
        code_string : typing.Text = ...,
        repo_string : typing.Text = ...,
        code_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"code_string",b"code_string",u"code_version",b"code_version",u"repo_string",b"repo_string"]) -> None: ...
global___Labels = Labels
