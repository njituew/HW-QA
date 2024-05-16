import config
import requests

headers = {
    "X-Auth-Token": f"Bearer {config.CABINET_TOKEN}"
}

def get_student_id_by_email(email: str) -> int:
    response = requests.get(f"{config.CABINET_URL}/public-api/user/email/{email}", headers=headers, timeout=config.TIMEOUT)
    student_profile = response.json()
    return student_profile["data"]["userId"]

def get_student_projects_by_year_id(student_id, year_id):
    response = requests.get(f"{config.CABINET_URL}/public-api/student_statistics/{student_id}?studyYearId={year_id}", headers=headers, timeout=config.TIMEOUT)
    return response.json()["data"]["projects"]



def get_students_projects_by_id(student_id: int) -> list[int]:
    response = requests.get(f"{config.CABINET_URL}/public-api/student_profile/{student_id}", headers=headers, timeout=config.TIMEOUT)
    student_profile = response.json()["data"]
    years = student_profile[0]["years"]

    projects_by_names = {}
    for year in years[:-1]:
        projects_by_year = get_student_projects_by_year_id(student_id, year["id"])
        for project in projects_by_year:
            if project["name"] != "":
                projects_by_names[project["name"]] = project
    return projects_by_names

def get_projects_names_by_student_email(email: str):
    student_id = get_student_id_by_email(email)
    res = get_students_projects_by_id(student_id+1)
    return list(map(lambda key: res[key]["name"], res.keys()))
