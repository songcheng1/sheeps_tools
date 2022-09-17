# -*- coding: utf-8 -*-
# @Time     : 2022/9/17 10:00
# @File     : sheep_tools.py
import requests

class SheepTools:
    def __init__(self, token, keywords, rank_time='180'):
        self.headers = {
            'Host': 'cat-match.easygame2021.com',
            'Connection': 'keep-alive',
            'charset': 'utf-8',
            't': token,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM7.181205.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220709 Mobile Safari/537.36 MMWEBID/2810 MicroMessenger/8.0.25.2200(0x28001953) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'content-type': 'application/json',
            'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/17/page-frame.html',
        }
        self.params = {
            'rank_score': '1',
            'rank_state': '1',
            'rank_role': '1',
            'skin': '1',
        }
        self.keywords = keywords
        self.rank_time = rank_time

    def sheep_tools(self, url, rank_time):
        """
        rank_time: Time of joining sheep OR Time of finished
        """
        params = {'rank_time': rank_time}
        params.update(self.params)
        response = requests.get(url=url, params=params, headers=self.headers)
        return response

    def main(self):
        if self.keywords == '加入羊群':
            url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over'
        else:
            url = 'https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over'
        topic_game_over = self.sheep_tools(url, self.rank_time)
        print(f"{topic_game_over.status_code}, data={topic_game_over.text}")

def runserver(token, keywords, rank_time):
    # rank_time 耗时时间
    sheep_tools = SheepTools(token, keywords, rank_time)
    sheep_tools.main()

def thread_pool(max_workers, max_count, token, keywords, rank_time='180'):
    # start thread pool
    with ThreadPoolExecutor(max_workers) as e:
        for spu_info in range(1, max_count):
            e.submit(runserver, token, keywords, rank_time)


if __name__ == '__main__':
    # max_workers 开启的线程池个数,决定你通关的速度
    # max_count 最多请求次数, 决定你通关的数量
    # token：通过工具抓包获取（fd, 青花瓷）
    # 如果要加入羊群需要输入关键字 keywords = '加入羊群'
    from concurrent.futures.thread import ThreadPoolExecutor
    token ='<<自己通过抓包工具获取的token值>>'
    keywords = '通关'
    rank_time = '120'
    thread_pool(max_workers=5, max_count=50, token=token, keywords=keywords, rank_time=rank_time)
