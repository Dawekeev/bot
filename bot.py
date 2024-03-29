from aiogram import executor,types,Bot,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datas import add_computer,add_user,get_computers,get_users,start_db
from  import admins_menu,reg_menu


token = ''
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot,storage=storage)

class RegState(StatesGroup):
    name = State()
    phone = State()

class CompState(StatesGroup):
    processor = State()
    videokarta = State()
    operativka = State()
    hdd = State()
    ssd = State()
    monitor = State()
    klava = State()
    mishka = State()
    naushnik = State()
    kovrik = State()

async def on_startup(_):
    await start_db()

admin_id = 5570471897
@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer(f'Salem admin xosh keldiniz!',reply_markup=admins_menu)
    else:
        await message.answer(f'Salem {message.from_user.first_name}',reply_markup=reg_menu)


@dp.message_handler(text='Users')
async def get_all_users(message:types.Message):
    users = await get_users()
    for i in users:
        await message.answer(i)






if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)