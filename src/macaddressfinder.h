#pragma once

#include <QString>
#include <QFile>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QUrl>
#include <QRegularExpression>

namespace MacAddressFinder {
QString findMacAddressesInText(const QString& text);
QString loadTextFromFile(const QString& filePath);
QString loadTextFromUrl(const QUrl& url);

bool isValidMacAddress(const QString& input);
};
