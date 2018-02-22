# Steps to edit this project (for RCHS club members)
### 1. Edit [bot.py](https://github.com/rchsmohsin/the-phoenix-bot/blob/master/bot.py) with whatever changes you'd like to make.
### 2. Edit [requirements.txt](https://github.com/rchsmohsin/the-phoenix-bot/blob/master/requirements.txt) if you added any libraries to the python code.
At the top of the code there should be some libraries, you'll see `import LIBRARYNAME `. If I were adding one of these, I would go to the requirements file and type in `LIBRARYNAME` on a new line.
### 3. Propose changes to the files.
Whenever you're finished with your edits, or along the way, you can press the green button that you'll see at the bottom that says "Propose Changes" or something like that. When you do that, it should create a separate branch for you. You can then make a pull request to merge your branch with the `master` branch. That request will have to be approved by me or another admin. 


# Hosting telegram bot on [Heroku](https://heroku.com) for free.
Easy way to host your python telegram bot on Heroku
Make an account on here if you'd like to host a bot yourself.

# Steps to Create Your Own Bot
## Deploying via [Heroku Toolbelt](https://toolbelt.heroku.com/) (CLI)
Install [Heroku Toolbelt](https://toolbelt.heroku.com/), then:
### Clone repository
`git clone https://github.com/rchsmohsin/the-phoenix-bot.git`
### Edit files
1. Edit [bot.py](https://github.com/rchsmohsin/the-phoenix-bot/blob/master/bot.py) file with your code (whatever bot code you're running)
2. Edit [requirments.txt](https://github.com/rchsmohsin/the-phoenix-bot/blob/master/requirements.txt) with your code's dependencies (you know when you write "import whatever" at the top of your bot code? yea put the "whatever" into this file, each on a different line.
3. Specify your python [runtime](https://github.com/rchsmohsin/the-phoenix-bot/blob/master/runtime.txt), avaliable versions listed [here](https://devcenter.heroku.com/articles/python-runtimes) (don't overthink this, it's just whatever version of python you're running. For me, it's: `python-3.6.4`

### Go to command line (type cmd into windows search, or just search command prompt)
#### Also if you don't know command line, you should probably learn it at some point but if you follow these directly it should be fine. The only issue will be if something messes up along the way.
(caps stuff should be replaced with corresponding thing, # means comment) 
```
cd heroku-telegram-bot
heroku login
heroku create APPNAME
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
```
If this isn't successful, STOP and figure out what's wrong. It's probably in the "Edit files" category of this guide.
```
heroku ps:scale APPNAME=1 # start bot dyno
heroku logs --tail # If for some reason it’s not working, check the logs
heroku ps:stop bot #stop bot dyno
```


### More about
- https://devcenter.heroku.com/articles/dynos
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/heroku-redis
- https://devcenter.heroku.com/articles/error-codes

Thanks to [Roman Zaynetdinov](https://github.com/zaynetro) for awesome and easy CLI guide.
This is an edited guide, originally from github user Kylmakalle. I (rchsmohsin) have edited it to be more in line with what I did to get my bot working.
