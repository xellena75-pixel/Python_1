import requests


class YougileProjects:
    def __init__(self, url, token):
        self.url = f"{url}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload):
        return requests.post(self.url, json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.url}/{project_id}", headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(
            f"{self.url}/{project_id}", json=payload, headers=self.headers
        )
