import ConfigParser
config={}
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
for s in Config.sections():
	config[s]={}
	for o in Config.options(s):
		config[s][o]=Config.get(s,o)
		
