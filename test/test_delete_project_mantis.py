import random


def test_dell_project(app, db, json_project):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(json_project)
    app.project.open_project_page()
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = db.get_project_list()
    # assert len(old_project) - 1 == len(new_project)
    # assert len(old_project) -1 == len(app.soap.get_list_project(username, password))
    assert len(app.soap.get_list_project(username, password)) == len(new_project)
