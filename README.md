# Movie-Trailer-Project

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree).
This projects demonstrates the simple usage of classes in order to build a movie trailer website.


## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Quick start](#quick-start)

## Demo
For a demo, click on <http://mvppoa.github.io/ud036_StarterCode/fresh_tomatoes.html>!

## Download
The files for the project, may be [downloaded here](https://github.com/mvppoa/ud036_StarterCode/archive/master.zip).

## Quick Start

After downloading the project files, a movie trailer page can be run not_so_roten_tomatoes.py
(https://github.com/mvppoa/ud036_StarterCode/blob/master/not_so_roten_tomatoes.py) in order
to start load up a page with three movies. Alter the file to manipulate the page content.

```
from media.classification_enum import ClassificationEnum
from media.movie import Movie
from web_page.fresh_tomatoes import FreshTomatoes

# Simple web page created to demo the movie site
# Instead of using fresh_tomatoes file as the main file, I created a class for it in order to be easy to read.
# Here te movies will be loaded and the web page will be created an opened. Movie class have a few more attributes
# if the developer wants to display more info in the web page.

movie_list = []

movie_goon_last_enforcer = Movie("GOON: LAST OF THE ENFORCERS",
                                 "1h30m",
                                 ClassificationEnum.R,
                                 "After one too many injuries, hockey enforcer Doug Glatt (Seann William Scott) is forced to give up his aspirations of going to the big show and settle into a buttoned down career as an insurance salesman at the urging of his pregnant wife Eva (Alison Pill). However, Doug can't resist the siren call of the Highlanders, so he sets course to reclaim his former glory.",
                                 "https://resizing.flixster.com/KKm9T_kpGlIxyaj7auuS14l4uHc=/206x305/v1.bTsxMjQ2MTEyODtqOzE3NDY5OzEyMDA7MTM4MjsyMDQ4",
                                 "https://www.youtube.com/watch?v=ch1_SliHPbE")

movie_death_note = Movie("Death Note (2017)",
                         "1h30m",
                         ClassificationEnum.R,
                         "Light Turner, a bright student who stumbles across a mystical notebook that has the power to kill any person whose name he writes in it. Light decides to launch a secret crusade to rid the streets of criminals. Soon, the student-turned-vigilante finds himself pursued by a famous detective known only by the alias L.",
                         "https://resizing.flixster.com/l5D4QP0lrM_KVH3UkRAbBABiQ-A=/206x305/v1.bTsxMjQ0MTQwMTtqOzE3NDY4OzEyMDA7MTgwMDsyNzAw",
                         "https://www.youtube.com/watch?v=R0BaQa0VNKk")

movie_kill_switch = Movie("KILL SWITCH",
                          "1h30m",
                          ClassificationEnum.R,
                          "Acclaimed writer-director Tim Smit explodes on to the scene with his futuristic, VFX-heavy feature debut! KILL SWITCH charts the story of a pilot battling to save his family and the planet, based on Smit's short What's In The Box? Set in a future version of the world, the video game style plot follows an experiment for unlimited energy, harnessing parallel universes, which goes wrong. Chased by drones and soldiers, pilot and physicist Will Porter must race through an imploding world to get the Redivider box to a tower, which ",
                          "https://resizing.flixster.com/EePJbMeZH6j6fJi829NVL5kI8BQ=/206x305/v1.bTsxMjM5ODAzMjtqOzE3NDY4OzEyMDA7ODY0OzEyODA",
                          "https://www.youtube.com/watch?v=SernjeZIsM8")

movie_list.append(movie_goon_last_enforcer)
movie_list.append(movie_death_note)
movie_list.append(movie_kill_switch)

fresh_tomatoes = FreshTomatoes()
fresh_tomatoes.open_movies_page(movie_list)

```

