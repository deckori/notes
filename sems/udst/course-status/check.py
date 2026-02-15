import json

# Load your udstCourses JSON
with open("udst-courses.json") as f:
    udstCourses = json.load(f)

# Courses you want to cancel / skip next semester
cancel_list = [
    # "AEEL1102", "MATH1030"
    "EFFL1001",  # Effective Learning
    "EFFL1002",  # Applied & Experiential Learning
    "AECH1100",  # Environmental Awareness & Ethics
    "AEMA1312",  # Engineering Graphics
    "AEPC1203",  # Basic Instrumentation
    "BIOL1001",  # Inquiry-Based Biology
    "BIOL1002",  # Introduction to Botany
    "BIOL1003",  # Fundamentals of Ecology
    "AECH2103",  # Leadership & Management Principles
    "AETN2302",  # Applied Programming I
    "AECH2112",  # Sustainability & Renewable Energy
    "AETN3101",  # Cyber Security
    "AETN3201",  # Cyber Security (Lab)
    "AETN3221",  # Linux Operating System
    "AETN3222",  # Applied Programming II
    "BUSG2001",  # Introduction to Entrepreneurship
    "SSHA1001",  # Islamic & Arab Civilization
    "SSHA1002",  # Introduction to Sociology
    "SSHA1003",  # Introductory Psychology
    "SSHA1004",  # Ethical Reasoning
    "SSHA1005",  # Law & Society
    "SSHA1006",  # Introduction to the Arts
    "AETN3203",  # Work Placement
    "AEMA4100",  # Project Management
    "AETN4301",  # Capstone Project I
    "AETN4302",  # Capstone Project II
    "COMM3010",  # Research & Reporting
    ]

# Convert list to a dict for easier lookup
course_dict = {c["course_number"]: c for c in udstCourses}


# Function to check if a course can be taken
def can_take(course):
    pre_reqs = course.get("pre_req", [])
    if not pre_reqs:
        return True  # No pre-reqs
    # All pre-reqs must be attempted
    return all(course_dict[pre]["attempted"] for pre in pre_reqs if pre in course_dict)


# Find all udstCourses eligible for next semester
eligible_courses = [
    c for c in udstCourses
    if not c.get("attempted", False)
    and can_take(c)
    and c["course_number"] not in cancel_list
]

# Print eligible udstCourses
print("udstCourses you can take next semester:")
for course in eligible_courses:
    print(f"{course['course_number']}: {course['course_title']}")

# Optionally save to a file
with open("next_sem_udst-courses.json", "w") as f:
    json.dump(eligible_courses, f, indent=2)
