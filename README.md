# Python Final 2022

The team members working on this project are Ricky, Colin, and Joe. 

The idea for our project is to create a program that can play music and songs using an external music package. <br />
We are planning on using pycharm to program and share the code in live time. <br />
We are also going to be using GitHub to share the code with each other when we are working on it, <br />
not at the same time, and to more easily access it from different computers. <br />
<br />
The safe goal for our project is to create a program that will play different songs from a pre-programmed list <br />
of songs. Our stretch goal will be to make it so we can use our keyboard like a piano and save that as <br />
a song that can be played back as well as add a way to import different songs through an imported <br />
file and put them into a list.
<br />

- What types of packages we will need to make this program 
- Create and share a common project for all members to work on and pull from 
- Find out the API and what functions the package(s) offer 
- Create the different files and folders we will need while continuing to document our changes 
- Create utility functions 
- Create music-related functions using the API 
- Populate a list of songs the user can pick from 
- Find ways to allow users to import their files into the program 
- Create an interface that shows a piano with its keymap 
- Get the keys pressed input to play music like its a piano 
- Find way to save the inputted keys into a file and/or list for future use

<br />
<br />

# How to setup a song file
- First you must have the song name, instrument, key and time sig on the first line
  - Ex: "test song 1","piano","c","2/4"
- Then on the following lines you can have the note and length in seconds held for
  - Ex: "a",1.5
- An example file will look like<br />
  "test song 1","piano","c","2/4"<br />
  "a",1.5<br />
  "b",2.5<br />
  "c",3.5<br />
  "d",4.5<br />
  "e",5.5<br />
  "f",6.5