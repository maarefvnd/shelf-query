#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QProcess>
#include <QDebug>
#include <QProcess>
#include <QStandardItemModel>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QFile>
#include <QTextStream>
#include <QStringList>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    model = new QStandardItemModel(this);
    ui->tableView->setModel(model);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
     ui->stackedWidget->setCurrentIndex(1);
}




void MainWindow::on_pushButton_2_clicked()
{
    QString pythonPath = "python"; // یا مسیر کامل پایتون مثل C:/Python311/python.exe
    QString scriptPath = "V:/Masin/Projects/shelf-query/python-fetcher/fetch-books.py"; // مسیر اسکریپت پایتون

    QProcess *process = new QProcess(this);

    // اگه بخوای خروجی رو بخونی:
    connect(process, &QProcess::readyReadStandardOutput, [=]() {
        QByteArray output = process->readAllStandardOutput();
        qDebug() << output;
    });

    connect(process, &QProcess::readyReadStandardError, [=]() {
        QByteArray errorOutput = process->readAllStandardError();
        qDebug() << "Error:" << errorOutput;
    });

    process->start(pythonPath, QStringList() << scriptPath);

    // بررسی اینکه اجرا شد یا نه
    if (!process->waitForStarted()) {
        qDebug() << "Failed to start the Python script!";
    }
}


void MainWindow::on_pushButton_3_clicked()
{
    QString filePath = "V:/Masin/Projects/shelf-query/python-fetcher/books.csv";
    // ⚠️ مسیر دقیق فایل CSV که پایتون ساخته

    QFile file(filePath);

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Cannot open CSV file!";
        return;
    }

    QTextStream in(&file);
    // ❌ in.setCodec("UTF-8");  ← اینو کامل حذف کن

    model->clear();

    // خواندن هدر
    if (!in.atEnd()) {
        QString headerLine = in.readLine();
        QStringList headers = headerLine.split(",");
        model->setColumnCount(headers.size());
        model->setHorizontalHeaderLabels(headers);
    }

    // خواندن ردیف‌ها
    while (!in.atEnd()) {
        QString line = in.readLine();
        QStringList fields = line.split(",");

        QList<QStandardItem*> rowItems;
        for (const QString &field : fields) {
            rowItems.append(new QStandardItem(field));
        }

        model->appendRow(rowItems);
    }

    file.close();

    ui->tableView->resizeColumnsToContents();
}

