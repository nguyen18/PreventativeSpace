# PreventativeSpace
Athena Hacks Project! made by Taylor Nguyen, Vanessa Yu, Lancy Tan

- https://preventionspace.web.app
- https://devpost.com/software/preventative-space

### Inspiration
The recent Coronavirus outbreak inspired us to create a text-adventure video game that could educate the general public about the importance of taking precautions during times of mass viral infections to keep not only ourselves healthy, but others as well.

### What it does
Prevention Space is a text-adventure video game that allows the user to go through a county that is experiencing a mass viral infection from a first-person point of view. The player has the choice to play through one of three paths, each path following a different virus based on how it spreads (airborne, water/food, and bodily contact). At the end, it educates them on how to prevent or help people based on their chosen disease path. During the game, they are also supposed to get texts from NPCs in-game to better immerse their gaming experience (with the help of Twilio), but it was implemented in the end, and so text messages are just described in the console.

### How it's built
We embedded a Python console onto a website. The Python was written on Repl.it and pasted into Trinket.io, which compiles Python code and allows you to embed it into HTML code so that it can show an interactive console that the user can play the game on. The website was written in HTML/CSS and hosted using Firebase with a domain they gave us.

### Challenges we ran into
We struggled with hosting our website on our domain from domain.com and spent many hours trying to host it. Instead, we used Google Firebase to host our domain and ended being provided a different domain to use as well. We also struggled to find a way to have an interactive console on our website without the code showing. We also tried to implement Twilio into our game, but it ended up being a fruitless struggle.

### Accomplishments
We were able to get an interactive console working on our website which took us a long time to figure out. After hours, our team member Vanessa figured out how to host a website on firebase. Lancy figured out how to use Twilio for the most part (the trinket.io we imbedded on our site is having issues with it, but in repl.it we were able to send messages to a phone). Taylor built the frontend of the website. All of us spent our time creating our own stories related to one of three diseases (it was a fun way to add creativity to our project).

### What I learned
- To put a website on the internet, you need a domain as well as a server to host it.
- There are static sites (that only show text and don't have any backend programs running) that can be hosted by places like Github, but software such as Google Firebase can also host a domain (and doesn't even require registering for a domain name).
- We also learned that implementing APIs are complicated, but allow for applications to have a new level of depth, as with the Twilio API we were able to send a text to a phone with information related to our game, but when we tried to embed the trinket.io python console into our website it would no longer work.

### What's next
- Adding graphics to the game would be nice and having more complete and cohesive pathways in the game.
- Provide more resources to users on where to go if they are still interested in learning more about diseases and how to protect yourself and others.
- Implement the Twilio API to send text messages corresponding to parts of the story when the user gets a text or email.
