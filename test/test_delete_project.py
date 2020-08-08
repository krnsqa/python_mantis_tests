from model.project import Project
from random import randrange


def test_delete_any_project(app, config):

    username = config['webadmin']['username']
    password = config['webadmin']['password']

    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.soap.get_project_list(username, password, app.base_url)
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.soap.get_project_list(username, password, app.base_url)
    old_projects[index:index+1] = []     # == del old_projects[index]
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects, key=lambda project: project.name)