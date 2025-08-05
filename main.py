import wx

# 1. Define a custom frame (main window)
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(1000, 500))

        # LOCAL VARIABLES:
        # 2. Panel to hold UI elements
        panel = wx.Panel(self)

        # INSTANCE VARIABLES: (methods from the parent class wx.Frame)
        # 3. Static text label
        self.label = wx.StaticText(panel, label="Welcome to Financial Planner", pos=(20, 20)) # Provide the window, name and position

        # 4. Button with click event
        self.button = wx.Button(panel, label="Test Button", pos=(20, 60)) # Provide the window, name and position
        self.button.Bind(wx.EVT_BUTTON, self.on_click) # Provide the actuator(event) and the response(handler)

        self.Centre()  # Center the window
        self.Show()    # Show the window

    # 5. Event handler for button
    def on_click(self, event):
        print("Working")  # Test output to console
        self.label.SetLabel("Button clicked!")  # Update label text


# 6. Start the application
if __name__ == "__main__": # Simply used as a safe way to start the program
    app = wx.App(False) # Create the actual app
    frame = MainWindow(None, title="Financial Planner") # Create the frame object (not the actual app)
    app.MainLoop() # Loop to check for events