#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cluster.api_init import requt
import time


def index(k3):
    data = requt(k3)
    aad = open('./log/{0}.log'.format(k3), 'r+')
    result_read = aad.read()
    if result_read != data['data']['backData']['lotteryOpen'][0]['openTime']:
        aad.seek(0)
        aad.write(data['data']['backData']['lotteryOpen'][0]['openTime'])
        # 取出5个
        aad.close()
        result_list = data['data']['backData']['lotteryOpen'][0:7]
        count_list = [_['count'] for _ in result_list]
        print(count_list)
        if int(count_list[0]) < 11 and int(count_list[1]) > 10 and int(count_list[2]) > 10 and \
                int(count_list[3]) > 10 and int(count_list[4]) > 10 and int(count_list[5]) > 10 \
                and int(count_list[6]) > 10 and int(count_list[7]) > 10:
            count_z = int(count_list[0])
            from cluster.api_init import pose_send
            if k3 != 'XY1K3':
                pose_send(2, int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '大', k3)
            else:
                pose_send(2, int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '大', k3)
            for i in range(2):
                while True:
                    with open('./log/{0}.log'.format(k3), 'r+') as f:
                        result_result = f.read().strip()
                        data = requt(k3)
                        time.sleep(25)
                        if result_result != data['data']['backData']['lotteryOpen'][0]['openTime']:
                            f.seek(0)
                            f.write(data['data']['backData']['lotteryOpen'][0]['openTime'])
                            if count_z < 11 and int(data['data']['backData']['lotteryOpen'][0]['count']) < 11:
                                time.sleep(1)
                                if k3 != 'XY1K3':
                                    pose_send((i+1) * 4, int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1,
                                              '大', k3)
                                else:
                                    pose_send((i + 1) * 4,
                                              int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '大', k3)
                                break
                            else:
                                return

        elif int(count_list[0]) > 10 and int(count_list[1]) < 11 and int(count_list[2]) < 11 and int(
                count_list[3]) < 11 and int(count_list[4]) < 11 and int(count_list[5]) < 11 and int(count_list[6]) < 11\
                and int(count_list[7]) < 11:
            count_z = int(count_list[0])
            from cluster.api_init import pose_send
            if k3 != 'XY1K3':
                pose_send(2, int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '小', k3)
            else:
                pose_send(2, int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '小', k3)
            for i in range(2):
                while True:
                    with open('./log/{0}.log'.format(k3), 'r+') as f:
                        result_result = f.read()
                        data = requt(k3)
                        time.sleep(25)
                        if result_result != data['data']['backData']['lotteryOpen'][0]['openTime']:
                            f.seek(0)
                            f.write(data['data']['backData']['lotteryOpen'][0]['openTime'])
                            if count_z > 10 and int(data['data']['backData']['lotteryOpen'][0]['count']) > 10:
                                time.sleep(1)
                                if k3 != 'XY1K3':
                                    pose_send((i + 1) * 4,
                                              int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '小', k3)
                                else:
                                    pose_send((i + 1) * 4,
                                              int(data['data']['backData']['lotteryOpen'][0]['issueNo']) + 1, '小', k3)
                                break
                            else:
                                return
    else:
        return


