import kivy
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

#App Version
__version__="00.04.05"

# window size
Wfac=3
WindowWidth= (40-Wfac)*9
WindowHeight= (40-Wfac)*19.5
Window.size=(dp(WindowWidth), dp(WindowHeight))

#other requirements
import csv
import random
import pyttsx3
# import speech_recognition as sr
import time

about_content='''This interactive application has been developed as a project for the ATL Space Challenge 2021 which ranges from quizzes, rapid fire rounds to interesting space and planets facts.
The theme of this project is “Explore Space” and the subtopic is “App Development – Create an App to raise awareness about space and the outer world.”
We have made this application as user - friendly as possible, so there’s no need for the user to have formal knowledge, in order to explore it to its fullest.'''

howtoplay_content='''Three modes:
    1.) Space Quiz

        - An interactive and competetive game mode where you will be getting 5 questions per round ( 5 rounds in one game, you can restart the game mode to play again after 5 rounds)
        - No Time Limit.

    2.) Rapid Fire based on Quiz questions.

        - Also an interactive but more competetive game mode with 5 questions per round ( 5 rounds in one game, you can restart the game mode to play again after 5 rounds)
        - 10 seconds to answer each question, if not answered in time you will get no score.
        - It is a One-Time Click game mode so you can't click the options multiple times .

    3.) Facts about Space.

        - Totally different game mode from the other two, this game is just for fun and to gather some knowledge about space bodies through random Space Facts.
        - You can also find facts for specific Planets in our Solar System.'''

info_content='''This application has been developed with the teamwork of three students (Team VAY) of class 12th from Science stream in Banasthali Public School, session 2021-22; namely:

    -> Vishesh Sharma
    -> Anshuman Khatri
    -> Yugam Sehgal'''

ques_content='''Q NO.,Question,Option 1,Option 2,Option 3,Option 4,Answer
1,Which is the smallest planet in our solar system?,Mercury,Uranus,Mars,Venus,Mercury
2,Which is the second smallest planet in our solar system?,Neptune,Mercury,Venus,Mars,Mars
3,"The moon called ""Titan"" orbits which planet?",Saturn,Jupiter,Venus,Mars,Saturn
4,Which is the brightest planet in the night's sky?,Neptune,Mercury,Jupiter,Venus,Venus
5,Name the largest planet of our solar system.,Uranus,Saturn,Jupiter,Neptune,Jupiter
6,Uranus has only been visited by which spacecraft?,Curiosity,The Voyager 2,Sputnik 1,The Voyager 1,The Voyager 2
7,Which is the only planet not named after Greek gods or goddesses?,Neptune,Earth,Saturn,Jupiter,Earth
8,There have been more missions to this planet versus any other planet. Which planet is it?,Mercury,Venus,Mars,Jupiter,Mars
9,Which planet has maximum number of most moons?,Saturn,Jupiter,Uranus,Neptune,Saturn
10,Which planet has the fastest rotation?,Neptune,Mercury,Jupiter,Venus,Jupiter
11,How long is a single Earth year on Jupiter?,12,8,2,15,12
12,What phenomena keeps the planets in steady orbit around the sun?,Spaghettification,Solar winds,Vacuum of space,Gravity,Gravity
13,Which is the largest star within our solar system?,Sun,Moon,Sirius,Polaris,Sun
14,How many stars are in the Milky Way?,More than 2 million,More than 20 million,More than 10 billion,More than 100 billion,More than 100 billion
15,How old is the sun approximately?,4 Billion,4.6 Billion,6 Billion,6.2 Billion,4.6 Billion
16,How long does the sun rays take to reach Earth in minutes?,10,8,12,15,8
17,How long does a solar eclipse last in minutes?,10,6.5,7.5,5,7.5
18,Where is the Asteroid Belt located?,Between Mars and Jupiter,Between Venus and Mercury,Between Uranus and Neptune,Between Saturn and Jupiter,Between Mars and Jupiter
19,What color is Mars's sunset?,Red,Pink,Blue,White,Blue
20,Name the spacecraft that carried the first astronauts to the moon,Apollo 11,The Voyager 2,Sputnik 1,The Voyager 1,Apollo 11
21,How much of the universe is composed of dark matter?,0.10%,5%,27%,55%,27%
22,Currently how many moons are in our solar system?,95,125,181,2,181
23,What has an incredibly strong gravitational pull that light can't even escape?,Sun,Stars,Black Hole,Nebula,Black Hole
24,Who was the first person to step on moon?,Buzz Aldrin,Neil Armstrong,Michael Collins,Rick Astley,Neil Armstrong
25,How old is the universe (in billion years)?,20.5,10.4,16.2,13.8,13.8
26,How is the distance between the sun and Earth measured?,Kilometres,Light Years,Miles,Astronomical Units,Astronomical Units
27,What protects Earth from meteoroids and radiation from the sun?,Magnetic Field,Clouds,Atmosphere,Orbit,Atmosphere
28,How many planets of solar system can be seen without telescope?,2,5,4,3,5
29,Which planet is closest in size to Earth?,Mercury,Venus,Mars,Neptune,Venus
30,Which is the oldest planet in our solar system?,Saturn,Mars,Jupiter,Uranus,Jupiter
31,Which Earth sized planet is largely made up of diamonds?,Proxima 1,A Centauri,Sirius A,55 Cancri e,55 Cancri e
32,Name the first human spacecraft sent into space?,Apollo 11,Apollo 13,Vostok 1,Vostok 2,Vostok 1
33,Who made the first human spacecraft?,Rick Astley,Ferdinand Magellan,Gallelio Galleli,Issac Newton,Ferdinand Magellan
34,When did the first human landed on moon?,14-Jan-87,10-May-98,23-Nov-56,20-Jul-69,20-Jul-69
35,How old is Earth in billion years?,1.12,2.51,4.54,25.56,4.54
36,How wide is our Solar System in billion kms?,123.87,52.12,504.78,287.46,287.46'''

fact_content='''Random Facts,Sun,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune
Uranus is tilted on its side.,Sun takes up 99.86% of the mass in Solar System!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
"Jupiter's moon named ""Io"" has towering volcanic eruptions.",Sun is giant gas ball composed of hydrogen and helium.,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
"Mars has the biggest volcano (that we know of) namely, Olympus Mons.","Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
Mars also has the longest valley Valles Marineris.,The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
"Venus has super-powerful winds, reaching 360kmph or 224mph!!",Sun takes up 99.86% of the mass in Solar System!,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
"The biggest star known in universe is UY Scuti, with a radius around 1,700 times larger than the sun!",Sun is giant gas ball composed of hydrogen and helium.,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
An Spacecraft have visited each and every planet in our Solar System.,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
The largest blackhole Ton 618 has a mass of 66 million times of the Sun!!,The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
Mercury's core is constantly shrinking in size.,Sun takes up 99.86% of the mass in Solar System!,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
Pluto is the only place after Earth which has white peaked mountain.,Sun is giant gas ball composed of hydrogen and helium.,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
Footprints of humans on the moon will stay for millions of years due to absence of atmosphere on it.,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
Some planets do not even have a surface to land on!,The Sun is big enough to fit 1.3 million Earth inside it!!,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
"Pieces of the same metal will permanently merge in space, this phenomena is known as cold welding.",Sun takes up 99.86% of the mass in Solar System!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
There are interstellar objects passing through our solar system.,Sun is giant gas ball composed of hydrogen and helium.,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
"Saturn is composed of gases, making it less dense than water, hence making it float on it!","Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
"Jupiter has the most moons in our solar system, with a total of 79 moons.",The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
The hottest planet in our solar system aka Venus reaches upto 450° C!,Sun takes up 99.86% of the mass in Solar System!,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
Halley's comet passes through Earth's vicinity every 75 years.,Sun is giant gas ball composed of hydrogen and helium.,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
Neutron stars can spin upto 600 times per second.,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
1 day on Venus is longer than 1 Earthly year.,The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
In 3.75 billion years the Milky Way and Andromeda galaxies will collide.,Sun takes up 99.86% of the mass in Solar System!,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
Largest known asteroid is 965 km wide.,Sun is giant gas ball composed of hydrogen and helium.,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
The Sun's mass takes up 99.86% of the solar system!,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
A volcano on Mars is 3 times the size of Mt.Everest.,The Sun is big enough to fit 1.3 million Earth inside it!!,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
It would take 9.5 years to walk to the Moon.,Sun takes up 99.86% of the mass in Solar System!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
Temperature of outer space is close to absolute zero.,Sun is giant gas ball composed of hydrogen and helium.,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
Around 6000 satellites are currently orbiting our Earth!!,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
There are more stars in the Universe than grains of sands on Earth!,The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
Sunset on Mars appears Blue.,Sun takes up 99.86% of the mass in Solar System!,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
"Space X launched the first privately funded liquid-propellant rocket to reach the orbit, namely Falcon 1.",Sun is giant gas ball composed of hydrogen and helium.,Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
Humanity have found around 60 potentially habitable exoplanets as of 2021,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
The nearest habitable planet is estimated to be 12 light years away,The Sun is big enough to fit 1.3 million Earth inside it!!,Mercury's core is constantly shrinking in size.,Venus is the brightest and second closest planet to the Sun.,"71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
NASA's first mission to demonstrate a planetary defense system is called DART.,Sun takes up 99.86% of the mass in Solar System!,Mercury is the smallest and closest planet to the Sun.,Venus is the brightest and second closest planet to the Sun.,"Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.
"The full form of NASA's defense system DART is ""Double Asteroid Redirection Test"".",Sun is giant gas ball composed of hydrogen and helium.,Mercury's core is constantly shrinking in size.,"Venus's atmosphere is 96% all carbondioxide, with no water on it's surface, creating a greenhouse effect.",Earth is the only habitable and third closest planet to the Sun which we live on.,Mars also known as the red planet is the fourth closest planet to the Sun.,Jupiter is the largest and fifth closest planet to the Sun.,Saturn also known as the ring planet is the sixth closest to the Sun.,Uranus is the seventh from planet to the Sun.,Neptune is the coldest and eight planet from the Sun.
The oldest known exoplanet in the universe is PSR B12620-26 b with an age of 13  billion years!!,"Sun is 149.48 million kms away from Earth, this distance is also known as the Astronomical Unit (A.U.)",Your weight on Mercury would be 38% of your weight on Earth.,"Venus's dense atmosphere traps heat, making it the hottest planet, hence the temperature reaching upto 450° C!","71% of the Earth's surface is covered with water, which only 3% of it is drinkable!",Shockingly there is water found on Mars in frozen form i.e. ice.,"Jupiter is 650.29 million km away from Earth, and is large enough to fit 1,300 Earths inside it!!",Saturn's ring isn't solid infact it's made up of millions of tiny particles such as ice and rocks held together by it's strong gravity!,Uranus's axis is so tilted ( almost 98° ) it appears to be rotating on its side.,Neptune being the coldest planet in our Solar System can go as low as -391° C or -671.8° F!!
,,,,"Earth's gravity and it's shape isn't uniform, more like an irregularly shaped ellipsoid.",The iron rich minerals present on Mars's surface is what gives it the red colour!,"Jupiter is the fastest spinning planet, and it's magnetic field is 14 times stronger than Earths.",Saturn is the most distant planet which can be seen by naked eye!,"Uranus is one of the coldest planet, with temperature hitting as low as -188.3° C or -370.94° F!",Neptune appears blue to eyes due to absorption of red and infrared light by it's methane atmosphere.'''

try:
    ques_file=open("questions.csv")
    read_ques_file=csv.reader(ques_file)
except FileNotFoundError:    
    ques_file=open("questions.csv","w+")
    ques_file.write(ques_content)
    ques_file.close()
    ques_file=open("questions.csv")
    read_ques_file=csv.reader(ques_file)

try:
    fact_file=open("facts.csv")
    read_facts_file=csv.reader(fact_file)
except FileNotFoundError:
    fact_file=open("facts.txt","w+")
    fact_file.write(fact_content)
    fact_file.close()
    fact_file=open("facts.txt")
    read_facts_file=csv.reader(fact_file)

ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)
r=random.randint(0,len(ques)-1)
loopques=[]

facts=[]
for fact in read_facts_file:
    facts.append(fact)
rf=random.randint(1,len(facts)-1)
loopfact=[]

class Home(Screen):
    pass

# class Setting(Screen):
#     pass

class Info(Screen):
    infos = StringProperty(f"{info_content}")
    aboutctfapp=StringProperty(f"{about_content}")
    howtoplayctfapp=StringProperty(f"{howtoplay_content}")

class GameMode(Screen):
    pass

class Quiz(Screen, object):
    global ques
    global loopques
    global r
    
    if len(ques)==1:
        for i in range(len(loopques)):
            ques.insert(1, loopques.pop(i))

    #default vals
    Quiz_Score = StringProperty("0")
    SCORE=0
    check=StringProperty("")
    ques_no=1

    #variables    
    ans=StringProperty("false")
    nexttohome=StringProperty("Next")
    quizcheck=StringProperty("")
    roundnum=StringProperty("1")
    
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question_number=StringProperty(f"{int(ques_no)}")
    question=StringProperty(f"{ques[r][1]}")
    answer=StringProperty(f"{ques[r][6]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
    talkquestion=f"Question {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
    
    # removing the used ques for this quiz
    loopques.insert(0, ques.pop(r))

    def start_quiz_ques(self, buttonnext, buttonhome):
        global ques
        global loopques
        global r

        self.ids.btnquizcheck.disabled=True
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False

        if len(ques)==1:
            for i in range(len(loopques)):
                ques.insert(1, loopques.pop(i))

        #functions
        self.ques_no+=1
        r=random.randint(1,len(ques)-1)
        self.ans1,self.ans2,self.ans3,self.ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
        self.question_number=f"{self.ques_no}"
        self.question=f"{ques[r][1]}"
        self.answer=ques[r][6]
        self.opt1=f"1.    {ques[r][2]}"
        self.opt2=f"2.    {ques[r][3]}"
        self.opt3=f"3.    {ques[r][4]}"
        self.opt4=f"4.    {ques[r][5]}"
        self.talkquestion=f"\nQuestion {str(self.ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
        self.quizcheck=""
        
        # removing the used ques for this quiz
        loopques.insert(0, ques.pop(r))

        # if self.ques_no==1:
        #     self.Quiz_Score="0"
        if self.ques_no==5:
            self.ques_no=0
            buttonnext.bind(on_release=self.gotoresult)

        if self.ques_no==1:
            self.roundnum=str(int(self.roundnum)+1)
        
        if self.roundnum=="6":
            self.roundnum="1"
            # buttonnext.bind(on_state=self.resultbutton,on_release=self.gotoresult)
        # if self.ques_no==4:
        #     buttonnext.disabled = False
        #     self.ids.imagenextquiz.source = "images/buttons/resultdark.png"
        
        self.ids.btnquiznextques.disabled=True
    
    # def resultbutton(self):
    #     if self.ids.btnquiznextques.state == "down":
    #         self.ids.imagenextquiz.source = "images/buttons/resultlight.png"
    #     else:
    #         self.ids.imagenextquiz.source = "images/buttons/resultdark.png"

    def gotoresult(self, quiznextparent):
        self.parent.current = "quizresult"
        self.ids.btnquiznextques.unbind(on_release=self.gotoresult)

    def inputA(self, button):
        if self.ans1==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
    
    def inputB(self, button):
        if self.ans2==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"

    def inputC(self, button):
        if self.ans3==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
            
    def inputD(self, button):
        if self.ans4==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"

    def check_quiz_ans(self):

        if self.ans=="true":
            Quiz.SCORE += 1
            self.Quiz_Score = str(int(self.Quiz_Score) + 1)
            self.quizcheck="Your Answer is Correct!!"
        else:
            self.quizcheck=f"Your answer is wrong!\nCorrect answer: {self.answer}."
        
        self.ids.btnquizcheck.disabled=True
        self.ids.btnopt1.disabled=True
        self.ids.btnopt2.disabled=True
        self.ids.btnopt3.disabled=True
        self.ids.btnopt4.disabled=True

        self.ids.btnquiznextques.disabled=False

    def exitquiz(self):
        self.ids.btnquiznextques.disabled=True
        
        self.ids.btnquizcheck.disabled=True
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False
        self.quizcheck=""

        self.ques_no=1
        self.Quiz_Score = "0"
        self.question_number=f"{self.ques_no}"

class RapidFire(Screen, object):
    global ques
    global loopques
    global r
    
    if len(ques)==1:
        for i in range(len(loopques)):
            ques.insert(1, loopques.pop(i))

    #default vals
    Rapid_Score = StringProperty("0")
    SCORE=0
    check=StringProperty("")
    ques_no=1

    #variables    
    ans=StringProperty("false")
    nexttohome=StringProperty("Next")
    rapidcheck=StringProperty("")
    timervar=StringProperty("10")
    roundnum=StringProperty("1")

    timercountdown=ObjectProperty()

    
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question_number=StringProperty(f"{int(ques_no)}")
    question=StringProperty(f"{ques[r][1]}")
    answer=StringProperty(f"{ques[r][6]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
    talkquestion=f"Question {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
    
    # removing the used ques for this rapid fire
    loopques.insert(0, ques.pop(r))
    

    # def __init__(self, **kwargs):
#         super(RapidFire, self).__init__(**kwargs)
#         self.timercountdown = Clock.schedule_interval(self.countdown, 1)
    # def start_timer(self):
    #     return self.timer()
    # def end_timer(self):
    #     return self.timerrapid
    def timer(self):
        self.timercountdown = Clock.schedule_interval(self.countdown, 1)
        self.timerstoper = Clock.schedule_once(self.timerrapid, 10)

    def countdown(self, *args):
        self.ids.counter.text=str(int(self.ids.counter.text)-1)

    def timerrapid(self, *args):
        self.timercountdown.cancel()
        self.ans="false"
        self.check_rapid_ans()

    def start_rapid_ques(self, buttonnext, buttonhome):
        self.ids.counter.text="10"
        

        # def timer(self):
        #     self.timercountdown = Clock.schedule_interval(countdown, 1)
        #     Clock.schedule_once(timerrapid, 10)

        # def countdown(self, *args):
        #     self.root.ids.counter.text=str(int(self.root.ids.counter.text)-1)

        # def timerrapid(self, *args):
        #     self.timercountdown.cancel()    
        #     RapidFire.check_rapid_ans()

        

        # timer()
        # Clock.schedule_interval(self.countdown, 1)
        

        
        # self.timercountdown = Clock.schedule_interval(RapidFire.countdown, 1)
        # Clock.schedule_once(RapidFire.timerrapid, 10)    
        
        # self.timercountdown = Clock.schedule_interval(self.countdown, 1)
        # Clock.schedule_once(self.timerrapid, 10)

        global ques
        global loopques
        global r

        # self.ids.btnrapidcheck.disabled=True
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False

        if len(ques)==1:
            for i in range(len(loopques)):
                ques.insert(1, loopques.pop(i))

        #functions
        self.ques_no+=1
        r=random.randint(1,len(ques)-1)
        self.ans1,self.ans2,self.ans3,self.ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
        self.question_number=f"{self.ques_no}"
        self.question=f"{ques[r][1]}"
        self.answer=ques[r][6]
        self.opt1=f"1.    {ques[r][2]}"
        self.opt2=f"2.    {ques[r][3]}"
        self.opt3=f"3.    {ques[r][4]}"
        self.opt4=f"4.    {ques[r][5]}"
        self.talkquestion=f"\nQuestion {str(self.ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
        self.rapidcheck=""

        loopques.insert(0, ques.pop(r))

        if self.ques_no==5:
            self.ques_no=0
            # self.roundnum=str(int(self.roundnum)+1)
            buttonnext.bind(on_release=self.gotoresult)
        
        if self.ques_no==1:
            self.roundnum=str(int(self.roundnum)+1)
        
        if self.roundnum=="6":
            self.roundnum="1"

        self.ids.btnrapidnextques.disabled=True

    def gotoresult(self, rapidnextparent):
        self.parent.current = "rapidresult"
        self.ids.btnrapidnextques.unbind(on_release=self.gotoresult)

    def inputA(self, button):
        if self.ans1==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
    
    def inputB(self, button):
        if self.ans2==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"

    def inputC(self, button):
        if self.ans3==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
            
    def inputD(self, button):
        if self.ans4==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"

    def check_rapid_ans(self):

        if self.ans=="true":
            RapidFire.SCORE += 1
            self.Rapid_Score = str(int(self.Rapid_Score) + 1)
            self.rapidcheck="Your Answer is Correct!!"
        else:
            self.rapidcheck=f"Your answer is wrong!\nCorrect answer: {self.answer}."
        
        self.ids.btnopt1.disabled=True
        self.ids.btnopt2.disabled=True
        self.ids.btnopt3.disabled=True
        self.ids.btnopt4.disabled=True

        self.ids.btnrapidnextques.disabled=False

    def exitrapid(self):
        self.ids.btnrapidnextques.disabled=True
        
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False
        self.rapidcheck=""

        self.ques_no=1
        self.Rapid_Score = "0"
        self.question_number=f"{self.ques_no}"

class Facts(Screen):
    global facts
    global loopfact
    global rf
    
    if len(facts)==0:
        for i in range(len(loopfact)):
            facts.insert(1, loopfact.pop(i))

    rf=random.randint(1,len(facts)-1)
    fact=StringProperty(f"Click on the button below to load a space fact.")
    # morefact=StringProperty("Click For Space Facts")
    diduno=StringProperty("")
    
    loopfact.insert(1, facts.pop(rf))

    optionchose=0
    planetimage="random"

    def ChooseOption(self):
        if self.ids.chooseplanets.text=="Random Space Facts":
            self.optionchose=0
            self.planetimage="random"
        if self.ids.chooseplanets.text=="Sun":
            self.optionchose=1
            self.planetimage="sun"
        if self.ids.chooseplanets.text=="Mercury":
            self.optionchose=2
            self.planetimage="mercury"
        if self.ids.chooseplanets.text=="Venus":
            self.optionchose=3
            self.planetimage="venus"
        if self.ids.chooseplanets.text=="Earth":
            self.optionchose=4
            self.planetimage="earth"
        if self.ids.chooseplanets.text=="Mars":
            self.optionchose=5
            self.planetimage="mars"
        if self.ids.chooseplanets.text=="Jupiter":
            self.optionchose=6
            self.planetimage="jupiter"
        if self.ids.chooseplanets.text=="Saturn":
            self.optionchose=7
            self.planetimage="saturn"
        if self.ids.chooseplanets.text=="Uranus":
            self.optionchose=8
            self.planetimage="uranus"
        if self.ids.chooseplanets.text=="Neptune":
            self.optionchose=9
            self.planetimage="neptune"

    def show_more_facts(self, button):
        global facts
        global loopfact
        global rf
        
        if len(facts)==0:
            for i in range(len(loopfact)):
                facts.insert(1, loopfact.pop(i))
        
        rf=random.randint(1,len(facts)-1)
        self.fact=f"{facts[rf][self.optionchose]}"
        # self.morefact="One More Fact"

        self.diduno="DID YOU KNOW?"

        loopfact.insert(1, facts.pop(rf))\
    
    factimage=StringProperty("")

    def buttonmorefacts(self, button):

        self.factimage=f"images/planet_img/{self.planetimage}.png"


        if self.ids.imagemorefacts.source=="images/buttons/loadfactdark.png":
            self.ids.imagemorefacts.source="images/buttons/loadfactlight.png"# if button.state == "down" else "images/buttons/loadfactdark.png"
        
        if self.ids.imagemorefacts.source=="images/buttons/loadfactlight.png":
            self.ids.imagemorefacts.source="images/buttons/loadfactdark.png"

    #this color animation is not yet fixed
        


class QuizResult(Quiz, Screen):
    # if __name__=="__main__":
    #     Quiz.SCORE=int(str(Quiz.Quiz_Score))
    
    # quizclass=Quiz()
    # print(quizclass.SCORE)

    
    finalquizscore=StringProperty(f"{Quiz.SCORE}")

class RapidResult(RapidFire, Screen):
    finalrapidscore=StringProperty(f"{RapidFire.SCORE}")
    
    # def result(self):
    #     # self.finalrapidscore = RapidFire.SCORE
    #     return RapidFire.SCORE

class WindowManager(ScreenManager):
    pass

#misc requirements
class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))



class CTFApp(App):

    windowwidth= StringProperty(str(int(dp(WindowWidth))))
    windowheight = StringProperty(str(int(dp(WindowHeight))))
    
    def build(self):
        kvfile = Builder.load_file("mymain.kv")
        self.title="CTF - Cosmos Trivia and Facts"
        self.icon="images/appicon.ico"
        return kvfile
    
    #tts func to make our program say something
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 178)

    def talk(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    appversion=StringProperty(f"{__version__}")

if __name__ == "__main__":
    CTFApp().run()
