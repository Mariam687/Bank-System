#pragma once

#pragma once
#include <iostream>
#include "clsScreen.h"
#include "clsCurrency.h"
#include <iomanip>
#include "clsUtil.h"

class clsListCurrenciesScreen : protected clsScreen
{

private:

    static void PrintCurrencyRecordLine(clsCurrency Currency)
    {
        cout << setw(8) << left << "" << "| " << setw(30) << left << Currency.Country();
        cout << "| " << setw(8) << left << Currency.CurrencyCode();
        cout << "| " << setw(45) << left << Currency.CurrencyName();
        cout << "| " << setw(10) << left << Currency.Rate();

    }

public:

    static void ShowListCurrenciesScreen()
    {

        vector <clsCurrency> vCurrencies = clsCurrency::GetCurrenciesList();

        string Title = "\t  Currencues List Screen";
        string SubTitle = "\t    (" + to_string(vCurrencies.size()) + ") Currency(s).";

        _DrawScreenHeader(Title, SubTitle);

        cout << "\n\t_______________________________________________________";
        cout << "_______________________________________________\n" << endl;

        cout << setw(8) << left << "" << "| " << left << setw(30) << "Country";
        cout << "| " << left << setw(8) << "Code";
        cout << "| " << left << setw(45) << "Name";
        cout << "| " << left << setw(10) << "Rate/(1$)";
        cout << setw(8) << left << "" << "\n\t_______________________________________________________";
        cout << "_______________________________________________\n" << endl;

        

        if (vCurrencies.size() == 0)
            cout << "\t\t\t\tNo Currencies Available In the System!";
        else

            for (clsCurrency Currency : vCurrencies)
            {
                PrintCurrencyRecordLine(Currency);
                cout << endl;
            }

        cout << "\n\t_______________________________________________________";
        cout << "_______________________________________________\n" << endl;

        
    }

};



