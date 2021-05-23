# pomodoro-start
A timer for measuring work and break times using the pomodoro technique

A guided tutorial on making a timer for the pomodoro technique using tkinter. 

This was a pretty fun exercise. I wasn't entirely familiar with the use of canvases but realised that they were something akin to surfaces in GML. After which I didn't
really have a problem understanding them. Following the advice of another user I decided to add a bell to the timer, and I also [on my own initiative] eliminated a bug
which would occur if the 'start' button was pressed while the timer was already running. The bug was that i'd get a new countdown for each time the start button was pressed - 
this was dealt with rather handily by just adding a flag as to whether the timer was running, which reset when the 'reset' button was pushed. At first I thought I'd simply
run the reset function before starting the timer, but that threw up a whole host of errors so just stuck with the simple solution. I had heard before that multiply works
on strings in Python, so to avoid using a for loop to determine how many check marks I needed, along with the requisite vertex calculations 
      
      counter = 0
      label = Label(text = check_mark, xpos = 400 + (20 * checkmarks -1),...)

I just set the string to multiply itself by a counter:

    counter = 0
    label = Label(text = check_mark * counter, xpos = 400,...)
    
Which kind of felt like cheating but was a lot simpler in the long run =)
