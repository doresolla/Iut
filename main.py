import sys
from MainWindow import Ui_MainWindow
from math import ceil

from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QMessageBox, QTableWidgetItem,
                             QCheckBox)

class Calc(QMainWindow, Ui_MainWindow):
    df = []
    sumPtext = ''
    sum_p = 0
    n = 0
    L = 0
    tables = {}
    nTextEdits = {}
    lTextEdits = {}
    times = []


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.i1radio.toggled.connect(self.update)
        self.i2radio.toggled.connect(self.update)
        self.i3radio.toggled.connect(self.update)
        self.i4radio.toggled.connect(self.copy)

        self.pushButton1.clicked.connect(self.mainAction)
        self.pushButton2.clicked.connect(self.mainAction)
        self.pushButton3.clicked.connect(self.mainAction)
        self.pushButton4.clicked.connect(self.mainAction)

        self.tableWidget1.FormatTable()
        self.tableWidget2.FormatTable()
        self.tableWidget3.FormatTable()
        self.tableWidget4.FormatTable()

        self.tableWidget1.createCheck()
        self.tableWidget2.createCheck()
        self.tableWidget3.createCheck()
        self.tableWidget4.createCheck()

        self.sumPtext = self.sumP.text()
        self.tabWidget.setCurrentWidget(self.tab1)

        self.tables = {0: self.tableWidget1, 1: self.tableWidget2, 2: self.tableWidget3, 3: self.tableWidget4}
        self.nTextEdits = {0: self.relHumidity1, 1: self.relHumidity2, 2: self.relHumidity3, 3: self.relHumidity4}
        self.lTextEdits = {0: self.length, 1: self.length2, 2: self.length3, 3: self.length4}

    def mainAction(self):
        self.sum_p = 0
        index = self.tabWidget.currentIndex()
        self.for_loop(index)
        self.sumP.setText(self.sumPtext + f'{self.sum_p} кВт')
        if not (self.nTextEdits[index].toPlainText() == ""):
            self.n = float(self.nTextEdits[index].toPlainText())
        if not (self.lTextEdits[index].toPlainText() == ""):
            self.L = float(self.lTextEdits[index].toPlainText())
        if (index == 0):
            self.times
            self.PlotP(I1)
            self.PlotL(I1)
            self.PlotN(I1)
        elif(index == 1):
            self.PlotP(I2)
            self.PlotL(I2)
            self.PlotN(I2)
        elif (index == 2):
            self.PlotP(I3)
            self.PlotL(I3)
            self.PlotN(I3)
        elif (index == 3):
            self.PlotP(I4)
            self.PlotL(I4)
            self.PlotN(I4)

    def frange2(self, start, stop, step):
        n_items = int(ceil((stop - start) / step))
        return (start + i * step for i in range(n_items))
    def PlotP(self, function):
        values = [item[1] for item in self.df]
        x = list(self.frange2(min(values), self.sum_p, 0.5))
        y = [function(self.L, i, self.n) for i in x]
        self.graph1.showGrid(x=True, y=True)
        self.graph1.setBackground('w')
        self.graph1.addLegend()
        self.graph1.setLabel('left','I_ут, мА')
        self.graph1.setLabel('bottom','P_уст, кВт')
        self.graph1.setXRange(min(x), max(x))
        self.graph1.setYRange(0, max(y))
        self.graph1.plot(x,y,pen = 'g', symbol ='x', symbolBrush=0.2, symbolPen='g')
    def PlotL(self, function):
        x = range(10, 300, 10)
        y = [function(i, self.sum_p, self.n) for i in x]
        self.graph2.showGrid(x=True, y=True)
        self.graph2.addLegend()
        self.graph2.setLabel('left', 'I_ут, мА')
        self.graph2.setLabel('bottom', 'L, м')
        self.graph2.setXRange(min(x), max(x))
        self.graph2.setXRange(0, max(y))
        self.graph2.plot(x, y, pen='g', symbol='x', symbolBrush=0.2, symbolPen='g')
    def PlotN(self, function):
        x = range(0, 110, 10)
        y = [function(i, self.sum_p, self.n) for i in x]
        self.graph3.showGrid(x=True, y=True)
        self.graph3.addLegend()
        self.graph3.setLabel('left', 'I_ут, мА')
        self.graph3.setLabel('bottom', 'Отн. влажность, %')
        self.graph3.setXRange(min(x), max(x))
        self.graph3.setXRange(0, max(y))
        self.graph3.plot(x, y, pen='g', symbol='x', symbolBrush=0.2, symbolPen='g')

    def update(self):
        rb = self.sender()
        if rb.isChecked():
            self.tabWidget.setCurrentIndex(int(rb.text()[4]) - 1)

    def for_loop(self, index):
      #ЧТЕНИЕ ТАБЛИЦЫ
      #по строкам таблицы : for row_index in range(table_name.rowCount())
      
        for i in range(self.tables[index].rowCount()):
            isEmpty = False
            for j in range(1, 3):
                item = self.tables[index].item(i, j)
                if item is None or item.text() == "":
                    msgBox = QMessageBox()
                    msgBox.setText(f'Введите значение в {i+1}-ю строку, {j+1}-й столбец')
                    msgBox.exec()
                    isEmpty = True
                    break
            check = self.tables[index].cellWidget(i,0).findChild(type(QCheckBox())).isChecked()
            if not (isEmpty) and (check):
                #self.df[self.tables[index].item(i, 1).text()] = float(self.tables[index].item(i, 2).text())
                try:
                    self.df.append((self.tables[index].item(i, 1).text(),float(self.tables[index].item(i, 2).text())))
                    self.sum_p += float(self.tables[index].item(i, 2).text())
                except:
                    msgBox = QMessageBox()
                    msgBox.setText(f'Число неверного формата на {i+1} строке, 3 столбце')
                    msgBox.exec()

    def copy(self):
        self.for_loop(0)
        self.for_loop(1)
        self.for_loop(2)
        cur_data = []
        rb = self.sender()
        if rb.isChecked():
            print("self_df = ", self.df)
            print("cur_data = ", cur_data)
            for r in range(self.tableWidget4.rowCount()):
                cur_data.append((self.tableWidget4.item(r, 1).text(), float(self.tableWidget4.item(r, 2).text())))
            ifIn = all(item in cur_data for item in self.df)
            if not ifIn:
                for row in self.df:
                    try:
                        _ = cur_data.index(row)
                    except:
                        cur_data.append(row)
                    print(row)

            while (self.tableWidget4.rowCount() > 0):
                self.tableWidget4.removeRow(0)
            for i in range(len(cur_data)):
                add_row = cur_data[i]
                self.tableWidget4.AddRow()
                self.tableWidget4.setItem(i, 1, QTableWidgetItem(add_row[0]))
                self.tableWidget4.setItem(i, 2, QTableWidgetItem(str(add_row[1])))

            self.tabWidget.setCurrentIndex(3)
            self.df.clear()



def I1(l, P, n):
    return -4.4815 + 0.0294 * l + 0.1119 * P + 0.0302 * n
def I2(l, P, n):
    return -11.74 + 0.0304 * l + 0.3589 * P + 0.1109 * n
def I3(l, P, n):
    return -11.23 + 0.0312 * l + 0.1827 * P + 0.1041 * n
def I4(l, P, n):
    return -11.032 + 0.0272 * l + 0.1835 * P + 0.0788 * n


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec())
