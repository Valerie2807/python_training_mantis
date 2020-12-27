import random


def test_delete_project(app, db, json_project):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(json_project)
    app.project.open_project_page()
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
