#!/usr/bin/env python

import os
import subprocess
from typing import Any, Dict, Optional

import grpc_tools  # type: ignore
from grpc_tools import protoc  # type: ignore


def generate_deprecated_class_definition() -> None:
    """
    Generate a class definition listing the deprecated features.
    This is to allow static checks to ensure that proper field names are used.
    """
    from wandb_telemetry_pb2 import Deprecated  # type: ignore[import]
    deprecated_features = Deprecated.DESCRIPTOR.fields_by_name.keys()

    code: str = (
        "class Deprecated:\n"
        + "".join(
            [
                f'    {feature} = "{feature}"\n'
                for feature in deprecated_features
            ]
        )
    )
    with open("wandb/proto/wandb_deprecated.py", "w") as f:
        f.write(code)


def get_pip_package_version(package_name: str) -> str:
    out = subprocess.check_output(("pip", "show", package_name))
    info: Dict[str, Any] = dict(
        [line.split(": ", 2) for line in out.decode().rstrip("\n").split("\n")]  # type: ignore[misc]
    )
    return info["Version"]


def get_requirements_version(requirements_file_name: str, package_name: str) -> Optional[str]:
    with open(requirements_file_name) as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split("==")
            if tokens[0] == package_name:
                assert len(tokens) == 2, f"Package {package_name} not pinned"
                return tokens[1]
    return None


package: str = "grpcio-tools"
package_version = get_pip_package_version(package)
requirements_file: str = "../../requirements_build.txt"
requirements_version = get_requirements_version(requirements_file, package)
assert package_version == requirements_version, (
    f"Package {package} found={package_version} required={requirements_version}"
)

proto_root = os.path.join(os.path.dirname(grpc_tools.__file__), "_proto")
os.chdir("../..")
ret = protoc.main(
    (
        '',
        '-I', proto_root,
        '-I', '.',
        '--python_out=.',
        '--mypy_out=.',
        'wandb/proto/wandb_base.proto',
    )
)
assert not ret

ret = protoc.main(
    (
        '',
        '-I', proto_root,
        '-I', '.',
        '--python_out=.',
        '--mypy_out=.',
        'wandb/proto/wandb_internal.proto',
    )
)
assert not ret

ret = protoc.main(
    (
        '',
        '-I', proto_root,
        '-I', '.',
        '--python_out=.',
        '--mypy_out=.',
        'wandb/proto/wandb_telemetry.proto',
    )
)
assert not ret

ret = protoc.main(
    (
        '',
        '-I', proto_root,
        '-I', '.',
        '--python_out=.',
        '--grpc_python_out=.',
        '--mypy_out=.',
        '--mypy_grpc_out=.',
        'wandb/proto/wandb_server.proto',
    )
)
assert not ret

generate_deprecated_class_definition()
