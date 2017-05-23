from appJar import gui

app=gui()

app.addLabel("1", "Welcome to TabbedFrame 1.0")
app.setBg("blue")
app.startLabelFrame("Notebooks")
app.setBg("yellow")

app.startTabbedFrame("Book1", 0, 0)
app.startTab("aaa")
app.setBg("red")
app.addLabel("11", "Stuff here")
app.addLabel("12", "Stuff here")
app.addLabel("13", "Stuff here")
app.stopTab()
app.startTab("bbb")
app.addLabel("21", "Stuff here")
app.addLabel("22", "Stuff here")
app.addLabel("23", "Stuff here")
app.stopTab()
app.startTab("ccc")
app.addLabel("31", "Stuff here")
app.addLabel("32", "Stuff here")
app.addLabel("33", "Stuff here")
app.stopTab()
app.stopTabbedFrame()

app.startTabbedFrame("Book2", 0, 1)
app.startTab("aaa")
app.addLabel("211", "Stuff here")
app.addLabel("212", "Stuff here")
app.addLabel("213", "Stuff here")
app.stopTab()
app.startTab("bbb")
app.addLabel("221", "Stuff here")
app.addLabel("222", "Stuff here")
app.addLabel("223", "Stuff here")
app.stopTab()
app.startTab("ccc")
app.addLabel("231", "Stuff here")
app.addLabel("232", "Stuff here")
app.addLabel("233", "Stuff here")
app.stopTab()
app.stopTabbedFrame()

app.stopLabelFrame()

app.go()
