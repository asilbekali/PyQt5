from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
import sys

def search():
    number = txt.text()
    try:
        number = int(number)
        numbers = {
            1: 'bir', 2: 'ikki', 3: 'uch', 4: "to'rt", 5: 'besh', 6: 'olti', 7: 'yetti',
            8: 'sakiz', 9: "to'qiz", 10: "o'n", 11: "o'n bir", 12: "o'n ikki", 13: "o'n uch",
            14: "o'n to'rt", 15: "o'nbesh", 16: "o'n olti", 17: "o'n yetti", 18: "o'n sakkiz",
            19: "o'n to'qiz", 20: "yigirma", 21: 'yigirma bir', 22: 'yigirma ikki',
            23: 'yigirma uch', 24: "yigirma to'rt", 25: 'yigirma besh'
        }
        if 1 <= number <= 25:
            label = QLabel(window)
            label.setText(numbers[number])
            label.move(300, 130)
            label.show()
    except ValueError:
        pass

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(1000, 100, 700, 700)
txt = QLineEdit(window)
btn = QPushButton("Click", window)
btn.setStyleSheet("QPushButton::hover"
                  "{"
                  "background-color : #00f365;"
                  "}")
btn.move(320, 60)
txt.move(300, 100)
soz = QLabel(window)
soz.setText("25 orlig'ida son kiriting")
soz.move(300, 150)
soz.show()
btn.clicked.connect(search)
window.show()
sys.exit(app.exec_())
