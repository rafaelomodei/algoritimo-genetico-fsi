from io import TextIOWrapper
import json
from discipline import Discipline

def readFile(file: str) -> list:
    disciplineList: list[Discipline] = list()

    with open(file, 'r', encoding='utf8') as ctx:
        data: TextIOWrapper = json.load(ctx)

        for discipline in data:
            currentDiscipline: Discipline = Discipline(
                discipline['id'],
                discipline['name'],
                discipline['teacher'],
                discipline['weeklyWorkload'],
                discipline['dependencies'],
                discipline['timeCourse'],
            )
            disciplineList.append(currentDiscipline)

    return disciplineList
