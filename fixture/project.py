from model.project import Project
import random


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def change_field_value(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)


    def fill_project_form(self, project):
        dw = self.app.dw
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def open_projects_page(self):
        dw = self.app.dw
        if not (dw.current_url.endswith("/manage_proj_page.php") and
                len(dw.find_elements_by_css_selector("input[value*='Create New Project'")) > 0):
            dw.find_element_by_link_text("Manage").click()
            dw.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        dw = self.app.dw
        self.open_projects_page()
        #add new project
        dw.find_element_by_css_selector(".width100 input[value='Create New Project'").click()
        self.fill_project_form(project)
        # submit project form creation
        dw.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None


    def count(self):
        dw = self.app.dw
        self.open_projects_page()
        return len(dw.find_elements_by_css_selector(".width100 tr[class*='row-'")[1:])


    project_cache = None


    def get_project_list(self):
        if self.project_cache is None:
            dw = self.app.dw
            self.open_projects_page()
            self.project_cache = []
            rows = dw.find_elements_by_css_selector(".width100 tr[class*='row-'")[1:]
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)


    def select_project_by_index(self, index):
        dw = self.app.dw
        (dw.find_elements_by_css_selector(".width100 tr[class*='row-']>td>a:nth-child(1)")[5:])[index].click()


    def delete_project_by_index(self, index):
        dw = self.app.dw
        self.open_projects_page()
        self.select_project_by_index(index)
        # submit deletion
        dw.find_element_by_css_selector("input[value='Delete Project']").click()
        dw.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None