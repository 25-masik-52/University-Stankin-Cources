#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "../src/macaddressfinder.h"

using namespace std;
using namespace MacAddressFinder;

// Тест на валидные MAC-адреса
TEST(MacAddressTest, ValidMacAddresses) {
    vector<string> validMacs = {
        "00:1A:2B:3C:4D:5E",
        "FF:FF:FF:FF:FF:FF",
        "01-23-45-67-89-AB",
        "1234.5678.9ABC",
        "DEAD.BEEF.C0DE"
    };
    
    for (const auto& mac : validMacs) {
        EXPECT_TRUE(isValidMacAddress(QString::fromStdString(mac)));
    }
}

// Тест на невалидные MAC-адреса
TEST(MacAddressTest, InvalidMacAddresses) {
    vector<string> invalidMacs = {
        "00:1A:2B:3C:4D",  // Недостаточно частей
        "00:1A:2B:3C:4D:ZE", // Неверный символ
        "01-23-45-67-89-A", // Недостаточно символов
        "1234.5678.9AB",   // Недостаточно символов
        "GARBAGE"          // Не MAC-адрес
    };
    
    for (const auto& mac : invalidMacs) {
        EXPECT_FALSE(isValidMacAddress(QString::fromStdString(mac)));
    }
}
