#include "macaddressfinder.h"
#include <gtest/gtest.h>
#include <iostream>
#include <QCoreApplication>

using namespace std;
using namespace MacAddressFinder;

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);
    
    QString filePath = ":/assets/test/test_assets/example.txt";
    QString url = "https://habr.com/ru/articles/483670/";
    
    QString fileContent = loadTextFromFile(filePath);
    QString urlContent = loadTextFromUrl(QUrl(url));
    
    QString fileMacs = findMacAddressesInText(fileContent);
    QString urlMacs = findMacAddressesInText(urlContent);
    
    cout << "MAC addresses from file: " << fileMacs.toStdString() << endl;
    cout << "MAC addresses from URL: " << urlMacs.toStdString() << endl;
    
    return app.exec();
    
    // для тестирования
    /*::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();*/
}

