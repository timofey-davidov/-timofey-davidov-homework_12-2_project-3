import pytest
from utils import dicts

# решаем через assert
assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
assert dicts.get_val({}, "vcs", "git") == "git"
assert dicts.get_val({}, "vcs", "bazzar") == "bazzar"

# решаем через фикстуры
@pytest.fixture
def data_1():
   return {"vcs": "mercurial"}

@pytest.fixture
def data_2():
   return {}

def test_get_val_1(data_1):
   assert dicts.get_val(data_1, "vcs") == "mercurial"

def test_get_val_2(data_1):
   assert dicts.get_val(data_1, "vcs", "git") == "mercurial"

def test_get_val_3(data_2):
   assert dicts.get_val(data_2, "vcs", "git") == "git"

def test_get_val_4(data_2):
   assert dicts.get_val(data_2, "vcs", "bazzar") == "bazzar"
