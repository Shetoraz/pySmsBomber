import random
import string


class Person:
    def __init__(self):
        self.username = self.password = "".join(
            random.choice(string.ascii_letters) for _ in range(12)
        )
        self.russian_name = "".join(
            random.choice(
                "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
            )
            for _ in range(5)
        )
        self.english_name = "".join(
            random.choice(
                "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
            )
            for _ in range(5)
        )
        self.email = (
            f"{self.username}@{random.choice(['gmail.com', 'mail.ru', 'yandex.ru'])}"
        )
