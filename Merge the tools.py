def merget_the_tools(string,k):
	string_length = len(string)
	for i in range(0,string_length,k):
		ui_creator(string[i:i+k])

def ui_creator(ti):
	# ti -> ui
	ui = []
	p = []
	Ui_string = ""
	for i in ti:
		if i not in p:
			Ui_string += i
			p.append(i)
	ui.append(Ui_string)
	for i in ui:
		print(i)

	
merget_the_tools("AABCAAADA",3)

