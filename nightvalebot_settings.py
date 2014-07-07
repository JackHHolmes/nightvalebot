
import socket
import proverbs

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

    if data.find ('PING') != -1:
        irc.send ('PONG ' + data.split() [ 1 ] + '\r\n')

    if data.find ('!goodnight') != -1:
        irc.send ('PRIVMSG #bottesting : Goodnight Night Vale, Goodnight\r\n')
        irc.send ('PART #bottesting\r\n')
        irc.send ('QUIT\r\n')

    if data.find ('KICK') != -1:
        irc.send ('JOIN #bottesting\r\n')

    if data.find ('!proverbrandom') != -1:
        proverbs.random_proverb()
        irc.send ('PRIVMSG #bottesting : ' + proverb + ' \r\n')

    if data.find ('!proverb') != -1:
        proverbs.proverb(n)
        irc.send ('PRIVMSG #bottesting : ' + proverb + ' \r\n')
