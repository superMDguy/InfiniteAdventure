Infinite Adventures
===================

Update 11/1/2016
----------------
After some research, I've decided to go with Inform7 instead of Tale.  This will make it a lot easier to generate the code than it'd be to generate a python program.  Inform also has a lot more capabilities than Tale.

Here's what my plans are for final deployment:
User goes on website -> Python server automatically writes Inform code based on templates -> Server executes code to compile Inform code, and save it as a web interface -> User is redirected to the web interface -> User plays game, maybe with an option to save progress/download game.

I'll also add settings for how many rooms are in the game.  I'll divide rooms up into __sections__.  Each section will have about 10 interacting rooms, and one overarching goal needed to 'escape' from the section.  This will make it easier for the player to hold all of the story in short term memory.  It will also provide organization and structure for the story.

Original Goal:
-------------

I think it'd be cool to have an infinite world which you can explore that's generated during play, but that would make it hard to quantify the word count.  In order to meet the 50,000 word requirement, I decided to write a program that writes the code for the text adventure story, using the Tale library.

Here are some thoughts about things I'd like in my text adventure:

1. **Multiple connected rooms.**  This one is kind of obvious.
2. **Obstacles.**  Something like a bear or a locked door.  All obstacles will require an _item_ to get past them.  This will give continuity and flow to the game as a whole, as once you get past one obstacle, you'll need to find the item for the next obstacle, etc.
3. **Enemies**.  A subset of obstacles.  These are possibly living obstacles that _actively_ try to stop you, instead of _passive_ obstacles, like a locked door.  They'll have the ability to regress your progress.
4. **Winning**.  Maybe I'll have a 'trophy case' at home base like in Zork, where you have to collect all the items to win the game.  Or maybe I'll have a specific 'goal room', which makes you win once you survive inside.
5. **Dialog**.  If I have extra time, I'd like to have some creatures/beings that can be talked to.  I'd just make a chatbot, probably using specific templates.

Hopefully all these elements will mix together to create an engaging game.  That's the ultimate goal, I want it to be _novel_ (no pun intended) and _fun to play_.  I think that it'll really help that a human is really controlling the game, because that will give it a human and therefore more realistic quality.
