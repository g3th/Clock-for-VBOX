# Clock for Virtual Box
## Get Time Zone/Clock while in a VBOX

### What?!

When using a virtual box set up with a different time-zone due to a different IP, just run this program in a terminal to:

1) Set your local time zone
2) Run a clock in your terminal to display your real location's time, if a time zone has been set


Alternatively, just display the time in your chosen time zone once.


This is particularly useful to me, since I have kali linux as my daily bare-metal system, but do most "normal user" activities (reddit, music, videos etc..) through a Virtual Box in an entirely different time zone.

### Oh...

To run:

1) Run in terminal as usual
2) Use the appropriate command-line arguments, or type ```python3 main.py --help```
3) Run the clock with ```python3 main.py --clock``` if you have a previously stored time zone.

TODO:

Clock display formatting. 