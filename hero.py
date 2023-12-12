class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}\nСуперспособность: {self.superpower}\nЗдоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Spider-Man", "Peter Parker", "Superhuman abilities, spider-sense", 100, "With great power comes great responsibility")

print(hero.get_name())
hero.double_health_points()
print(hero)
print(f" Длина коронной фразы героя : ", hero.__len__())
