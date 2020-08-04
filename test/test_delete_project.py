from model.project import Project
from random import randrange


def test_delete_any_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index+1] = []     # == del old_projects[index]
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects, key=lambda project: project.name)