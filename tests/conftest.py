import os
from pathlib import Path

import pytest
import toml

tests_location = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(params=Path(os.path.join(tests_location, "texts")).glob("*.toml"))
def test_text(request):
    yield toml.load(request.param)


@pytest.fixture
def test_text_file(test_text, tmp_path):
    tmp_file: Path = tmp_path / f"{test_text['meta']['title']}.txt"
    tmp_file.write_text(test_text["text"])
    yield tmp_file
    tmp_file.unlink()
