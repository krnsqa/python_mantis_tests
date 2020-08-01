from data.project import testdata
import pytest



@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects, key=lambda project: project.name)