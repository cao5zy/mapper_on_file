from assertpy import assert_that
from codegenhelper import put_folder, put_file, remove
from mapper_on_files import map
from nose import with_setup

root = "./test"
map_file = "./test/map.mapper"

def setup_test_map():
    put_file("map.mapper", put_folder(root), '''
''')

def clear():
    remove(root)


@with_setup(setup_test_map, clear)
def test_map():
    data = {
        "title": "alan",
        "methods": [{"name": "all"}]
    }    
    assert_that(map(map_file, data)) \
        .contains_entry({"name": "alan"}) \
        .contains_entry({"methods": ["all"]})
