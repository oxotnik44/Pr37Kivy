from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image


Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')

number_correct_answers = 0
number_question = 1
music = SoundLoader.load('three-days-grace-strange-days.mp3')


question_list = [['https://almode.ru/uploads/posts/2020-07/1596081783_13-p-kharrison-ford-instagramm-16.jpg', 'Марк Хэмилл', 'Харрисон Форд', 'Кэрри Фишер', 'Энтони Дэниелс', 2],
                 ['https://v1.popcornnews.ru/k2/news/1200/upload/iHAr0T.jpg',
                     'Джек Николсон', 'Леонардо Ди Каприо', 'Мэттью МакКонахи', 'Брэд Питт', 2],
                 ['https://i.pinimg.com/originals/b8/86/57/b8865711b76c03b1eac95b9c5c4f21aa.jpg',
                     'Тим Роббинс', 'Морган Фримен', 'Боб Гантон', 'Уильям Сэдлер', 1],
                 ['https://molva33.ru/wp-content/uploads/2021/02/1-6.jpg', 'Сильвестр Сталлоне',
                  'Арнольд Шварценеггер', 'Брюс Уиллис', 'Вин Дизель', 2],
                 ['https://24smi.org/public/media/resize/660x-/celebrity/2022/11/18/lgxvqnz158y6-marlon-brando.jpg',
                  'Роберт Де Ниро', 'Марлон Брандо', 'Аль Пачино', 'Джеймс Каан', 2],
                 ['https://i.pinimg.com/736x/b0/ff/9d/b0ff9d0e231604370577b3530ea6ebdb.jpg',
                  'Том Хэнкс', 'Мэтт Дэймон', 'Джон Траволта', 'Брэд Питт', 1],
                 ['https://i.pinimg.com/originals/95/cf/d2/95cfd2d582e2b907a796ff7cfda1ef5b.jpg',
                  'Мэрил Стрип', 'Холли Хантер', 'Джулия Робертс', 'Мег Райан', 3],
                 ['https://static.wikia.nocookie.net/starwars/images/d/d9/Malcolm_McDowell.jpg/revision/latest?cb=20220911203404',
                  'Джек Николсон', 'Харви Кейтель', 'Рутгер Хауэр', 'Малкольм Макдауэлл', 4],
                 ['https://almode.ru/uploads/posts/2021-03/1617047354_43-p-rassel-krou-43.jpg',
                  'Рассел Кроу', 'Джоакин Феникс', 'Хавьер Бардем', 'Джим Керри', 1],
                 ['https://www.kino-teatr.ru/news/22919/203089.jpg', 'Джонни Депп',
                  'Орландо Блум', 'Кира Найтли', 'Джек Девенпорт', 1],
                 ['https://damion.club/uploads/posts/2022-02/1644408895_9-damion-club-p-maikl-dzh-foks-znamenitosti-10.jpg',
                  'Билли Зейн', 'Том Хэнкс', 'Кристофер Ллойд', 'Майкл Дж. Фокс', 4],
                 ['https://almode.ru/uploads/posts/2021-04/1618121580_8-p-zhan-reno-8.jpg',
                  'Жан Рено', 'Натали Портман', 'Гэри Олдман', 'Дэнни Эйелло', 1],
                 ['https://almode.ru/uploads/posts/2020-07/1596169523_7-p-elaidzha-vud-instagramm-11.jpg',
                  'Вигго Мортенсен', 'Шон Эстин', 'Элайджа Вуд', 'Иэн Маккеллен', 3],
                 ['https://cdn.fishki.net/upload/post/201408/17/1294670/Men___Male_Celebrity_Actor_Robert_De_Niro_057900_.jpg', 'Джеймс Вудс', 'Элизабет МакГоверн', 'Роберт Де Ниро', 'Джо Пеши', 3]]


class MainWidget(BoxLayout):
    def new_question(self):
        img_result = None  # Initialize img_result to None

        if len(question_list) > 0:
            question = question_list[randint(0, len(question_list)-1)]
            self.ids['img_question'].source = question[0]
            self.ids['btn_answer1'].text = question[1]
            self.ids['btn_answer2'].text = question[2]
            self.ids['btn_answer3'].text = question[3]
            self.ids['btn_answer4'].text = question[4]
        else:
            text = '\n Результат: ' + str(number_correct_answers) + ' из 15'
            self.ids['lbl_question'].text = text
            self.remove_widget(self.ids['img_question'])
            self.remove_widget(self.ids['layout_btns'])
            if number_correct_answers > 12:
                self.ids['img_result'].source = 'source/megaxarosh.jpg'
            elif number_correct_answers > 8:
                self.ids['img_result'].source = 'source/xarosh.jpg'

            elif number_correct_answers > 4:
                self.ids['img_result'].source = 'source/neploh.jpg'

            self.ids['img_result'].opacity = 1

    def btn_pressed(self, number_button):
        question: list
        for i in question_list:
            if (i[0] == self.ids['img_question'].source):
                question = i
                break  # Перебор списка, чтобы выбрать вопрос который выпал из списка
        global number_correct_answers
        global number_question
        if (number_button == question[5]):
            number_correct_answers += 1

        number_question += 1
        question_list.remove(question)
        self.new_question()


class MainApp(App):
    def build(self):
        app = MainWidget()
        app.new_question()  # вызываем new_question из build метода, когда окно приложения готово
        return app


if __name__ == '__main__':
    music = SoundLoader.load('three-days-grace-strange-days.mp3')
    music.volume = 0.1
    music.play()

    MainApp().run()
