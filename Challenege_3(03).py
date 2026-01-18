class Message:
  def __init__(self, sender, time, mid, critical):
    self.sender = sender
    self.time = time
    self.id = mid
    self.critical = critical
messages = []
subs = [set() for _ in range(4)]
def fetch_feed(user):
    visible = []
    for message in messages:
        if message.sender == user or message.sender in subs[user]:
            visible.append(message)
            visible.sort(key=lambda x: (-x.time, -x.critical))
            return [message.id for message in visible[:10]]
# Test cases
subs[1].add(2)
messages.append(Message(2,1,1,False))
messages.append(Message(2,2,2,True))
print(fetch_feed(1))
print(fetch_feed(2))
print(fetch_feed(3))