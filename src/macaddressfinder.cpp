#include "macaddressfinder.h"
#include <QEventLoop>
#include <QRegularExpressionMatchIterator>

QString MacAddressFinder::findMacAddressesInText(const QString& text) {
    QRegularExpression macRegex(
        R"((?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})|(?:(?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}))"
        );
    QRegularExpressionMatchIterator i = macRegex.globalMatch(text);
    
    QStringList matches;
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        matches.append(match.captured());
    }
    
    return matches.join(", ");
}

QString MacAddressFinder::loadTextFromFile(const QString& filePath) {
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return "Error: Could not open file.";
    }
    return QString::fromUtf8(file.readAll());
}

QString MacAddressFinder::loadTextFromUrl(const QUrl& url) {
    QNetworkAccessManager manager;
    QNetworkReply* reply = manager.get(QNetworkRequest(url));
    QEventLoop loop;
    QObject::connect(reply, &QNetworkReply::finished, &loop, &QEventLoop::quit);
    loop.exec();
    
    if (reply->error() == QNetworkReply::NoError) {
        return QString::fromUtf8(reply->readAll());
    } else {
        return "Error: Could not load URL.";
    }
}

bool MacAddressFinder::isValidMacAddress(const QString& input) {
    QRegularExpression macRegex(
        R"((?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})|(?:(?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}))"
        );
    return macRegex.match(input).hasMatch();
}
