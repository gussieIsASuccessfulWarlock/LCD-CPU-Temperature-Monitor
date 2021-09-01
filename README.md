# LCD-CPU-Temperature-Monitor
Central Prossing Unit Thermometer (C.P.U.T.)

<h2>What you will need</h2>
<ul>
  <li>Raspberry PI</li>
  <li>LCD Screen</li>
  <li>Breadboard</li>
  <li>Jumper Cables</li>
</ul>
<h2>What does this do</h2>
<p>This program will allow you to monitor the temperature of your C.P.U. in fahrenheit and celsius from an LCD screen.</p>

<h1>Setup</h1>
<p> </p>
<p> </p>
<p> </p>
<h2>Step 1:</h2>
<h3>Configure Settings</h3>
<p>Open the terminal window and type:</p> <code>sudo su</code> <p></p> <code>raspi-config</code> <p></p> <p>This will open configuration settings on the Raspberry PI.</p>

<img width="2560" alt="Screen Shot 2021-08-30 at 8 11 43 PM" src="https://user-images.githubusercontent.com/82612866/131427096-a1215079-d75c-4e38-8adf-aede3b1b2e51.png">

<p>Select interface options and then I2C</p>

<img width="2560" alt="Screen Shot 2021-08-30 at 8 12 13 PM" src="https://user-images.githubusercontent.com/82612866/131427338-f9530e05-c44a-472c-8724-a6cdd6b1f331.png">

<p>Once selected, enable it, and then exit the configuration settings on the Raspberry PI.</p>

<img width="2560" alt="Screen Shot 2021-08-30 at 8 12 19 PM" src="https://user-images.githubusercontent.com/82612866/131427442-1c394ffe-45d4-4fea-9dc7-44f431218099.png">



<h2>Step 2:</h2>

<h3>Plug-in LCD Screen</h3>

![_EKS5017](https://user-images.githubusercontent.com/82612866/131503423-afa3708c-dda0-414b-a135-bf9f4d3a5b3c.jpg)


![Diagram](https://user-images.githubusercontent.com/82612866/131503273-0c9fc9d0-4bcd-4557-ac07-ed67c2eea853.png)



<h2>Step 3:</h2>

<h3>Install Needed Libraries</h3>

<p>Type in the terminal:</p> <code>sudo pip3 install rpi_lcd</code> <p></p> <p>once done installing, type: i2cdetect -y one will give you the hardware address of your LCD.</p> <p>Now type:</p> <code>cd /usr/local/lib/python3.7/dist-packages/rpi_lcd</code> <p></p> <p>once done type</p> <code>sudo nano __init__.py</code> <p></p> <p>and change the address in the config file (image below).</p>

<img width="2560" alt="image" src="https://user-images.githubusercontent.com/82612866/131504788-16ba63ee-7842-49a6-adb8-360c8d9e9b14.png">



<h2>Step 4:</h2>
<h3>Install the script</h3>
<p>Click install and move the python script called cput.py to your home directory. 
<code>sudo mv cut.py /~</code> 
<p>Then type in your terminal:</p> 
<p></p>
<code>sudo chmod u+x cput.py</code>


<h2>Step 5:</h2>
<h3>Run The Script</h3>
<p>Type in the terminal</p> <code>./cput.py</code>
