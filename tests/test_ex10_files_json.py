import json

from tests.utils import load

ex = load("stage2_advanced.ex10_files_json")


def test_write_and_read_lines(tmp_path):
    path = tmp_path / "a.txt"
    ex.write_lines(path, ["第一行", "second", "", "  third  "])
    assert path.read_text(encoding="utf-8") == "第一行\nsecond\n\n  third  \n"
    assert ex.read_lines(path) == ["第一行", "second", "third"]


def test_count_words(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("hello world\n  python   is\tfun\n", encoding="utf-8")
    assert ex.count_words(path) == 5


def test_append_log(tmp_path):
    path = tmp_path / "app.log"
    ex.append_log(path, "start")
    ex.append_log(path, "stop")
    assert path.read_text(encoding="utf-8") == "[LOG] start\n[LOG] stop\n"


def test_save_json(tmp_path):
    path = tmp_path / "nested" / "dir" / "data.json"
    data = {"name": "张三", "tags": ["a", "b"]}
    ex.save_json(path, data)
    text = path.read_text(encoding="utf-8")
    assert "张三" in text, "中文不应被转义，试试 ensure_ascii=False"
    assert '\n  "name"' in text, "需要 indent=2"
    assert json.loads(text) == data


def test_load_json(tmp_path):
    path = tmp_path / "d.json"
    path.write_text('{"a": [1, 2]}', encoding="utf-8")
    assert ex.load_json(path) == {"a": [1, 2]}
    assert ex.load_json(tmp_path / "missing.json") is None
    assert ex.load_json(tmp_path / "missing.json", default={}) == {}


def test_list_files(tmp_path):
    for name in ["b.md", "a.md", "c.txt"]:
        (tmp_path / name).write_text("x", encoding="utf-8")
    (tmp_path / "sub.md").mkdir()  # 目录不算
    assert ex.list_files(tmp_path, ".md") == ["a.md", "b.md"]
    assert ex.list_files(tmp_path, ".csv") == []


def test_update_json_counter(tmp_path):
    path = tmp_path / "counter.json"
    assert ex.update_json_counter(path, "home") == 1
    assert ex.update_json_counter(path, "home") == 2
    assert ex.update_json_counter(path, "about") == 1
    assert json.loads(path.read_text(encoding="utf-8")) == {"home": 2, "about": 1}
