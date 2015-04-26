from database import Session
from models import Professor, User, Comment
import pickle


dept_map = pickle.load(open("dept_map.p", "rb"))
session = Session()

departments  = dept_map.keys()
for department in departments:
    for name in dept_map[department]:
        sections = name.split(" ")

        first = sections[0]
        middle = filter(lambda x: "." in x, sections)
        if len(middle) != 0:
            middle = middle[0]
        else:
            middle = None
        others = filter(lambda x: not "." in x, sections[1:])
        last = "-".join(others)

        session.add(Professor(first_name=sections[0], middle_name=middle, last_name=last, department=department))

session.commit()

query = session.query(Professor).filter_by(department= u'Industrial Engineering\xa0Professors').all()

for q in query:
    print q.first_name, q.middle_name, q.last_name, q.department

