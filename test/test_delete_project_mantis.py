import random


def test_delete_project(app, db):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
