#pragma once

#include <iostream>
#include "clsScreen.h"
#include "clsBankClient.h"
#include "clsInputValidate.h"

class clsTransferScreen : protected clsScreen
{

private:

    static void _PrintClient(clsBankClient Client)
    {
        cout << "\nClient Card:";
        cout << "\n___________________";
        cout << "\nFull Name   : " << Client.FullName();
        cout << "\nAcc. Number : " << Client.AccountNumber();
        cout << "\nBalance     : " << Client.AccountBalance;
        cout << "\n___________________\n";

    }

    static string _ReadAccountNumber(string message)
    {
        string AccountNumber = "";
        cout << "\n" << message;
        cin >> AccountNumber;

        while (!clsBankClient::IsClientExist(AccountNumber))
        {
            cout << "\nClient with [" << AccountNumber << "] does not exist.\n";
            AccountNumber = _ReadAccountNumber("Enter Another Account Number: ");
        }

        return AccountNumber;
    }

    static float ReadAmount(clsBankClient SourceClient)
    {
        float Amount;

        cout << "\nEnter Transfer Amount? ";

        Amount = clsInputValidate::ReadFloatNumber();

        while (Amount > SourceClient.AccountBalance)
        {
            cout << "\nAmount Exceeds the available Balance, Enter another Amount ? ";
            Amount = clsInputValidate::ReadDblNumber();
        }
        return Amount;
    }

    

public:

    

    static void ShowTransferScreen()
    {
        string Seperator = "#//#";
        string TranferRecordLine = "";

        _DrawScreenHeader("\t   Transfer Screen");

        string AccountNumber = _ReadAccountNumber("Enter Account Number To Transfer From: ");

        clsBankClient SourceClient = clsBankClient::Find(AccountNumber);
        _PrintClient(SourceClient);

        AccountNumber = _ReadAccountNumber("Enter Account Number To Transfer To: ");

        clsBankClient DestinationClient = clsBankClient::Find(AccountNumber);
        _PrintClient(DestinationClient);

        float Amount = ReadAmount(SourceClient);

        cout << "\nAre you sure you want to perform this transaction? ";
        char Answer = 'n';
        cin >> Answer;

        if (Answer == 'Y' || Answer == 'y')
        {

            if (SourceClient.Transfer(Amount, DestinationClient,CurrentUser.UserName))
            {
                cout << "\nTransfer done successfully\n";
               
            }
            else
            {
                cout << "\nTransfer Faild \n";
            }

            _PrintClient(SourceClient);
            _PrintClient(DestinationClient);


        }

    }


};

