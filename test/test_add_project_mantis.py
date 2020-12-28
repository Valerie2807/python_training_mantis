from model.project import Project


def test_add_project(app, db, json_project):
    app.session.login(username="administrator", password="root")
    old_projects_list = app.soap.get_list_project(username="administrator", password="root")
    app.project.create(json_project)
    new_projects_list = app.soap.get_list_project(username="administrator", password="root")
    assert len(old_projects_list) == len(new_projects_list)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)


# def test_add_project(app, db, json_project):
#     username = "administrator"
#     password = "root"
#     app.session.login(username, password)
#     old_project = db.get_project_list()
#     app.project.create_new_project(json_project)
#     new_project = db.get_project_list()
#     # assert len(old_project) == len(new_project)
#     # assert len(old_project) + 1 == len(app.soap.get_list_project(username, password))
#     assert len(app.soap.get_list_project(username, password)) == len(new_project)
