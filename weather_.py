from bs4 import BeautifulSoup
import requests
import lxml
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1100, 800)
        MainWindow.setIconSize(QtCore.QSize(100, 100))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 910)
        MainWindow.setStyleSheet("background-color:rgb(85, 85, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(310, 0, 501, 161))
        self.title.setObjectName("title")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(130, 200, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.search_input.setFont(font)
        self.search_input.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.search_input.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.search_input.setObjectName("search_input")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(490, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.submit.setStyleSheet("gridline-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 56, 69);")
        self.submit.setObjectName("submit")
        self.weather_pic = QtWidgets.QLabel(self.centralwidget)
        self.weather_pic.setGeometry(QtCore.QRect(140, 310, 321, 271))
        self.weather_pic.setText("")
        self.weather_pic.setPixmap(QtGui.QPixmap("imgs/cloud.png"))
        self.weather_pic.setScaledContents(True)
        self.weather_pic.setObjectName("weather_pic")

        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(505, 410, 151, 71))
        self.temperature.setStyleSheet("""
            QLabel {
                color: White;
            }
            """)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.temperature.setFont(font)
        self.temperature.setObjectName("temperature")

        #---------------------------------------------------------------

        self.city_title = QtWidgets.QLabel(self.centralwidget)
        self.city_title.setGeometry(QtCore.QRect(510, 320, 800, 81))
        self.city_title.setStyleSheet("""
    QLabel {
        color: White;
    }
    """)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(45)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(45)
        self.city_title.setFont(font)
        self.city_title.setObjectName("city_title")

        #--------------------------------------------------------

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(530, 500, 21, 21))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")


        #------------------------------------------------

        self.degree = QtWidgets.QLabel(self.centralwidget)
        self.degree.setGeometry(QtCore.QRect(550, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.degree.setFont(font)
        self.degree.setObjectName("degree")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)

        self.degree.setStyleSheet("""
                            QLabel {
                                color: White;
                            }
                            """)

        #------------------------------------------------

        self.day_time = QtWidgets.QLabel(self.centralwidget)
        self.day_time.setGeometry(QtCore.QRect(700, 410, 331, 31))
        self.day_time.setStyleSheet("""
            QLabel {
                color: White;
            }
            """)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.day_time.setFont(font)
        self.day_time.setObjectName("day_time")

       #---------------------------------------------------

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(700, 450, 331, 21))
        self.description.setStyleSheet("""
                    QLabel {
                        color: White;
                    }
                    """)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.day_time.raise_()


        self.title.raise_()
        self.search_input.raise_()
        self.submit.raise_()
        self.weather_pic.raise_()
        self.temperature.raise_()
        self.city_title.raise_()
        self.radioButton.raise_()
        self.degree.raise_()
        self.description.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Weather App</span></p></body></html>"))
        self.search_input.setPlaceholderText(_translate("MainWindow", " Search for a city"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))
        self.temperature.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">9°C</span></p></body></html>"))
        self.city_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">Paris</span></p></body></html>"))
        self.degree.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.day_time.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Sunday 9:00 AM</span></p></body></html>"))
        self.day_time.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Sunday 9:00 AM</span></p></body></html>"))
        self.description.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mostly Cloudy</span></p></body></html>"))


        self.submit.clicked.connect(self.search_submit)
        self.radioButton.clicked.connect(self.temperature_change)


    def search_submit(self):


        headers = {
            'User-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

        try:
            location_input = self.search_input.text()

            url = requests.get('https://www.google.com/search?q={}+weather'.format(location_input), headers=headers).text


            soup = BeautifulSoup(url, 'lxml')
            self.temp = soup.find('span', class_='wob_t q8U8x').text
            location = soup.find('div', class_='wob_loc q8U8x').text
            time = soup.find('div', class_='wob_dts').text
            description = soup.find('div', class_='wob_dcp').text
            rain = soup.find('span',{"id":"wob_pp"}).text


            self.city_title.setText(location)
            self.temperature.setText(f'{self.temp}°F')
            self.day_time.setText(time)
            self.description.setText(description)

            if (int(self.temp) < 80 and int(rain[:-1]) < 50) or ('cloudy' or 'Cloudy' in description):
                self.weather_pic.setPixmap(QtGui.QPixmap("cloud.png"))
            if (int(rain[:-1]) > 40) or 'Thunderstorm' in description or 'rainy' in description:
                self.weather_pic.setPixmap(QtGui.QPixmap("rain.ico"))
            if (int(self.temp) > 80) or 'Sunny' in description:
                self.weather_pic.setPixmap(QtGui.QPixmap("sunny.png"))




        except AttributeError:
            self.city_title.setText('Wrong Location')


    def temperature_change(self,):
        if self.radioButton.isChecked() == True:
            self.temperature.setText(f'{int((int(self.temp)-32) * 5/9)}°C')
            self.degree.setText('°F')
        else:
            self.degree.setText('°C')
            self.temperature.setText(f'{self.temp}°F')





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

