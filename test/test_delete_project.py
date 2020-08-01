from model.project import Project
import random


def test_delete_any_group(app):
    if len(app.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_index(project)
    new_projects = app.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects