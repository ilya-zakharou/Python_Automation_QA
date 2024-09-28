from pages.form_page import FormPage

class TestFormPage:

    def test_form(self,driver):
        form_page = FormPage(driver,'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        assert f'{person.first_name} {person.last_name}' == result[0], 'the first, last name has not been failed'
        assert person.email == result[1] , 'the email form has not been failed'
        print(person)  # увидеть какие рандомные данные сделал генератор в person
        print(result) #увидеть какие рандомные данные сделал генератор в итоге))