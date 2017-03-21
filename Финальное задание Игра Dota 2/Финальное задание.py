# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:40:37 2017


"""
import pandas as pd

#==============================================================================
# Считайте таблицу с признаками из файла features.csv с помощью кода, приведенного выше.
# Удалите признаки, связанные с итогами матча (они помечены в описании данных как отсутствующие в тестовой выборке).
#==============================================================================
data_train = pd.read_csv('features.csv')
data_test = pd.read_csv('features_test.csv')

columns_train_difference=data_train.columns.difference(data_test.columns.values.tolist()).tolist()#Удалите признаки, которых нет в тестовой выборке - получаем различие в колонках
data_train.drop(columns_train_difference, axis=1, inplace=True)#elfkztv внутри датасета

#==============================================================================
# Описание признаков в таблице
# match_id: идентификатор матча в наборе данных
# start_time: время начала матча (unixtime)
# lobby_type: тип комнаты, в которой собираются игроки (расшифровка в dictionaries/lobbies.csv)
# Наборы признаков для каждого игрока (игроки команды Radiant — префикс rN, Dire — dN):
#   r1_hero: герой игрока (расшифровка в dictionaries/heroes.csv)
#   r1_level: максимальный достигнутый уровень героя (за первые 5 игровых минут)
#   r1_xp: максимальный полученный опыт
#   r1_gold: достигнутая ценность героя
#   r1_lh: число убитых юнитов
#   r1_kills: число убитых игроков
#   r1_deaths: число смертей героя
#   r1_items: число купленных предметов
# Признаки события "первая кровь" (first blood). Если событие "первая кровь" не успело произойти за первые 5 минут, то признаки принимают пропущенное значение
#   first_blood_time: игровое время первой крови
#   first_blood_team: команда, совершившая первую кровь (0 — Radiant, 1 — Dire)
#   first_blood_player1: игрок, причастный к событию
#   first_blood_player2: второй игрок, причастный к событию
# Признаки для каждой команды (префиксы radiant_ и dire_)
#   radiant_bottle_time: время первого приобретения командой предмета "bottle"
#   radiant_courier_time: время приобретения предмета "courier"
#   radiant_flying_courier_time: время приобретения предмета "flying_courier"
#   radiant_tpscroll_count: число предметов "tpscroll" за первые 5 минут
#   radiant_boots_count: число предметов "boots"
#   radiant_ward_observer_count: число предметов "ward_observer"
#   radiant_ward_sentry_count: число предметов "ward_sentry"
#   radiant_first_ward_time: время установки командой первого "наблюдателя", т.е. предмета, который позволяет видеть часть игрового поля
# Итог матча (данные поля отсутствуют в тестовой выборке, поскольку содержат информацию, выходящую за пределы первых 5 минут матча)
# duration: длительность
# radiant_win: 1, если победила команда Radiant, 0 — иначе
# Состояние башен и барраков к концу матча (см. описание полей набора данных)
#   radiant_win
#   tower_status_dire
#   barracks_status_radiant
#   barracks_status_dire
#==============================================================================

#==============================================================================
# Проверьте выборку на наличие пропусков с помощью функции count(),
# которая для каждого столбца показывает число заполненных значений.
# Много ли пропусков в данных? Запишите названия признаков, имеющих пропуски, и
# попробуйте для любых двух из них дать обоснование, почему их значения могут быть пропущены.
#
#==============================================================================
train_size=len(data_train)
print("Select count=%s" % train_size)
for col in data_train.columns.values.tolist():
    count=data_train[col].count()
    if count!=train_size:
        print("Column %s, len=%s" % (col,count))

#==============================================================================
# Select count=97230
# Column first_blood_time, len=77677 - Если событие "первая кровь" не успело произойти за первые 5 минут, то признаки принимают пропущенное значение
# Column first_blood_team, len=77677 - Если событие "первая кровь" не успело произойти за первые 5 минут, то признаки принимают пропущенное значение
# Column first_blood_player1, len=77677
# Column first_blood_player2, len=53243
# Column radiant_bottle_time, len=81539
# Column radiant_courier_time, len=96538
# Column radiant_flying_courier_time, len=69751
# Column radiant_first_ward_time, len=95394
# Column dire_bottle_time, len=81087
# Column dire_courier_time, len=96554
# Column dire_flying_courier_time, len=71132
# Column dire_first_ward_time, len=95404
#==============================================================================
