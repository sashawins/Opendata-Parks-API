import json
import psycopg
import requests

# Specify each of your parameters in `config.py` before begin:
from config import host, port, user, password, database

# Connection with your PostgreSQL Database
conn = psycopg.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=database
)

cur = conn.cursor()

# Specifying the download link for our `parks` table:
url = "https://opendata.mkrf.ru/opendata/7705851331-parks/data-92-structure-3.json"

# Extracting the JSON file
response = requests.get(url)

if response.status_code == 200:
    # Extracting the data from file
    json_data = response.json()

    # Iterating over each record in the data
    for record in json_data:
        data_general_name = record['data']['general']['name']  # Название
        data_general_locale_name = record['data']['general']['locale']['name']  # Местоположение
        data_general_locale_timezone = record['data']['general']['locale']['timezone']  # Часовой пояс
        data_general_address_street = record['data']['general']['address']['street']  # Улица
        data_general_address_comment = record['data']['general']['address']['comment']  # Примечание
        data_general_address_fullAddress = record['data']['general']['address']['fullAddress']  # Адрес
        data_general_address_mapPosition = record['data']['general']['address']['mapPosition']  # На карте
        data_general_description = record['data']['general']['description']  # Описание
        data_general_contacts_website = ((record['data']['general']).get('contacts', {})).get('website', '')  # Адрес сайта
        data_general_contacts_email = ((record['data']['general']).get('contacts', {})).get('email', '')  # Адрес электронной почты
        data_general_contacts_phones = ((record['data']['general']).get('contacts', {})).get('phones', '')  # Номер
        data_general_image = (record['data']['general']).get('image', {})  # Изображение
        data_general_gallery = (record['data']['general']).get('gallery', {})  # Дополнительные изображения
        data_general_category_type = (record['data']['general']['category']).get('type', '')  # Тип категории
        data_general_category_name = record['data']['general']['category']['name']  # Категория
        data_general_organization_name = record['data']['general']['organization']['name']  # Юридическое лицо
        data_general_organization_locale_name = record['data']['general']['organization']['locale']['name']  # Местоположение
        data_general_organization_locale_timezone = record['data']['general']['organization']['locale']['timezone']  # Часовой пояс-1
        data_general_organization_address_street = record['data']['general']['organization']['address']['street']  # Улица
        data_general_organization_address_comment = (record['data']['general']['organization']['address']).get('comment', '')  # Примечание-1
        data_general_organization_address_fullAddress = record['data']['general']['organization']['address']['fullAddress']  # Адрес-1
        data_general_organization_address_mapPosition = (record['data']['general']['organization']['address']).get('mapPosition', '')  # На карте
        data_general_organization_inn = (record['data']['general']['organization']).get('inn', '')  # ИНН
        data_general_organization_type = record['data']['general']['organization']['type']  # Принадлежность
        data_general_organization_subordination_name = record['data']['general']['organization']['subordination']['name']  # Name
        data_general_organization_subordination_timezone = record['data']['general']['organization']['type']  # Часовой пояс-2
        data_general_organization_socialGroups = (record['data']['general']['organization']).get('socialGroups', [])  # Социальные сети
        for item in data_general_organization_socialGroups:
            data_general_organization_socialGroups_network = item.get('network', {})
            data_general_organization_socialGroups_name = item.get('name', {})
            data_general_organization_socialGroups_networkId = item.get('networkId', {})
            data_general_organization_socialGroups_updateDate = item.get('updateDate', {})
            data_general_organization_socialGroups_createDate = item.get('createDate', {})
            data_general_organization_socialGroups_accountId = item.get('accountId', {})
            data_general_organization_socialGroups_postingGroupId = item.get('postingGroupId', {})
        data_general_organization_id = record['data']['general']['organization']['id']  # Идентификатор ЕИПСК
        data_general_tags = (record['data']['general']).get('tags', {})  # Тэги
        data_general_videoHostings = (record['data']['general']).get('videoHostings', {})  # "Видео-хостинги"
        data_general_workingSchedule_0 = record['data']['general'].get('workingSchedule', {}).get('0', {})  # ПН
        data_general_workingSchedule_1 = record['data']['general'].get('workingSchedule', {}).get('1', {})  # ВТ
        data_general_workingSchedule_2 = record['data']['general'].get('workingSchedule', {}).get('2', {})  # СР
        data_general_workingSchedule_3 = record['data']['general'].get('workingSchedule', {}).get('3', {})  # ЧТ
        data_general_workingSchedule_4 = record['data']['general'].get('workingSchedule', {}).get('4', {})  # ПТ
        data_general_workingSchedule_5 = record['data']['general'].get('workingSchedule', {}).get('5', {})  # СБ
        data_general_workingSchedule_6 = record['data']['general'].get('workingSchedule', {}).get('6', {})  # ВС
        data_general_extraFields_artType = ((record['data']['general']).get('extraFields', {})).get('artType', '')  # Категория учреждения
        data_general_extraFields_audienceType = ((record['data']['general']).get('extraFields', {})).get('audienceType', '')  # Аудитория
        data_general_extraFields_language = ((record['data']['general']).get('extraFields', {})).get('language', '')  # Язык
        data_general_extraFields_professionalLevel = ((record['data']['general']).get('extraFields', {})).get('professionalLevel', '')  # Профессиональный уровень
        data_general_extraFields_virtualTour = ((record['data']['general']).get('extraFields', {})).get('virtualTour', '')  # Виртуальный тур
        data_general_extraFields_types = ((record['data']['general']).get('extraFields', {})).get('types', '')  # Types[]
        data_general_extraFields_seances = ((record['data']['general']).get('extraFields', {})).get('seances', '')  # Start
        data_general_id = record['data']['general']['id']  # Идентификатор места ЕИПСК
        data_general_externalInfo = (record['data']['general']).get('externalInfo', '')  # Название сервиса
        data_general_externalIds_eipskId = ((record['data']['general']).get('externalIds', {})).get('eipskId', '')  # ЕИПСК
        data_general_externalIds_culturarf = ((record['data']['general']).get('externalIds', {})).get('culturarf', '')  # Культура.РФ
        data_general_externalIds_goscatalogId = ((record['data']['general']).get('externalIds', {})).get('goscatalogId', '')  # Госкаталог
        data_general_externalIds_statistic = ((record['data']['general']).get('externalIds', {})).get('statistic', '')  # Статистика (КОПУК)
        data_info_createDate = record['data']['info']['createDate']  # Дата создания записи
        data_info_updateDate = record['data']['info']['updateDate']  # Дата последнего обновления записи

        cur.execute('''
            CREATE TABLE IF NOT EXISTS parks (
                "Название" VARCHAR,
                "Местоположение" VARCHAR,
                "Часовой пояс" VARCHAR,
                "Улица" VARCHAR,
                "Примечание" VARCHAR,
                "Адрес" VARCHAR,
                "На карте" VARCHAR,
                "Описание" VARCHAR,
                "Адрес сайта" VARCHAR,
                "Адрес электронной почты" VARCHAR,
                "Номер" VARCHAR,
                "Изображение" VARCHAR,
                "Дополнительные изображения" VARCHAR,
                "Тип категории" VARCHAR,
                "Категория" VARCHAR,
                "Юридическое лицо" VARCHAR,
                "Местоположение-1" VARCHAR,
                "Часовой пояс-1" VARCHAR,
                "Улица-1" VARCHAR,
                "Примечание-1" VARCHAR,
                "Адрес-1" VARCHAR,
                "На карте-1" VARCHAR,
                "ИНН" VARCHAR,
                "Принадлежность" VARCHAR,
                "Name" VARCHAR,
                "Часовой пояс-2" VARCHAR,
                "Социальные сети" VARCHAR,
                "Идентификатор ЕИПСК" VARCHAR,
                "Тэги" VARCHAR,
                "Видео-хостинги" VARCHAR,
                "ПН" VARCHAR,
                "ВТ" VARCHAR,
                "СР" VARCHAR,
                "ЧТ" VARCHAR,
                "ПТ" VARCHAR,
                "СБ" VARCHAR,
                "ВС" VARCHAR,
                "Категория учреждения" VARCHAR,
                "Аудитория"    VARCHAR,
                "Язык"    VARCHAR,
                "Профессиональный уровень"    VARCHAR,
                "Виртуальный тур"    VARCHAR,
                "Types[]"    VARCHAR,
                "Start"    VARCHAR,
                "Идентификатор места ЕИПСК" VARCHAR,
                "Название сервиса" VARCHAR,
                "ЕИПСК" VARCHAR,
                "Культура.РФ" VARCHAR,
                "Госкаталог" VARCHAR,
                "Статистика (КОПУК)" VARCHAR,
                "Дата создания записи" TIMESTAMP WITH TIME ZONE,
                "Дата последнего обновления записи" TIMESTAMP WITH TIME ZONE
                
            );
        ''')

        # Executing SQL insert into table query
        SQL = '''
        INSERT INTO parks (
            "Название",
            "Местоположение",
            "Часовой пояс",
            "Улица",
            "Примечание",
            "Адрес",
            "На карте",
            "Описание",
            "Адрес сайта",
            "Адрес электронной почты",
            "Номер",
            "Изображение",
            "Дополнительные изображения",
            "Тип категории",
            "Категория",
            "Юридическое лицо",
            "Местоположение-1",
            "Часовой пояс-1",
            "Улица-1",
            "Примечание-1",
            "Адрес-1",
            "На карте-1",
            "ИНН",
            "Принадлежность",
            "Name",
            "Часовой пояс-2",
            "Социальные сети",
            "Идентификатор ЕИПСК",
            "Тэги",
            "Видео-хостинги",
            "ПН",
            "ВТ",
            "СР",
            "ЧТ",
            "ПТ",
            "СБ",
            "ВС",
            "Категория учреждения",
            "Аудитория",
            "Язык",
            "Профессиональный уровень",
            "Виртуальный тур",
            "Types[]",
            "Start",
            "Идентификатор места ЕИПСК",
            "Название сервиса",
            "ЕИПСК",
            "Культура.РФ",
            "Госкаталог",
            "Статистика (КОПУК)",
            "Дата создания записи",
            "Дата последнего обновления записи"
            
            
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        ) ON CONFLICT DO NOTHING
        '''

        data = (
            data_general_name,
            data_general_locale_name,
            data_general_locale_timezone,
            data_general_address_street,
            data_general_address_comment,
            data_general_address_fullAddress,
            json.dumps(data_general_address_mapPosition, ensure_ascii=False),
            data_general_description,
            data_general_contacts_website,
            json.dumps(data_general_contacts_email, ensure_ascii=False),
            json.dumps(data_general_contacts_phones, ensure_ascii=False),
            json.dumps(data_general_image, ensure_ascii=False),
            json.dumps(data_general_gallery, ensure_ascii=False),
            data_general_category_type,
            data_general_category_name,
            data_general_organization_name,
            data_general_organization_locale_name,
            data_general_organization_locale_timezone,
            data_general_organization_address_street,
            data_general_organization_address_comment,
            data_general_organization_address_fullAddress,
            data_general_organization_address_mapPosition,
            data_general_organization_inn,
            data_general_organization_type,
            data_general_organization_subordination_name,
            data_general_organization_subordination_timezone,
            json.dumps(data_general_organization_socialGroups, ensure_ascii=False),
            data_general_organization_id,
            json.dumps(data_general_tags, ensure_ascii=False),
            json.dumps(data_general_videoHostings, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_0, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_1, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_2, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_3, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_4, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_5, ensure_ascii=False),
            json.dumps(data_general_workingSchedule_6, ensure_ascii=False),
            data_general_extraFields_artType,
            data_general_extraFields_audienceType,
            data_general_extraFields_language,
            data_general_extraFields_professionalLevel,
            data_general_extraFields_virtualTour,
            data_general_extraFields_types,
            data_general_extraFields_seances,
            data_general_id,
            json.dumps(data_general_externalInfo, ensure_ascii=False),
            data_general_externalIds_eipskId,
            data_general_externalIds_culturarf,
            data_general_externalIds_goscatalogId,
            data_general_externalIds_statistic,
            data_info_createDate,
            data_info_updateDate,
        )

        cur.execute(SQL, data)
    print("Data inserted successfully!")

    # Committing transaction
    conn.commit()

    # Closing connection
    cur.close()
    conn.close()

else:
    print("Extraction has failed:", response.status_code)

# Copyright (c) 2024 Alexander Omelekhin
