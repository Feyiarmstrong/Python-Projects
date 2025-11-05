import os
import requests
from dotenv import load_dotenv

load_dotenv()

class JiraFetcher:
    def __init__(self):
        self.email = os.getenv("JIRA_EMAIL")
        self.api_token = os.getenv("JIRA_TOKEN")
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.project_key = os.getenv("JIRA_PROJECT_KEY")
        self.auth = (self.email, self.api_token)
        self.headers = {"Accept": "application/json"}
        self.service_desk_id = None

    def connect(self):
        url = f"{self.base_url}/rest/servicedeskapi/servicedesk"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        for sd in response.json().get("values", []):
            if sd["projectKey"] == self.project_key:
                self.service_desk_id = sd["id"]
                print(f"Connected. Service Desk ID: {self.service_desk_id}")
                return
        print(f"No Service Desk found for project {self.project_key}")

    def fetch_requests(self, max_results=10):
        if not self.service_desk_id:
            print("Service Desk ID not found. Connect first.")
            return

        url = f"{self.base_url}/rest/servicedeskapi/request?serviceDeskId={self.service_desk_id}&start=0&limit={max_results}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        requests_data = response.json().get("values", [])
        if not requests_data:
            print("No requests found.")
            return

        print("\nLatest Requests:\n")
        for req in requests_data:
            key = req.get("issueKey")
            summary = req.get("summary")
            status = req.get("currentStatus", {}).get("status")
            jira_link = f"{self.base_url}/servicedesk/customer/portal/{self.service_desk_id}/{key}"
            # Clickable link in terminal
            clickable_link = f"\033]8;;{jira_link}\033\\Open Request\033]8;;\033\\"
            print(f"{key} | {summary} | Status: {status} | {clickable_link}")


if __name__ == "__main__":
    fetcher = JiraFetcher()
    fetcher.connect()
    fetcher.fetch_requests(max_results=5)