from data.project import testdata
import pytest



@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project, config):

    username = config['webadmin']['username']
    password = config['webadmin']['password']

    old_projects = app.soap.get_project_list(username, password, app.base_url)
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password, app.base_url)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects, key=lambda project: project.name)