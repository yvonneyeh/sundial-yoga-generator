

# **Sundial**
### Created by Jen Brissman, Ilana Rose Mercer, Rachel Perkins, Yvonne Yeh (A.K.A. **The Lovalace Ladies**)

*Sundial* is a web app for yoga students, teachers, and enthusiasts that allows a user to create custom yoga sequences. Users can also generate random sequences of varying lengths, and save all sequences to their library of yoga "playlists". :sun_with_face: 

## **Tech Stack**
**Front-end**: React, CSS, HTML </br>
**Back-end**: Python, Flask, SQLAlchemy, CockroachDB </br>
**APIs**: Yoga API by Rebecca G. Estes with expanded data set from the creators and friendly yoga teachers

## About the project


Yvonne was initially inspired to create such an app long ago while working as a yoga instructor, and her proposal was supported by our whole group (the Lovelace Ladies) as a way to provide a free, easy way to create yoga sequences. Yoga is an essential tool for the mental and physical health of many, and we felt that it was important for anyone to have free access to these sequences, and the ability to start customizing one's own personal health care. 

we learned: We all learned how to delegate, 
how was it built: 
challenges

## **Setup/Installation**

#### **Requirements**
* PostgreSQL
* Python 3.7.3

#### **Clone this repository**
```bash
git clone https://github.com/yvonneyeh/HackOR-Lovelace-Ladies.git
```
#### **Create a virtual environment**
``` bash
virtualenv env
```
#### **Activate the virtual environment**
``` bash
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

``` bash
(env) $ python3 -i model.py
>>> db.create_all()
```

#### **Start backend server**
``` bash
(env) $ python3 server.py
``` 

#### **Run the frontend server**
``` bash
(env) npm start
```


## **About the Lovelace Ladies**

#### **Jen Brissman**:
A tenacious multi-hyphenate, Jen is an NYC based theatre, tv, film, voiceover, commercial actress and model, and a senior operations manager, a professional organizer, and lifestyle manager. She is thrilled about her new venture into the world of software engineering. In her free time, she is an adventurous world traveler who enjoys mountain biking, snowboarding, running, scuba diving, and is happiest in hiking boots. Her most recent work includes recording demo videos/recordings for prominent software companies." [*LinkedIn*](https://www.linkedin.com/in/jenbrissman) | [*Github*](https://www.github.com/jenbrissman)


#### **Ilana Rose Mercer**:
Ilana Rose Mercer is a software engineer living in New York City who is passionate about leveraging technology to help improve human quality of life. Before she learned how to code and became passionate about her career in tech, she worked as a professional classical musician and private music teacher." [*LinkedIn*](https://www.linkedin.com/in/i-mercer) | [*Github*](https://www.github.com/violatido)


#### **Rachel Perkins**:
As a former high school math and yearbook teacher, Rachel took a cross country move as an opportunity to explore her interests in design and eningeering. Engineering has challenged her in all the right ways and it's hard to take her away from learning." [*LinkedIn*](https://www.linkedin.com/in/rachelelysia) | [*Github*](https://www.github.com/rachelelysia)

#### **Yvonne Yeh**:
Yvonne is a software engineer from the Silicon Valley who has never seen the show. Curiosity, creativity, and a love of learning are at the root of everything Yvonne does. She loves that coding because it is artful – there are infinite ways to code a program! Before she learned how to code, she worked in K-12 education, design, and mental/physical fitness. [*LinkedIn*](https://www.linkedin.com/in/yvonneyeh) | [*Github*](https://www.github.com/yvonneyeh)