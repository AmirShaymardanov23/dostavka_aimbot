from aiogram.dispatcher.filters.state import State ,StatesGroup


#Процесс для регистрацции
class Registration(StatesGroup):
    get_name_state=State()
    get_phone_number_state=State()
    get_location_state=State()
    get_gender_state=State()


#процесс для выбора  товара
class GetProduct(StatesGroup):
    get_pr_name=State()
    get_pr_count=State()


#процессы при работе с крзиной
class Cart(StatesGroup):
   waiting_for_product=State()
   waiting_new_count= State()
#процессы при оформлении
class Order(StatesGroup):
    waiting_location= State()
    waiting_pay_type=State()
    waiting_accept_state=State()