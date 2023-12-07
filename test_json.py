import json
import requests
import pandas as pd
import numpy as np

json_line = \
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": [
                                "GML",
                                "XML"
                            ]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }


# json_object = json.loads(json_line)
# print(json_line['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][0])


def export_all_calendar_plans():
    api_token = ''
    url = 'https://api.smartsheet.com/2.0/sheets?includeAll=true'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json'
    }
    sheet_data = {}
    arr_id, arr_name, arr_accessLevel, arr_permalink, arr_createdAt, arr_modifiedAt = [], [], [], [], [], []

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sheet_data = response.json()
    else:
        print(f'Error: {response.status_code}')

    for calendar_plan in sheet_data['data']:
        arr_id.append(calendar_plan['id'])
        arr_name.append(calendar_plan['name'])
        arr_accessLevel.append(calendar_plan['accessLevel'])
        arr_permalink.append(calendar_plan['permalink'])
        arr_createdAt.append(calendar_plan['createdAt'])
        arr_modifiedAt.append(calendar_plan['modifiedAt'])

    df = pd.DataFrame(np.column_stack((arr_id,
                                       arr_name,
                                       arr_accessLevel,
                                       arr_permalink,
                                       arr_createdAt,
                                       arr_modifiedAt)),
                      columns=['id',
                               'name',
                               'accessLevel',
                               'permalink',
                               'createdAt',
                               'modifiedAt'])
    return df


def export_one_calendar_plan(sheet_id):
    api_token = ''
    url = f'https://api.smartsheet.com/2.0/sheets/{sheet_id}'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json'
    }
    sheet_data = {}
    titles = {
        'Имя задачи': None,
        'Длительность': None,
        'Начало': None,
        'Готово': None,
        'Предшественники': None,
        'Ответственный': None,
        '% выполнено': None,
        'Состояние': None,
        'Комментарии': None,
        'Документы': None,
        'Соответствует этапу': None,
        'Базовый показатель - начало': None,
        'Базовый показатель - конец': None,
        'Расхождение': None
    }
    arrays = {}
    arr_row_id, arr_row_number, arr_task_name, arr_task_duration = [], [], [], []
    arr_task_start, arr_task_end, arr_task_parent, arr_task_responsible = [], [], [], []
    arr_task_percent_done, arr_task_state, arr_task_comment, arr_task_docs = [], [], [], []
    arr_task_stage, arr_task_base_start, arr_task_base_end, arr_task_gap = [], [], [], []

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sheet_data = response.json()
        # print(str(sheet_data).replace('\"', '\\"').replace('\'', '\"').replace('False', 'false').replace('True', 'true'))
    else:
        print(f'Error: {response.status_code}')

    for column in sheet_data['columns']:
        if column['title'] in titles.keys():
            titles[column['title']] = column['id']

    all_column_ids = [
        titles['Имя задачи'],
        titles['Длительность'],
        titles['Начало'],
        titles['Готово'],
        titles['Предшественники'],
        titles['Ответственный'],
        titles['% выполнено'],
        titles['Состояние'],
        titles['Комментарии'],
        titles['Документы'],
        titles['Соответствует этапу'],
        titles['Базовый показатель - начало'],
        titles['Базовый показатель - конец'],
        titles['Расхождение']
    ]

    for row in sheet_data['rows']:
        row_values = {column_id: None for column_id in all_column_ids}

        for cell in row['cells']:
            column_id = cell['columnId']
            if column_id in row_values:
                row_values[column_id] = cell.get('value')

        arr_task_name.append(row_values[titles['Имя задачи']])
        arr_task_duration.append(row_values[titles['Длительность']])
        arr_task_start.append(row_values[titles['Начало']])
        arr_task_end.append(row_values[titles['Готово']])
        arr_task_parent.append(row_values[titles['Предшественники']])
        arr_task_responsible.append(row_values[titles['Ответственный']])
        arr_task_percent_done.append(row_values[titles['% выполнено']])
        arr_task_state.append(row_values[titles['Состояние']])
        arr_task_comment.append(row_values[titles['Комментарии']])
        arr_task_docs.append(row_values[titles['Документы']])
        arr_task_stage.append(row_values[titles['Соответствует этапу']])
        arr_task_base_start.append(row_values[titles['Базовый показатель - начало']])
        arr_task_base_end.append(row_values[titles['Базовый показатель - конец']])
        arr_task_gap.append(row_values[titles['Расхождение']])

    df = pd.DataFrame(np.column_stack((arr_task_name,
                                       arr_task_duration,
                                       arr_task_start,
                                       arr_task_end,
                                       arr_task_parent,
                                       arr_task_responsible,
                                       arr_task_percent_done,
                                       arr_task_state,
                                       arr_task_comment,
                                       arr_task_docs,
                                       arr_task_stage,
                                       arr_task_base_start,
                                       arr_task_base_end,
                                       arr_task_gap)),
                      columns=['task_name',
                               'task_dur',
                               'task_start',
                               'task_end',
                               'task_parent',
                               'task_responsible',
                               'task_percent_done',
                               'task_state',
                               'task_comment',
                               'task_docs',
                               'task_stage',
                               'task_base_start',
                               'task_base_end',
                               'task_gap'])
    return df


# print(export_all_calendar_plans().to_string())
# sheet_id = 'Q3jV68JcPvH5c973H56M7W8R8pQRpvWXhgMJrWp1'
sheet_id = '75R7HvcH7GHG3V3XJ9XV5QqWxwhm2q2hRPCJpG71'
print(export_one_calendar_plan(sheet_id).to_string())
