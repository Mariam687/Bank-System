
#pragma once

#include <iostream>
#include "clsScreen.h"
#include "clsListCurrenciesScreen.h"
#include "clsFindCurrencyScreen.h"
#include "clsUpdateRateScreen.h"
#include "clsCurrencyCalculatorScreen.h"
#include <iomanip>

using namespace std;

class clsCurrencyExchangeScreen :protected clsScreen
{


private:
    enum enCurrencyExchangeMenueOptions {
       eListCurrencies=1,eFindCurrency=2,eUpdateRate=3,eCurrencyCalculator=4,eMainMenue=5
    };

    static short ReadCurrencyExchangeMenueOption()
    {
        cout << setw(37) << left << "" << "Choose what do you want to do? [1 to 5]? ";
        short Choice = clsInputValidate::ReadShortNumberBetween(1, 5, "Enter Number between 1 to 5? ");
        return Choice;
    }


    static void _ShowListCurrenciesScreen()
    {
        //cout << "\n List Currencies Screen will be here.\n";
        clsListCurrenciesScreen::ShowListCurrenciesScreen();
        
    }

    static void _ShowFindCurrencyScreen()
    {
        //cout << "\n Find Currency Screen will be here.\n";
        clsFindCurrencyScreen::ShowFindCurrencyScreen();
       
    }

    static void _ShowUpdateRateScreen()
    {
        //cout << "\n Update Rate Screen will be here.\n";
        clsUpdateRateScreen::ShowUpdateCurrencyRateScreen();
        
    }

    static void _ShowCurrencyCalculatorScreen()
    {

        //cout << "\n Currency Calculator Screen will be here.\n";
        clsCurrencyCalculatorScreen::ShowCurrencyCalculatorScreen();

    }

    static void _GoBackToCurrencyExchangeMenue()
    {
        cout << "\n\nPress any key to go back to currency exchange menue...";
        system("pause>0");
        ShowCurrencyExchangeMenue();

    }

    static void _PerformCurrencyExchangeMenueOption(enCurrencyExchangeMenueOptions CurrencyExchangeMenueOptions)
    {
        switch (CurrencyExchangeMenueOptions)
        {
        case enCurrencyExchangeMenueOptions::eCurrencyCalculator:
        {
            system("cls");
            _ShowCurrencyCalculatorScreen();
            _GoBackToCurrencyExchangeMenue();
            break;
        }

        case enCurrencyExchangeMenueOptions::eFindCurrency:
        {
            system("cls");
            _ShowFindCurrencyScreen();
            _GoBackToCurrencyExchangeMenue();
            break;
        }

        case enCurrencyExchangeMenueOptions::eListCurrencies:
        {
            system("cls");
            _ShowListCurrenciesScreen();
            _GoBackToCurrencyExchangeMenue();
            break;
        }

        case enCurrencyExchangeMenueOptions::eUpdateRate:
        {
            system("cls");
            _ShowUpdateRateScreen();
            _GoBackToCurrencyExchangeMenue();
            break;
        }

        case enCurrencyExchangeMenueOptions::eMainMenue:
        {
            //do nothing here the main screen will handle it :-) ;
        }
        }


    }



public:


    static void ShowCurrencyExchangeMenue()
    {
        if (!CheckAccessRights(clsUser::enPermissions::pCurrencyExchange))                 
        {
            return;// this will exit the function and it will not continue
        }

        system("cls");
        _DrawScreenHeader("\t Currency Exchange Screen");
 
        cout << setw(37) << left << "" << "===========================================\n";
        cout << setw(37) << left << "" << "\t\t Currency Exchange Menue\n";
        cout << setw(37) << left << "" << "===========================================\n";
        cout << setw(37) << left << "" << "\t[1] List Currencies.\n";
        cout << setw(37) << left << "" << "\t[2] Find Currency.\n";
        cout << setw(37) << left << "" << "\t[3] Update Rate.\n";
        cout << setw(37) << left << "" << "\t[4] Currency Calculator.\n";
        cout << setw(37) << left << "" << "\t[5] Main Menue.\n";
        cout << setw(37) << left << "" << "===========================================\n";

        _PerformCurrencyExchangeMenueOption((enCurrencyExchangeMenueOptions)ReadCurrencyExchangeMenueOption());
    }

};


