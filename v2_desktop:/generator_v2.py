import sys  
import random 
import string  

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QSlider, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt 

class PasswordGenerator(QWidget): 
    def __init__(self):  
        super().__init__()  

        self.setWindowTitle("Password Generator") 
        self.setFixedSize(450, 280)  

        self.dark_mode = False  

        layout = QVBoxLayout() 
        layout.setSpacing(10)  

        self.title = QLabel("🔒 Password Generator")  
       
        self.title.setAlignment(Qt.AlignCenter)  
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;") 
        layout.addWidget(self.title) 

        self.password_field = QLineEdit()  
        self.password_field.setReadOnly(True)  
        self.password_field.setStyleSheet( 

        "font-size: 13px; padding: 3px; border: 2 solid #7f8c8d; border-radius: 8px;"
        )

        layout.addWidget(self.password_field)  

        slider_layout = QHBoxLayout()

        self.slider_label = QLabel("How Long: 12")  
        self.slider_label.setStyleSheet("font-size: 15px;")  
        slider_layout.addWidget(self.slider_label) 

        self.slider = QSlider(Qt.Horizontal) 
        self.slider.setRange(6, 50)  
        self.slider.setValue(12) 
        self.slider.setMinimumHeight(30)  
        self.slider.valueChanged.connect(self.update_length_label)  
        slider_layout.addWidget(self.slider)  

        layout.addLayout(slider_layout)  

        self.generate_btn = QPushButton("Generate")  
        self.generate_btn.setStyleSheet(self.button_style())  
        self.generate_btn.clicked.connect(self.generate_password)  
        layout.addWidget(self.generate_btn)  

        self.copy_btn = QPushButton("Copy")  
        self.copy_btn.setStyleSheet(self.button_style())  
        self.copy_btn.clicked.connect(self.copy_password)  
        layout.addWidget(self.copy_btn) 

        self.theme_btn = QPushButton("Theme")
      
        self.theme_btn.setStyleSheet(self.button_style())  
        self.theme_btn.clicked.connect(self.toggle_theme)  
        layout.addWidget(self.theme_btn) 

        self.setLayout(layout) 

        self.apply_theme()  

    def update_length_label(self):  
        self.slider_label.setText(f"How Long: {self.slider.value()}") 

    def generate_password(self): 
        length = self.slider.value() 
        chars = string.ascii_letters + string.digits + string.punctuation 
        password = ''.join(random.choice(chars) for _ in range(length))  
        self.password_field.setText(password)  

    def copy_password(self): 
        password = self.password_field.text()  
        if not password:  
            return
        QApplication.clipboard().setText(password)  

        msg = QMessageBox(self)  
        msg.setWindowTitle("Copied")  
        msg.setText("Your password is Copied!")  
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setWindowModality(Qt.NonModal)  
        msg.setStyleSheet("QLabel{min-width:250px; text-align:center;}")  
        msg.show() 

    def toggle_theme(self):  
        self.dark_mode = not self.dark_mode 
        self.apply_theme() 

    def apply_theme(self):  
        if self.dark_mode:  
            self.setStyleSheet("""
               
                QWidget { background-color: #2c3e50; color: white; }
                QLineEdit { background-color: #34495e; color: white; border: 2px solid  #1abc9c; }
            """)
        else:  
            self.setStyleSheet("""
                QWidget { background-color: white; color: black; }
                QLineEdit { background-color: white; color: black; border: 2px solid #7f8c8d; }
            """)
        self.generate_btn.setStyleSheet(self.button_style())  
        self.copy_btn.setStyleSheet(self.button_style())

        self.theme_btn.setStyleSheet(self.button_style())

    def button_style(self):  
        if self.dark_mode: 
            return """
                QPushButton {
                    background-color: #1abc9c;
                    color: black;
                    font-size: 16px;
                    padding: 4px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #16a085;
                }
            """
        else:  
            return """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    font-size: 16px;
                    padding: 4px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                
               }
               """

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = PasswordGenerator() 
    window.show()  
    sys.exit(app.exec_())  
