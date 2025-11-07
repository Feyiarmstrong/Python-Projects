import os
import requests
from dotenv import load_dotenv
from logger import log_info, log_error  # <-- Import logger

load_dotenv()

class JiraConnector:
    def __init__(self):  # corrected from init
        self.email = os.getenv("JIRA_EMAIL")
        self.api_token = os.getenv("JIRA_TOKEN")
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.project_key = os.getenv("JIRA_PROJECT_KEY")
        self.auth = (self.email, self.api_token)
        self.headers = {"Accept": "application/json"}
        self.service_desk_id = None
        self.request_types = []

    def connect(self):
        try:
            self.service_desk_id = self.get_service_desk_id()
            if not self.service_desk_id:
                raise ValueError(f"No Service Desk found for project {self.project_key}")
            log_info(f"Connected to Jira Service Desk. ID: {self.service_desk_id}")
            self.request_types = self.get_request_types()
            log_info(f"Found {len(self.request_types)} request types.")
        except Exception as e:
            log_error(f"Failed to connect to Jira: {e}")
            print(f"Failed to connect: {e}")

    def get_service_desk_id(self):
        try:
            url = f"{self.base_url}/rest/servicedeskapi/servicedesk"
            response = requests.get(url, headers=self.headers, auth=self.auth)
            response.raise_for_status()
            for sd in response.json().get("values", []):
                if sd["projectKey"] == self.project_key:
                    return sd["id"]
            return None
        except Exception as e:
            log_error(f"Error fetching service desk ID: {e}")
            return None

    def get_request_types(self):
        try:
            url = f"{self.base_url}/rest/servicedeskapi/servicedesk/{self.service_desk_id}/requesttype"
            response = requests.get(url, headers=self.headers, auth=self.auth)
            response.raise_for_status()
            return response.json().get("values", [])
        except Exception as e:
            log_error(f"Error fetching request types: {e}")
            return []

    def create_request(self, summary, description, request_type_name):
        try:
            # Find the request type ID based on its name
            request_type_id = None
            for rt in self.request_types:
                if rt["name"] == request_type_name:
                    request_type_id = rt["id"]
                    break

            if not request_type_id:
                log_error(f"No request type named '{request_type_name}' found.")
                print(f"No request type named '{request_type_name}' found.")
                return None

            # Prepare payload for creating the ticket
            payload = {
                "serviceDeskId": self.service_desk_id,
                "requestTypeId": request_type_id,
                "requestFieldValues": {
                    "summary": summary,
                    "description": description
                }
            }

            url = f"{self.base_url}/rest/servicedeskapi/request"
            response = requests.post(url, json=payload, headers=self.headers, auth=self.auth)

            if response.status_code == 201:
                data = response.json()
                issue_key = data["issueKey"]
                log_info(f"Request created successfully! Key: {issue_key} | Summary: {summary}")
                print("Request created successfully!")
                print(f"Summary: {summary}")
                print(f"Request Key: {issue_key}")
                print(f"View it here: {self.base_url}/servicedesk/customer/portal/{self.service_desk_id}/{issue_key}")
                return issue_key  # Return the created ticket key
            else:
                log_error(f"Failed to create request: {response.status_code} - {response.text}")
                print(f"Failed to create request: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            log_error(f"Error creating Jira request: {e}")
            print(f"Error creating Jira request: {e}")
            return None


if __name__ == "__main__":  # Run this file directly to test
    connector = JiraConnector()
    connector.connect()

    request_type_name = "Submit a request or incident"
    connector.create_request(
        summary="New Request from Python",
        description="This request is created dynamically using the REST API.",
        request_type_name=request_type_name
    )