#include <iostream>
#include "clsLoginScreen.h"

int main()

{
    while (true) {

        if (!clsLoginScreen::ShowLoginScreen())
            break;
    }

    cout << "\nYou are locked after 3 trial(s).\n";



    system("pause>0");

    return 0;


}

/*
#include <iostream>
#include "clsCurrency.h"




int main()

{
    clsCurrency Currency1 = Currency1.FindByCode("jod");

    if (Currency1.IsEmpty())
    {
        cout << "\nCurrency Is Not Found!\n";
    }
    else
    {
        _PrintCurrency(Currency1);
    }

    clsCurrency Currency2 = Currency2.FindByCountry("Egypt");

    if (Currency2.IsEmpty())
    {
        cout << "\nCurrency Is Not Found!\n";
    }
    else
    {
        _PrintCurrency(Currency2);
    }

    cout << "Currency1 after updating Rate:\n";
    Currency1.UpdateRate(0.71);
    _PrintCurrency(Currency1);


    return 0;
}

*/