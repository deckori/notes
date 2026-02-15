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


