import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar
from main_ui import *
from request_handler import RequestHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.httpMethods = [
            "GET",
            "POST",
            "PUT",
            "DELETE",
            "PATCH",
            "HEAD",
            "OPTIONS"
        ]

        self.ui.methodsComboBox.addItems(self.httpMethods)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Connections
        self.ui.methodsComboBox.currentIndexChanged.connect(self.updateHttpMethod)
        self.ui.sendRequestPushButton.clicked.connect(self.sendRequest)

        self.show()
    
    def updateHttpMethod(self):
        print(self.httpMethods[self.ui.methodsComboBox.currentIndex()])
    
    def sendRequest(self):
        # print(self.ui.urlInput.text)
        if self.ui.urlInput.text() == "":
            self.statusBar.showMessage("URL text box is empty.",2000)
        else:
            response_type, response_content = RequestHandler(self.ui.urlInput.text(), method=self.ui.methodsComboBox.currentText()).send()
        if response_type == "json":
            print(response_content)
            self.ui.outputTextEdit.setText(str(response_content))
        if response_type == "html":
            print(response_content)
            self.ui.outputTextEdit.setText(response_content)
        

    def updateOutput(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())