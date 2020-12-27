from model.project import Project


def test_add_project(app, db, json_project):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_project = db.get_project_list()
    app.project.create_new_project(json_project)
    new_project = db.get_project_list()
    # assert len(old_project) == len(new_project)
    # assert len(old_project) + 1 == len(app.soap.get_list_project(username, password))
    assert len(app.soap.get_list_project(username, password)) == len(new_project)
