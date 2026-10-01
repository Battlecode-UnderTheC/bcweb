import json

from bcweb import core


def test_devalue_stream_decodes_nodes():
    # One SvelteKit __data.json line: node data is a flattened devalue array.
    line = json.dumps({"type": "data", "nodes": [
        {"type": "data", "data": [{"team": 1}, {"id": 2, "name": 3}, 328, "UnderTheC"]}]})
    assert core._devalue_stream(line) == [{"team": {"id": 328, "name": "UnderTheC"}}]


def test_battle_id():
    assert core._battle_id("M727546") == core._battle_id("727546") == 727546
