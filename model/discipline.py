class Discipline:

    positions: list = []
    name: str = ""
    teacher: str = ""
    weeklyWorkload: int = ""
    dependencies: list = []
    timeCourse: int = 1

    def __init__(self, id: str, name: str, teacher: int, weeklyWorkload: int, dependencies: list, timeCourse: int):
        self.id: int = id
        self.name: str = name
        self.teacher: str = teacher
        self.weeklyWorkload: int = weeklyWorkload
        self.dependencies: list = dependencies
        self.timeCourse: int = timeCourse