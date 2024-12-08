import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password: int = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: float, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now: float = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users: dict[str, User] = {}
        self.videos: dict[str, Video] = {}
        self.current_user: User | None = None

    def log_in(self, nickname: str, password: str):
        if nickname not in self.users.keys():
            print(f"Пользователь {nickname} не найден.")
            return
        user = self.users[nickname]
        if user.password != hash(password):
            print("Пароль не верный!")
            return
        self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return
        user = User(nickname, password, age)
        self.users[nickname] = user
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        new_video = {
            video.title: video
            for video in args
            if isinstance(video, Video) and video.title not in self.videos
        }
        self.videos |= new_video

    def get_videos(self, keyword: str) -> list[str]:
        titles = [str(key) for key in self.videos.keys()]
        if keyword != "":
            titles = [title for title in titles if keyword.lower() in title.lower()]
        return titles

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = self.videos.get(title, None)
        if video is None:
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        while video.time_now < video.duration:
            video.time_now += 1
            if video.time_now > video.duration:
                video.time_now = video.duration
            print(video.time_now, "", end="")
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video("Лучший язык программирования 2024 года", 200)
    v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos("лучший"))
    print(ur.get_videos("ПРОГ"))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video("Для чего девушкам парень программист?")
    ur.register("vasya_pupkin", "lolkekcheburek", 13)
    ur.watch_video("Для чего девушкам парень программист?")
    ur.register("urban_pythonist", "iScX4vIJClb9YQavjAgF", 25)
    ur.watch_video("Для чего девушкам парень программист?")

    # Проверка входа в другой аккаунт
    ur.register("vasya_pupkin", "F8098FM8fjm9jmi", 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video("Лучший язык программирования 2024 года!")
