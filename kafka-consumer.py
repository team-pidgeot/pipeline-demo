from kafka import KafkaConsumer
from github import Github

#Must pip install pygithub first

user = "team-pidgeot"
password = "3r07W7R940yVAPRm5VL6"
g = Github(user,password)

consumer = KafkaConsumer('test', bootstrap_servers='34.217.221.173:9092', auto_offset_reset='latest')
#consumer.seek_to_beginning()
for message in consumer:
    print (message)
    messagestr = message.value
    repo = g.get_user().get_repo("pipeline-demo")
    contents = repo.get_contents("message.txt", ref="master")
    repo.update_file(contents.path, "updating the repo with new message contents", messagestr, contents.sha, branch="master")

