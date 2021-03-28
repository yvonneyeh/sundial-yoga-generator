# **Sundial**

### Created by Jen Brissman, Ilana Rose Mercer, Rachel Perkins, Yvonne Yeh (A.K.A. **The Lovalace Ladies**)

_Sundial_ is a web app for yoga enthusiasts that allows practitioners (teachers and students) to algorithmically generate yoga sequences at the touch of a button. Users can generate and save these sequences to use for both teaching and personal, at-home use.:sun_with_face:

## **Tech Stack**

**Front-end**: React, CSS, HTML </br>
**Back-end**: Python, Flask, SQLAlchemy, CockroachDB </br>
**APIs**: Yoga API by Rebecca G. Estes with expanded data set from the creators and friendly yoga teachers

## About the project

One of the most difficult parts of being a good yoga teacher is planning out effective yoga sequences that take into account the transitions between poses. Teachers also require deep understanding of the body, anatomy, and flow of positions when creating the sequences. An experienced registered yoga teacher, Yvonne proposed an app that plans out yoga sequences to her Hackathon team, the Lovelace Ladies. We are all passionate about mental health and wellness, and together we built Sundial.

## **Setup/Installation**

#### **Requirements**

- CockroachDB
- Python 3.7.3

#### **Clone this repository**

```bash
git clone https://github.com/yvonneyeh/HackOR-Lovelace-Ladies.git
```

#### **Create a virtual environment**

```bash
virtualenv env
```

#### **Activate the virtual environment**

```bash
source env/bin/activate
```

#### **Install the requirements**

```bash
pip3 install -r requirements.txt
```

#### **Create database VMS**

```bash
(env) $ createdb yoga
```

#### **Create database tables**

```bash
(env) $ python3 -i model.py
>>> db.create_all()
```

#### **Start backend server**

```bash
(env) $ python3 server.py
```

#### **Run the frontend server**

```bash
(env) npm start
```

## **About the Lovelace Ladies**

#### **Jen Brissman**:

Jen is an NYC based software engineer. A tenacious multi-hyphenate, she is also a theatre, tv, film, voiceover, commercial actress and model, a senior operations manager, a professional organizer, and lifestyle manager. In her free time, she is an adventurous world traveler who happiest in hiking boots and enjoys mountain biking, snowboarding, running, and scuba diving. Her most recent work includes producing demo tutorial videos and recordings for prominent software companies. [_LinkedIn_](https://www.linkedin.com/in/jenbrissman) | [_Github_](https://www.github.com/jenbrissman)

#### **Ilana Rose Mercer**:

Ilana Rose Mercer is a software engineer living in New York City who is passionate about leveraging technology to help improve human quality of life. Before she learned how to code and became passionate about her career in tech, she worked as a professional classical musician and private music teacher. [_LinkedIn_](https://www.linkedin.com/in/i-mercer) | [_Github_](https://www.github.com/violatido)

#### **Rachel Perkins**:

As a former high school math and yearbook teacher, Rachel took a cross country move as an opportunity to explore her interests in design and eningeering. Engineering has challenged her in all the right ways and it's hard to take her away from learning." [_LinkedIn_](https://www.linkedin.com/in/rachelelysia) | [_Github_](https://www.github.com/rachelelysia)

#### **Yvonne Yeh**:

Yvonne is a software engineer from the Silicon Valley who has never seen the show. Curiosity, creativity, and a love of learning are at the root of everything Yvonne does. She loves that coding because it is artful – there are infinite ways to code a program! Before she learned how to code, she worked in K-12 education, design, and mental/physical fitness. [_LinkedIn_](https://www.linkedin.com/in/yvonneyeh) | [_Github_](https://www.github.com/yvonneyeh)


