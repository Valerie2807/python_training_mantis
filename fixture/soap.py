from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
        except WebFault:
            return False
        return True

    def get_list_project(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        list = client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for el in list:
            id = el[0]
            name = el[1]
            description = el[7]
            project_list.append(
                Project(id=str(id), name=name, description=description))
        return project_list
