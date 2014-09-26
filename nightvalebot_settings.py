
import socket
import proverbs
import time

network = 'irc.freenode.net'
port = 6667
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
irc.connect ((network, port))
print irc.recv (4096)
irc.send ('NICK nightvalebot\r\n')
irc.send ('USER nightvalebot nightvalebot nightvalebot :Python IRC\r\n')
irc.send ('JOIN #bottesting\r\n')
irc.send ('PRIVMSG #bottesting :Welcome to Night Vale.\r\n')
while True:
    data = irc.recv (4096)
    if data == '':
        break
    data = data.split()
    print data

#[':jackhholmes!~jackhholm@c-24-1-147-220.hsd1.in.comcast.net', 'PRIVMSG', '#bottesting', ':hi']


    if data[0] == 'PING':
        print data
        irc.send ('PONG ' + data[ 1 ] + '\r\n')

    if len(data) <= 3:
        continue

    who = data[0]
    cmd = data[1]
    channel = data[2]
    msg = data[3:]
    msg = ' '.join(msg)
    msg = msg[1:]
    
    print 'THE MESSAGE WAS', msg

    if msg.lower() =='!goodnight':
        irc.send ('PRIVMSG #bottesting : Goodnight Night Vale, Goodnight\r\n')
	time.sleep(1)
        irc.send ('PART #bottesting\r\n')
        irc.send ('QUIT\r\n')
        irc.close()
        break

    if msg.lower() == 'KICK':
        irc.send ('JOIN #bottesting\r\n')

    if msg.lower() == ':!proverbrandom':
        proverbs.random_proverb()
        irc.send ('PRIVMSG #bottesting : ' + proverb + ' \r\n')

    if msg.lower() == ':!proverb':
        n = int(data[4])
        proverbs.proverb(n)
        irc.send ('PRIVMSG #bottesting : ' + proverb + ' \r\n')

    if msg.lower() == ':!character':
        character.char_prof
        irc.send ('PRIVMSG #bottesting : ' + char + ' \r\n')

