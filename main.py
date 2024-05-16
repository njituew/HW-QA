from src import cabinet_client
from flask import Flask
from jinja2 import Template
from pathlib import Path
import config

app = Flask(__name__, static_url_path="", static_folder="")

PROJECTS_TEMPLATE = str(Path("templates/projects.html"))

@app.route("/user_projects/<email>")
def get_projects_html_by_student_email(email):
    with open(PROJECTS_TEMPLATE) as f:
        return Template(f.read()).render(
            projects_names=cabinet_client.get_projects_names_by_student_email(email),
            student_email=email
        )

@app.route("/api/user_projects/<student_email>", methods=["POST"])
def get_projects_names_by_student_email(student_email):
    return cabinet_client.get_projects_names_by_student_email(student_email)


if __name__ == "__main__":
    app.run(config.HOST, config.PORT, debug=True)
