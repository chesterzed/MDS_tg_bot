from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest, EditTitleRequest, DeleteChannelRequest, EditAdminRequest
from telethon.tl.functions.messages import CreateChatRequest, ExportChatInviteRequest
from telethon.tl.types import InputPeerChannel, ChatAdminRights, PeerUser

import asyncio

from work.models import User_tg, Chat, Channel


def create_channel(namechannel, descrchannel, linkchannel, id):
    """Создание канала"""
    try:
        client = _get_client()
        channel = Channel.objects.get(id=id)

        createdPrivateChannel = client(CreateChannelRequest(namechannel,descrchannel,megagroup=False))

        newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
        newChannelAccessHash = createdPrivateChannel.__dict__["chats"][0].__dict__["access_hash"]
        desiredPublicUsername = linkchannel

        checkUsernameResult = client(CheckUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
        if(checkUsernameResult==True):
            publicChannel = client(UpdateUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))

            channel.tg_id = newChannelID
            channel.save()
            client.disconnect()
            return True
        
        else:
            client.disconnect()
            return False

    except:
        client.disconnect()

def change_channel(namechannel, username):
    """Редактирование канала"""
    try:
        client = _get_client()
        client(
            EditTitleRequest(
                channel=username,
                title=namechannel
            )
        )
        client.disconnect()
    except:
        client.disconnect()


def add_admin(id, tg_id):
    """Добавление администраторов в канал"""
    try:
        client = _get_client()
        rights = ChatAdminRights(
            change_info=True,
            post_messages=True,
            delete_messages=True,
            ban_users=True,
            invite_users=True,
            pin_messages=True,
            add_admins=False,
            anonymous=True,
            manage_call=True,
            other=True
        )

        client.get_entity(PeerUser(tg_id))

        client(
            EditAdminRequest(
                channel=int(id),
                user_id=int(tg_id),
                admin_rights=rights,
                rank='Admin'
            )
        )
        client.disconnect()
    except Exception as e:
        # print(e)
        client.disconnect()


def delete_channel(username):
    """Редактирование канала"""
    try:
        client = _get_client()
        client(
            DeleteChannelRequest(
                channel=username
            )
        )
        client.disconnect()
    except:
        client.disconnect()


def create_chat(title, users, id):
    """Создание чата"""
    try:
        client = _get_client()
        id_chat = client(
            CreateChatRequest(
                users=['Test_py_dnk_bot'],
                title=title
            )
        ).chats[0].id
        link = client(ExportChatInviteRequest(id_chat)).link

        chat = Chat.objects.get(id=id)
        chat.link = link
        chat.tg_id = id_chat
        chat.save()
        
        for el in users:
            try:
                user = User_tg.objects.get(phone = el)
                user.chat = id
                user.save()
                client.send_message(
                    'Test_py_dnk_bot',
                    f'/send {user.tg_id} У нас открыся чат, приглашаем вступить \n{link}'
                )

            except Exception as e:
                # # print(e)
                pass

    except Exception as e:
        pass
    
    client.disconnect()


def send_message(user, message):
    client = _get_client()
    client.send_message(
                    'Test_py_dnk_bot',
                    f'/send {user} {message}'
                )

    client.disconnect()


def _get_client(): 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    api_id = 12278609
    api_hash = '35a1e01383db6f82ff373ca0c9473d2d'
    name = 'mds_test551123'

    client = TelegramClient(name, api_id, api_hash, loop=loop)
    client.start()
    client.connect()

    return client
