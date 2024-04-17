import dataclasses


@dataclasses.dataclass
class User:
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str
    email: str
    birth_date: str
    birth_place: str
    passport_number: str
    passport_issue_date: str
    passport_issuer_code: str
    passport_issuer_title: str
    gender: str
    registration_address: str
    data_option_address: str
    inn: str


test_user = User(
    last_name='Тестова',
    first_name='Тест',
    middle_name ='Тестовна',
    phone_number='79999999999',
    email='invest.akbars.qa@gmail.com',
    birth_date='01 01 2000',
    birth_place='г. Казань',
    passport_number='0000 000000',
    passport_issue_date='01 01 2014',
    passport_issuer_code='000 000',
    passport_issuer_title='МВДпо РТ в г. Казань',
    gender='female',
    registration_address='г. Казань ул Декабристов 1а',
    data_option_address=':nth-child(1)',
    inn='000000000184',
)

bykova_user = User(
    last_name='Быкова',
    first_name='Сафия',
    middle_name ='Лия',
    phone_number='79999999999',
    email='invest.akbars.qa@gmail.com',
    birth_date='01 01 2000',
    birth_place='г. Казань',
    passport_number='0000 000000',
    passport_issue_date='01 01 2014',
    passport_issuer_code='000 000',
    passport_issuer_title='МВДпо РТ в г. Казань',
    gender='female',
    registration_address='г. Казань ул Декабристов 1а',
    data_option_address=':nth-child(1)',
    inn='000000000184',
)
