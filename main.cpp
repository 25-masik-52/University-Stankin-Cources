#include <QCoreApplication>
#include <QFile>
#include <QXmlStreamReader>
#include <QString>
#include <QVector>
#include <QDebug>

struct Person {
    QString firstName{};
    QString lastName{};
    struct Address {
        QString streetAddress{};
        QString city{};
        QString postalCode{};
    } address;
    QVector<QString> phoneNumbers{};
};

Person readPersonFromXml(const QString &filePath) {
    Person person;

    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qWarning() << "Не удалось открыть файл:" << filePath;
        return person;
    }

    QXmlStreamReader xml(&file);

    while (!xml.atEnd()) {
        xml.readNext();

        if (xml.isStartElement()) {
            if (xml.name() == "firstName")
                person.firstName = xml.readElementText();
            else if (xml.name() == "lastName")
                person.lastName = xml.readElementText();
            else if (xml.name() == "streetAddress")
                person.address.streetAddress = xml.readElementText();
            else if (xml.name() == "city")
                person.address.city = xml.readElementText();
            else if (xml.name() == "postalCode")
                person.address.postalCode = xml.readElementText();
            else if (xml.name() == "phoneNumber")
                person.phoneNumbers.append(xml.readElementText());
        }
    }

    if (xml.hasError())
        qWarning() << "Ошибка при чтении XML:" << xml.errorString();

    file.close();
    return person;
}

void printPerson(const Person &person) {
    qDebug() << "Имя:" << person.firstName;
    qDebug() << "Фамилия:" << person.lastName;
    qDebug() << "Адрес:";
    qDebug() << " Улица:" << person.address.streetAddress;
    qDebug() << " Город:" << person.address.city;
    qDebug() << " Почтовый индекс:" << person.address.postalCode;
    qDebug() << "Телефоны:";
    for (const auto &phone : person.phoneNumbers) {
        qDebug() << " " << phone;
    }
}

int main() {
    QString filePath = "person.xml";

    Person person = readPersonFromXml(filePath);

    printPerson(person);
}