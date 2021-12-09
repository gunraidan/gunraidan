import requests
import sys
from string import Template
from PyQt5 import QtCore
from PyQt5.QtGui import*
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*


class Trans():
  changed_location = "Placeholder"
  
  def __init__(self, text = None):
    self.text = text
        
  def get_text(self):
    return self.text
    
  def set_text(self, new_text):
    self.text = new_text

  def text_update(self):
    pull = Trans()
    pull.set_text(Trans.changed_location)
    result = pull.text
    template = Template("$text")
    text_string = template.safe_substitute(text = result)
    Trans.changed_location = text_string
        

class Meat():
    
  def __init__(self, zip):
    self.zip = zip
  
  def transform (self):
    Trans.text_update(self)
    template = Template("$t_string")
    transformed_string = template.safe_substitute(t_string = Trans.changed_location)
  
  def main(self,zip):        
        
    headers = { 
      "apikey": "30ad1fa0-4b34-11ec-9573-4dfc542bc923"}

    params = (
      ("codes",zip),("country", "US")
    );


    response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params);
    
    data = response.json()
    
    longitude = data["results"][zip][0]["longitude"]
    
    latitude = data["results"][zip][0]["latitude"]
    
    print(longitude)
    print(latitude)

    
class MainWindow(QWidget):
      def __init__(self):
        super().__init__()
        self.title = "Geolocator"
        self.left = 200
        self.top = 300
        self.width = 180
        self.height = 80
        self.mw_attributes()
        self.zip_title_label = QLabel(self)
        self.location_label = QLabel(self)
        self.display()
        self.location_display()
        self.zip_code_input()
        self.button_1()
        self.show()

      def mw_attributes(self):
          self.setWindowTitle(self.title)
          self.setGeometry(self.left, self.top, self.width, self.height)
          
      def display(self):
        self.zip_title_label.setGeometry (20, 25, 200, 10)
        self.zip_title_label.setText ("Zipcode:")
        
      def location_display(self):
        self.location_label.setGeometry (60, 55, 200, 10)
        self.location_label.setText (Trans.changed_location)
        
      def zip_code_input(self):
          self.line = QLineEdit(self)
          self.line.setPlaceholderText("Input...")
          self.line.resize(60,20)
          self.line.move(80,20)
          
      def button_1(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.clicked.connect(self.button_1_click)
        self.button.setEnabled(True)
        self.button.setText("O")
        self.button.resize (30,35)
        self.button.move(145,15)

      def button_1_click(self):
        Trans.changed_location = self.line.text()
        Meat.transform(self)
        template2 = Template("$text")
        label_string = template2.safe_substitute(text = Trans.changed_location)
        self.location_label.setText(label_string)
        Meat.main(self,label_string)


app = QApplication(sys.argv) 
ex = MainWindow()
sys.exit (app.exec())