from contextlib import nullcontext as does_not_raise
from typing import ContextManager, Union

import pytest
import yaml
from jinja2.ext import Extension
from plumbum import local
from plumbum.cmd import git

from copier.cli import CopierApp
from copier.errors import UnsafeTemplateError
from copier.main import run_copy, run_update
from copier.types import AnyByStrDict

from .helpers import build_file_tree


class JinjaExtension(Extension):
    ...


# TODO: 