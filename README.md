<h1>Item Catalog</h1> 
This is the second project in Udacity's Full Stack Web developer Nanodegree. In this project, we 
would be developing a web application that provides a list of various items, in this case video
games, that provides a list of it and its catagories. The categories each game will be divided into are based on platforms/consoles, each game will contain the title, a brief description, as well as the year it was released.  This will be built using Flask.
<br>
<br>
<br>
<h2>Languages used</h2>
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>AJAX/Javascript (for OAUTH login)</li>
  <li>Python</li>
</ul>

<h2>Setup</h2>
For this project to run on your computer, you need: 
<ul>
  <li>Unix-Style Terminal (You can download this <a href="https://git-scm.com/downloads">Here!</a>)</li>
  <li>Vagrant (You can download this <a href="https://www.vagrantup.com/downloads.html">Here!</a></li>
  <li>Virtual Box (You can download this <a href="https://www.virtualbox.org/wiki/Downloads">Here!</a></li>
  <li>Python</li>
  </ul>

<h2>Installing and Running</h2>
First, download a Unix style terminal, vagrant and virtual box and install them.<br>
<br>
Next clone this repo, unzip and place the file into the vagrant directory. <br>
<br>
Using the Unix style terminal, navigate to the vagrant directory and launch vagrant using:<br>
vagrant up<br>
<br>
Once vagrant is up and running login using:
vagrant ssh<br>
<br>
Change the directory using:<br>
cd /vagrant<br>
<br>
The following steps are important and need to be initialized for code to work properly! <br>
<br>
Initialize the database and populate the database with the following commands: <br>
python database_setup.py<br>
python gamedatabase.py<br>
<br>
Afterwards, you can run the application with: <br>
python project.py<br>

Lastly, open your browser and go to  <a href="http://localhost:8000">http://localhost:8000</a>
