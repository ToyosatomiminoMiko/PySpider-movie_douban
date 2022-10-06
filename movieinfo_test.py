def parse(object_: object, obj_list: list) -> list:
    rl = []
    for obj in obj_list:
        rl.append(object_(obj))
    return rl


class Person:
    def __init__(self, d: dict):
        self.name: str = d['name']
        self.id: int = int(d['url'].split('/')[2])

    def __str__(self) -> str:
        return f'{self.__ne__}/{self.id}:"{self.name}"'

    def save_data(self):
        ...


class AggregateRating:
    def __init__(self, d: dict):
        self.rating_count: int = int(d['ratingCount'])
        self.best_rating: int = int(d['bestRating'])
        self.worst_rating: int = int(d['worstRating'])
        self.rating_value: float = float(d['ratingValue'])
        self.id: int = d['id']

    def __str__(self) -> str:
        return f"{self.__ne__}/movie_id:{self.id}"

    def save_data(self):
        ...


class Movie:
    """
    这是单个的电影
    通过id获取v其信息
    """

    def __init__(self, m_id: str):
        # get_data -> movie_info
        self.movie_info = {'@context': 'http://schema.org',
                           'name': '夺冠',
                           'url': '/subject/30128916/',
                           'image': 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2620083313.jpg',
                           'director': [{'@type': 'Person', 'url': '/celebrity/1274300/', 'name': '陈可辛 Peter Chan'}],
                           'author': [{'@type': 'Person', 'url': '/celebrity/1327606/', 'name': '张冀 Ji Zhang'}],
                           'actor': [{'@type': 'Person', 'url': '/celebrity/1035641/', 'name': '巩俐 Li Gong'},
                                     {'@type': 'Person', 'url': '/celebrity/1274242/', 'name': '黄渤 Bo Huang'},
                                     {'@type': 'Person', 'url': '/celebrity/1274840/', 'name': '吴刚 Gang Wu'},
                                     {'@type': 'Person', 'url': '/celebrity/1354775/', 'name': '彭昱畅 Yuchang Peng'},
                                     {'@type': 'Person', 'url': '/celebrity/1426542/', 'name': '白浪 Lydia Bai'},
                                     {'@type': 'Person', 'url': '/celebrity/1411592/', 'name': '朱婷 Ting Zhu'},
                                     {'@type': 'Person', 'url': '/celebrity/1425182/', 'name': '徐云丽 Yunli Xu'},
                                     {'@type': 'Person', 'url': '/celebrity/1423856/', 'name': '张常宁 Changning Zhang'},
                                     {'@type': 'Person', 'url': '/celebrity/1423861/', 'name': '姚迪 Di Yao'},
                                     {'@type': 'Person', 'url': '/celebrity/1423860/', 'name': '林莉 Li Lin'},
                                     {'@type': 'Person', 'url': '/celebrity/1423858/', 'name': '刘晓彤 Xiaotong Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1423857/', 'name': '颜妮 Ni Yan'},
                                     {'@type': 'Person', 'url': '/celebrity/1426543/', 'name': '李冬徐 Dongxu Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1426544/', 'name': '马雪纯 Xuechun Ma'},
                                     {'@type': 'Person', 'url': '/celebrity/1426547/', 'name': '刘畅 Chang Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1426550/', 'name': '刘贞宏 Zhenhong Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1367486/', 'name': '惠若琪 Ruoqi Hui'},
                                     {'@type': 'Person', 'url': '/celebrity/1400391/', 'name': '丁霞 Xia Ding'},
                                     {'@type': 'Person', 'url': '/celebrity/1400389/', 'name': '袁心玥 Xinyue Yuan'},
                                     {'@type': 'Person', 'url': '/celebrity/1423859/', 'name': '龚翔宇 Xiangyu Gong'},
                                     {'@type': 'Person', 'url': '/celebrity/1324619/', 'name': '李现 Xian Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1318610/', 'name': '刘敏涛 Mintao Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1426539/', 'name': '陈展 Zhan Chen'},
                                     {'@type': 'Person', 'url': '/celebrity/1426540/', 'name': '罗慧 Hui Luo'},
                                     {'@type': 'Person', 'url': '/celebrity/1426546/', 'name': '毛雯 Wen Mao'},
                                     {'@type': 'Person', 'url': '/celebrity/1426545/', 'name': '李紫微 Ziwei Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1426541/', 'name': '凌敏 Min Ling'},
                                     {'@type': 'Person', 'url': '/celebrity/1426549/', 'name': '李阳一 Yangyi Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1426548/', 'name': '刘晨曦 Chenxi Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1274762/', 'name': '邢佳栋 Jiadong Xing'},
                                     {'@type': 'Person', 'url': '/celebrity/1445156/', 'name': '曾春蕾 Chunlei Zeng'},
                                     {'@type': 'Person', 'url': '/celebrity/1445157/', 'name': '刘晏含 Yanhan Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1424363/', 'name': '王梦洁 Wang Mengjie'},
                                     {'@type': 'Person', 'url': '/celebrity/1424361/', 'name': '郑益昕 Zheng Yixin'},
                                     {'@type': 'Person', 'url': '/celebrity/1445158/', 'name': '杨涵玉 Hanyu Yang'},
                                     {'@type': 'Person', 'url': '/celebrity/1424362/', 'name': '王媛媛 Yuanyuan Wang'},
                                     {'@type': 'Person', 'url': '/celebrity/1445159/', 'name': '王路加 Lujia Wang'},
                                     {'@type': 'Person', 'url': '/celebrity/1445161/', 'name': '李珊 Shan Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1423855/', 'name': '安家杰 Jiajie An'},
                                     {'@type': 'Person', 'url': '/celebrity/1423862/', 'name': '玛丽安妮·斯泰因布莱彻 Marianne Steinbrecher'},
                                     {'@type': 'Person', 'url': '/celebrity/1423863/', 'name': '杰奎琳·卡瓦霍 Jaqueline Carvalho'},
                                     {'@type': 'Person', 'url': '/celebrity/1423864/', 'name': '帕乌拉·配奇诺 Paula Pequeno'},
                                     {'@type': 'Person', 'url': '/celebrity/1429826/', 'name': '雅南 Fiona Fu'},
                                     {'@type': 'Person', 'url': '/celebrity/1408521/', 'name': '许文姗 Audrey Hui'},
                                     {'@type': 'Person', 'url': '/celebrity/1430029/', 'name': '宋世雄 Shixiong Song'},
                                     {'@type': 'Person', 'url': '/celebrity/1337707/', 'name': '高野浩幸 Hiroyuki Takano'},
                                     {'@type': 'Person', 'url': '/celebrity/1445168/', 'name': '霍尔·约翰逊 Halle Johnson'},
                                     {'@type': 'Person', 'url': '/celebrity/1445167/', 'name': '孟子旋 Zixuan Meng'},
                                     {'@type': 'Person', 'url': '/celebrity/1445166/', 'name': '李雅楠 Yanan Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1445165/', 'name': '小平花织 Kodaira Kaori'},
                                     {'@type': 'Person', 'url': '/celebrity/1445164/', 'name': '中道瞳 Hitomi Nakamichi'},
                                     {'@type': 'Person', 'url': '/celebrity/1445163/', 'name': '姜倩雯 Qianwen Jiang'},
                                     {'@type': 'Person', 'url': '/celebrity/1445162/', 'name': '刘抒妍 Shuyan Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1445160/', 'name': '迈克·杰克逊 Mike Jackson'},
                                     {'@type': 'Person', 'url': '/celebrity/1445215/', 'name': '张寒艳 Hanyan Zhang'},
                                     {'@type': 'Person', 'url': '/celebrity/1445216/', 'name': '赵晨璐 Chenlu Zhao'},
                                     {'@type': 'Person', 'url': '/celebrity/1445673/', 'name': '刘桃 Tao Liu'},
                                     {'@type': 'Person', 'url': '/celebrity/1445218/', 'name': '李孟婕 Mengjie Li'},
                                     {'@type': 'Person', 'url': '/celebrity/1445217/', 'name': '田欣 Xin Tian'},
                                     {'@type': 'Person', 'url': '/celebrity/1445674/', 'name': '谢星 Xing Xie'},
                                     {'@type': 'Person', 'url': '/celebrity/1352302/', 'name': '王永强 Yongqiang Wang'},
                                     {'@type': 'Person', 'url': '/celebrity/1420478/', 'name': '杜功海 Gonghai Du'}],
                           'datePublished': '2020-09-25',
                           'genre': ['剧情', '运动'],
                           'duration': 'PT2H15M',
                           'description': '2008年8月15日，北京奥运会女排比赛，中国VS美国。戴着金丝框眼镜的郎平（巩俐 饰）坐在美国队教练席上，大气沉稳，目光如电；中国队教练（黄渤 饰）站在场边，全神贯注，面带笑容。中国队教练望向郎平，...',
                           '@type': 'Movie',
                           'aggregateRating': {'@type': 'AggregateRating',
                                               'ratingCount': '413539',
                                               'bestRating': '10',
                                               'worstRating': '2',
                                               'ratingValue': '7.1'}
                           }

        # movie_list -> id
        self.id: int = int(m_id)
        self.title: str = ''
        self.image_url: str = ''
        self.director: list = []
        self.author: list = []
        self.actor: list = []
        self.date_published: str = ''  # 上映时间
        self.genre: str = ''
        self.duration: str = ''  # 时长
        self.description: str = ''
        self.aggregate_rating: object = AggregateRating

    def save_data(self):
        self.title = self.movie_info['name']
        print("title:", self.title)

        self.id = int(self.movie_info['url'].split("/")[2])
        print("id:", self.id)

        self.image_url = self.movie_info['image']
        print("image_url:", self.image_url)

        self.director = parse(Person, self.movie_info['director'])
        print("director:", self.director)

        self.author = parse(Person, self.movie_info['author'])
        print("author:", self.author)

        self.actor = parse(Person, self.movie_info['actor'])
        # print('actor:', self.actor[0])
        print('actor:', self.actor)

        self.movie_info['aggregateRating']['id'] = self.id
        self.aggregate_rating = parse(AggregateRating, [self.movie_info['aggregateRating']])
        # print('aggregate_rating:', self.aggregate_rating[0])
        print('aggregate_rating:', self.aggregate_rating)

        self.date_published = self.movie_info['datePublished']
        print("date_published:", self.date_published)

        self.genre = self.movie_info['genre']
        print("genre:", self.genre)

        self.duration = self.movie_info['duration']
        print("duration:", self.duration)

        self.description = self.movie_info['description']
        print("description:", self.description)


m = Movie('30128916')
m.save_data()
