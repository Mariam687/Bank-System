#pragma once

#include <iostream>
#include "clsScreen.h"
#include "clsUser.h"
#include "clsUtil.h"
#include "clsString.h"
#include <iomanip>
#include "clsMainScreen.h"
#include "Global.h"

class clsLoginScreen :protected clsScreen
{

private:

    static  bool _Login()
    {
        bool LoginFaild = false;
        short countFails=0;
        
        string Username, Password;
        do
        {

            if (LoginFaild)
            {
                countFails++;
                cout << "\nInvlaid Username/Password!\n";
                cout << "You have "<<3- countFails<<" trial(s) to login\n\n";
            }

            if (countFails == 3)
            {
                return false;
            }

            cout << "Enter Username? ";
            cin >> Username;

            cout << "Enter Password? ";
            cin >> Password;

           
            CurrentUser = clsUser::Find(Username, Password);

            LoginFaild = CurrentUser.IsEmpty();

        } while (LoginFaild);

        
        CurrentUser.RegisterLogIn();

        clsMainScreen::ShowMainMenue();

    }

    
public:


    static bool ShowLoginScreen()
    {
        system("cls");
        _DrawScreenHeader("\t  Login Screen");
        return _Login();

    }

};

