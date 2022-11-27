import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("learn PyQt5")
        self.setBackgroundRole(qtg.QPalette.ColorRole.Background)
        self.setLayout(qtw.QGridLayout())

        my_label = qtw.QLabel("Hello World! wat ur name?")
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Enter your name here...")
        my_entry.setMinimumHeight(50)
        self.layout().addWidget(my_entry)
        
        # Create a button
        my_button = qtw.QPushButton("Click me!", clicked=lambda: press_it())
        my_button.setObjectName("my_button")
        my_button.setFont(qtg.QFont("Helvetica", 18))
        my_button.setMinimumHeight(35)
        self.layout().addWidget(my_button)
        
        # Show the app
        self.show()

        def press_it():
            my_label.setText(f"Hello {my_entry.text()}!")

app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()