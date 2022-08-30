from requests import delete
from accounts.models import User

from .models import Channel, Ivent, User_tg, Chat, TaskConnect, Mailing, Statistic

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage

from services.channels import add_admin, create_channel, change_channel, delete_channel, create_chat, send_message


def main(req, page=None):
    """Главноя страница со всеми меню"""
    if req.user.is_authenticated:        
        if page == 'channels':
            channels = Channel.objects.all()
            return render(req, 'work/main.html', {'page': page, 'channels': channels})

        elif page == 'users':
            users_tg = User_tg.objects.all()
            return render(req, 'work/main.html', {'page': page, 'users': users_tg})

        elif page == 'chats':
            channels = Chat.objects.all()
            return render(req, 'work/main.html', {'page': page, 'channels': channels})

        elif page == 'task':
            task = TaskConnect.objects.all()
            return render(req, 'work/main.html', {'page': page, 'tasks': task})

        elif page == 'mailing':
            mailings = Mailing.objects.all()
            return render(req, 'work/main.html', {'mailings': mailings, 'page': page})

        elif page == 'ivent':
            """Страница управления контентом"""
            ivents = Ivent.objects.all()
            return render(req, 'work/main.html', {'ivents': ivents, 'page': page})

        elif page == 'statistic':
            """Страница управления контентом"""
            stat = Statistic.objects.all()
            return render(req, 'work/main.html', {'statistic': stat, 'page': page})

        else:
            users = User.objects.all()
            return render(req, 'work/main.html', {'page': page, 'users': users})

    else:
        return redirect('login')


def create_staf(req):
    """Создание персонала"""
    messages = []
    if req.method == 'POST':
        user = User()
        data = req.POST.dict()
        user.name = data['name']
        user.phone = data['phone']
        user.username = data['phone']
        user.manage = True if data['manage'] == 'true' else False
        user.user_manage = True if data['user_manage'] == 'true' else False
        user.chat_manage = True if data['chat_manage'] == 'true' else False
        user.channel_manage = True if data['channel_manage'] == 'true' else False
        user.password = make_password(data['psswd'])
        user.save()
        return redirect('staf', user.id)

    return render(req, 'work/createstaf.html', {'messages': messages})


def staf(req, id=None):
    """Страница редактирования данных персонала"""
    messages = []
    if req.user.is_authenticated:
        user = User.objects.get(id=id)
        if user:
            if req.method == 'POST':
                data = req.POST.dict()

                if 'delete' in data:
                    user.delete()
                    return redirect('main', 'manage')

                user.name = data['name']
                user.phone = data['phone']
                user.manage = True if data['manage'] == 'true' else False
                user.user_manage = True if data['user_manage'] == 'true' else False
                user.chat_manage = True if data['chat_manage'] == 'true' else False
                user.channel_manage = True if data['channel_manage'] == 'true' else False
                user.save()
                messages.append('Изменения сохранены!')

            return render(req, 'work/staf.html', {'user': user, 'messages': messages})


def create_user(req):
    users = User_tg.objects.all()

    """Создание нового пользователя (телеграм)"""
    if req.user.is_authenticated == False:
        return  redirect('login')

    if req.method == 'POST':
        data = req.POST.dict()

        file = req.FILES['photo']
        file_name = default_storage.save(f'{data["phone"]}.{str(file.name).split(".")[-1]}', file)

        user_tg = User_tg()
        user_tg.phone = data['phone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '').replace('+', '')
        user_tg.name = data['name']
        user_tg.photo = f"../crm/media/{data['phone']}.{str(file.name).split('.')[-1]}"
        user_tg.about = data['about']
        user_tg.about_1 = data['about_1']
        user_tg.about_2 = data['about_2']
        user_tg.about_3 = data['about_3']
        user_tg.about_4 = data['about_4']
        usersuccess = []
        for us in users:
            usersuccess.append(us.phone)
            if us.phone != user_tg.phone:
                user_tg.save()
                usersuccess.append(user_tg.phone)
                return redirect('user', user_tg.id)
            else:
                return redirect('login')

    return render(req, 'work/createuser.html', {'users':users})


def user_page(req, id=None):
    """Страница пользователя"""
    messages = []
    if req.user.is_authenticated:
        user = User_tg.objects.get(id=id)
        # file = req.FILES['photo']
        
        if req.method == 'POST':
            data = req.POST.dict()
            print(data)
            print(req.FILES['photo'])
            print(req.FILES)
            # user.name = req.FILES['name']

            file = req.FILES['photo']
            # file = data['photo']
            file_name = default_storage.save(f'/root/crm/media/{user.phone}.{str(file.text).split(".")[-1]}', file)
            user.photo = f'/root/crm/media/{file_name}'

            user.about = data['about']
            user.about_1 = data['about_1']
            user.about_2 = data['about_2']
            user.about_3 = data['about_3']
            user.about_4 = data['about_4']
            

            if 'ban' in data:
                user.tg_id = f'{user.tg_id}_ban' if '_ban' not in user.tg_id else str(user.tg_id).replace('_ban', '')
                user.phone = f'{user.phone}_ban' if '_ban' not in user.phone else str(user.phone).replace('_ban', '')

            user.save()

            if 'delete' in data:
                user.delete()
                return redirect('main', 'users')

        if user:
            ban = '_ban' in user.tg_id
            return render(req, 'work/user.html', {'user': user, 'ban': ban, 'messages': messages})


def statistic(req, id=None):
    """Страница пользователя"""
    if req.user.is_authenticated:
        stat = Statistic.objects.get(id=id)
        # user = User_tg.objects.get(phone=stat.user_phone)

        if req.method == 'POST':
            data = req.POST.dict()
            # user.name = data['name']
            # user.save()

            if 'delete' in data:
                stat.delete()
                return redirect('main', 'statistic')

        if stat:
            return render(req, 'work/statistic.html', {'statistic': stat})
    return redirect('login')


def create_channel_view(req):
    """Создание канала"""
    if req.method == 'POST':
        data = req.POST.dict()
        channel = Channel()
        channel.name = data['name']
        channel.desc = data['desc']
        channel.link = data['username']
        channel.save()
        if create_channel(namechannel=data['name'], descrchannel=data['desc'], linkchannel=data['username'], id=channel.id):
            return redirect('channel', channel.id)
        else:
            channel.delete()
            return render(req, 'work/createchannel.html', {
                'messages': ['Канал с таким именем уже существует']
            })

    return render(req, 'work/createchannel.html')


def channel_view(req, id):
    print(id)
    """Просмотр и редактирование канала"""
    channel = Channel.objects.get(id=id)

    if req.method == 'POST':
        data = req.POST.dict()

        if 'delete' in data:
            channel.delete()
            delete_channel(channel.link)
            return redirect('main', 'channels')
        else:
            channel.name = data['name']
            channel.save()

            if 'add_admin' in data and data['add_admin']:
                add_admin(channel.tg_id, int(data['add_admin']))

            change_channel(data['name'], channel.link)
            return render(req, 'work/channel.html', {'channel': channel})
    else:
        return render(req, 'work/channel.html', {'channel': channel})


def create_chat_view(req):
    """Создание канала"""
    if req.method == 'POST':
        data = req.POST.dict()
        chat = Chat()
        chat.name = data['name']
        chat.save()

        users = data['username'].replace("@", '').replace(' ', '').split(',')
        create_chat(title=chat.name, users=users)
        return redirect('main', 'chats')

    return render(req, 'work/createchat.html')


def delete_chat(req, id=None):
    chat = Chat.objects.get(id=id)
    chat.delete()
    return redirect('main', 'chats')


def task_connect(req, id):
    task = TaskConnect.objects.get(id=id)
    photo = ''
    users = User_tg.objects.all()
    photo = task.photo_path

    if req.method == 'POST':
        data = req.POST
        user = User_tg.objects.get(phone=task.user_from)
        if task.user_to == '0':
            text_alone = 'Ваша заявка на изменение профиля не прошла модерацию, свяжитесь с поддержкой'
            text_success = 'Данные профиля обновлены по вашей заявке'
        else:
            text_alone = 'Вы отправляли заявку связаться с пользователем. К сожалению он не захотел связываться'
            text_success = f'Вы отправляли заявку связаться с пользователем. Вот его намер телефона \n{task.user_to}'
        try:
            if 'delete' in data:
                send_message(user.tg_id, text_alone)
                pass
            elif 'connect' in data:
                if photo:
                    user.photo = photo
                    user.save()
                send_message(user.tg_id, text_success)
        except:
            pass
        task.delete()
        return redirect('main', 'task')

    return render(req, 'work/task_connect.html', {'task': task, 'photo': photo if photo else '', 'users': users})


def add_ivent(req, id=None):
    """Создать мероприятие"""
    if req.method == 'POST':
        data = req.POST.dict()

        if 'delete' in data and id:
            ivent = Ivent.objects.get(id=id)
            ivent.delete()
            return redirect('content_page')
        if id:
            ivent = Ivent.objects.get(id=id)
            ivent.name = data['name'] if 'name' in data else ivent.name
            ivent.type_ivent = data['type_ivent'] if 'type_ivent' in data else ivent.type_ivent
            ivent.date = data['data'] if 'data' in data else ivent.date
            ivent.desc = data['desc'] if 'desc' in data else ivent.desc

            if 'photo' in req.FILES:
                file = req.FILES['photo']
                file_name = default_storage.save(f'{ivent.id}.{str(file.name).split(".")[-1]}', file)

                ivent.photo = f'../crm/media/{ivent.id}.{str(file.name).split(".")[-1]}'

            ivent.save()
            data = {
                'ivent': Ivent.objects.get(id=id)
            }

            return render(req, 'work/addivent.html', data)

        ivent = Ivent()
        ivent.name = data['name']
        ivent.type_ivent = data['type_ivent']
        ivent.date = data['data']
        ivent.desc = data['desc']

        file = req.FILES['photo']
        file_name = default_storage.save(f'{ivent.id}.{str(file.name).split(".")[-1]}', file)

        ivent.photo = f'../crm/media/{ivent.id}.{str(file.name).split(".")[-1]}'
        ivent.save()

        return redirect('ivent', ivent.id)

    data = {}
    if id:
        data = {
            'ivent': Ivent.objects.get(id=id)
        }

    return render(req, 'work/addivent.html', data)


def add_mailing(req, id=None):
    users = User_tg.objects.all()
    print(id)
    """Создать мероприятие"""
    if req.method == 'POST':
        data = req.POST.dict()
        print(str(data) + "test")

        if 'delete' in data and id:
            mailing = Mailing.objects.get(id=id)
            mailing.delete()
            return redirect('mailing')
        print(id)
        if id:
            print("FFFFF")
            mailing = Mailing.objects.get(id=id)
            mailing.name = data['name'] if 'name' in data else mailing.name
            mailing.desc = data['desc'] if 'desc' in data else mailing.desc
            mailing.photo = data['photo'] if 'photo' in data else mailing.photo
            mailing.save()

            return render(req, 'work/mailing.html', {'mailing': mailing})
        else:
            mailing = Mailing()
            mailing.name = data['name']
            mailing.desc = data['desc']
            file = req.FILES['photo']
            file_name = default_storage.save(f'{mailing.id}.{str(file.name).split(".")[-1]}', file)

            mailing.photo = f'../crm/media/{file_name}'
            mailing.numbers = data['our']
            mailing.save()

        # send messages to the people
        for phone in mailing.numbers.split():
            print(phone)
            try:
                user = User_tg.objects.get(phone=phone)
                send_message(user.tg_id, data['desc'])
            except:
                pass

        return redirect('mailing', mailing.id)

    try:
        mailing = Mailing.objects.get(id=id)
        return render(req, 'work/mailing.html', {'mailing': mailing, 'users': users})
    except:
        return render(req, 'work/mailing.html', {'users': users})
