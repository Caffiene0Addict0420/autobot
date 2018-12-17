import praw, time, pickle

def send_msg(reddit, user, title, message):
    reddit.redditor(user).message(title, message)

def getData(myfile):
    for line in open(myfile):
        return line

client_id = getData("client_id.txt")
client_secret = getData("client_secret.txt")
username = getData("username.txt")
password = getData("password.txt")
    
try:

    reddit = praw.Reddit(client_id='80DMpVrG-a7Bkg',
                         client_secret='I1aKl88RwDQGts7x1SSbtp-aOYU',
                         user_agent='Freelancer Jobs Scraper (Python)',
                         username = 'Caffiene_Addict-420',
                         password = 'testing')
    print("Authenticated!")
    try:all_id = pickle.load(open("redditid.data", "rb"))
    except:all_id = []
    while True:
        try:
            for submission in reddit.subreddit("slavelabour+forhire+jobbit+Jobs4Bitcoins").new(limit=100):
                if submission.id not in all_id:
                    #print(submission.title)
                    all_id.append(submission.id)
                    title = submission.title.lower()
                    alltext = title + " " + submission.selftext.lower()
                    if "[task]" in alltext or "[hiring]" in alltext or "[paid]" in title.lower() or "(paid)" in title.lower():
                        if "[for hire]" not in alltext:
                            if " python " in alltext or " bot " in alltext or " scraper " in alltext or " automate " in alltext or " automation " in alltext:
                                
                                print(submission.title)
                                print(submission.url)
                                #print(submission.selftext)
                                if submission.subreddit != "forhire":
                                    submission.reply("$bid Pmed")
                                send_msg(reddit, submission.author.name, "Python / Bot Creation", "* I Am Away Until The 25th Of December, So Projects Will Be Resumed After then * \n\n You can still contact me (discord) at CaffieneAddict420#8646 or caffiene0addict0420@gmail.com \n\n Just messaging to say i saw your post regarding python / making a bot, so i thought i'd shoot you a PM.\n\nI am a senior python developer with over 7 years expirience working with the language. \n\nWondering how i messaged you so fast? \n\nThis  message itself was sent by one of my bots, i use it to showcase my skills, and land jobs. PM me back if you are interested\n\n*This message is automated and is not confirmation that i have accepted your task, it is just letting you know this is a task that i would be able to complete. I will manually message you back to let you know if the pricing works (I will reject underpaid tasks)*")
                                print("\n" * 5)
        except Exception as e:
            print(e)
            print("ADVICE: *Check Wifi*")
        time.sleep(60)
except KeyboardInterrupt:
    pickle.dump(all_id, open("redditid.data", "wb"))
except Exception as e:print(e)
while True:pass
