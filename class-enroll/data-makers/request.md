I am gonna provide a list of available courses.

## Schedule Requirements

I want a schedule for one college student where:

### Mandatory

- My schedule should be as **congested as possible** outside of the above constraints.
- i can only pick one instructor and a section or 2 sections (lecture section and lab lecture section) for a course
    - a course can have single section (lecture section only) or 2 sections (lecture section and lab lecture section)
- I want good instructors no matter how much time i sacrifice for them

### Optional

- My classes are **mostly** on **Sunday, Tuesday, and Thursday** (preferred but not mandatory).
- My **desired start time** is **8 AM**.
- I have **no preference for an ending time**.
- if days off can be had at expense of more time in other days, then that is acceptable.

## Data to be provided maker rules

> Note: This section is only for the clarity of the AI processor to understand data

The data to be provided by me have been formatted according to a set of rules. They are given below:

---

give me available course classes in markdown code block the format:

```markdown
| Class ID | Days and Times | Room | Instructor | Status |
```

a subject is of format `XXXX ****`. Here X stands for any alphabet while * stands for any number

subjects contain multiple courses

a single course includes one or 2 sections. if it has 2 sections, it will be a Lecture type session and a LecTheatre type session. If it has one section, it will only have a Lecture type session.

more than one course cannot be chosen for one subject.

Here Class ID is something like: Lecture - Class 1295 -Section 1

use html in between .md, <br> for line breaks and <hr> to show line breaks, to split lines. do that with days and times. use additional html tags where necessary to keep structure (not design). use md tables. also for Days and Times,	Room	Instructor, make sure they are aligned accordingly when multiple is given

i dont want this type of info:
- AEEL 1102 - Fundamentals of Electricity II
  04/05/2025 - 26/06/2025

For the open seats: format -> 'open/closed (?-?)' where ? is some number according to data and open or closed is used depending on the given or data

Here is an example output with nonsense data. dont use this data

```markdown
| Class ID | Days and Times | Room | Instructor | Status |
|---|---|---|---|---|
| AEEL 1102-4   | Tuesday 12:00PM to 2:00PM<br>Thursday 12:00PM to 2:00PM<br>Sunday 12:00PM to 2:00PM | 05.2.35| Yoosaf Vannarath        | open (8-30)  |
```

use the following data

```random text copied by select all in a website

```

---

## Schedule Format

give the schedule in the same format as the data provided, that is:

```markdown
| Class ID | Days and Times | Room | Instructor | Status |
```

give output table in code block


Here is an example output with nonsense data. dont use this data

```markdown
| Class ID | Days and Times | Room | Instructor | Status |
|---|---|---|---|---|
| AEEL 1102-4   | Tuesday 12:00PM to 2:00PM<br>Thursday 12:00PM to 2:00PM<br>Sunday 12:00PM to 2:00PM | 05.2.35| Yoosaf Vannarath        | open (8-30)  |
```

Remember i want the course code for each listing

Class ID should be like this `XXXX ****-<* or (*,*)>`. Example:

- `COMM 1020-2`, where `2` stands for lecture section number for single section courses
- `COMM 1020-(2,3)`, where `2` stands for lecture section and `3` stands for theatre section

---

#### Provide the schedule using the following data:

