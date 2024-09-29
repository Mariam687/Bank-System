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
