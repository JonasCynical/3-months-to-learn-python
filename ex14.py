from sys import argv

script, user_name = argv
prompt = 'answer: '

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer =raw_input (prompt)

print "Which kind of phone do you use?"
phone =raw_input (prompt)

print"""
Alright, so you said %r about like me.
You live in %r. Not sure where thhat is.
You have a %r computer and use %r. Nice.
""" % (likes, lives, computer, phone)
