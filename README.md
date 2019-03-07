<h1>Item Catalog</h1> 
This is the second project in Udacity's Full Stack Web developer Nanodegree. In this project, we 
would be developing a web application that provides a list of various items, in this case video
games, that provides a list of it and its catagories. This will be built using Flask.
<br>
<br>

<h2>Setup</h2>
For this project to run on your computer, you need: 
<ul>
  <li>Unix-Style Terminal (You can download this <a href="https://git-scm.com/downloads">Here!</a>)</li>
  <li>Vagrant</li>
  <li>Virtual Box</li>
  <li>Python 3</li> 
  </ul>

<h2>Installing</h2>
<ol>
  <li>Install Virtual Box, Vagrant, and Unix Style Terminal</li>
  <li>Clone this repo, and unzip and place into Vagrant Directory</li>
  <li>Launch Vagrant by using:</li>
    `$vagrant up`
  <li>Once vagrant is launched, enter the following command</li>
  `$vagrant ssh`
  <li>Change the directory to `/vagrant`</li>
  `$cd/vagrant`
  <li>In order for the app to properly work, you need to initialize the database by:</li>
  `$ python database_setup.py`
  <li>You need to populate the database by using:</li>
  `$ python menus.py`
  <li>Once populated and loaded, you can launch the application using:</li>
  `$ python project.py`
  <li>Finally, open your browser and go to http://localhost:8000
