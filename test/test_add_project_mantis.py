from model.project import Project


def test_add_project(app, json_project):
    app.session.login("administrator", "root")
    app.project.create_new_project(json_project)
