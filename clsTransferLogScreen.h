
#pragma once

#include <iostream>
#include "clsScreen.h"
#include <iomanip>
#include <fstream>
#include "clsBankClient.h"

class clsTransferLogScreen :protected clsScreen
{

private:

    static void PrintTranferRecordLine(clsBankClient::stTransferRecord TransferRegisterRecord)
    {

        cout << setw(8) << left << "" << "| " << setw(20) << left << TransferRegisterRecord.DateTime;
        cout << "| " << setw(10) << left << TransferRegisterRecord.SourceAccountNumber;
        cout << "| " << setw(10) << left << TransferRegisterRecord.DestinationAccountNumber;
        cout << "| " << setw(10) << left << TransferRegisterRecord.Amount;
        cout << "| " << setw(10) << left << TransferRegisterRecord.SourceClientBalance;
        cout << "| " << setw(10) << left << TransferRegisterRecord.DestinationClientBalance;
        cout << "| " << setw(10) << left << TransferRegisterRecord.UserName;
    }

public:

    static void ShowTransferLogScreen()
    {
       
        vector <clsBankClient::stTransferRecord> vTransferRecord = clsBankClient::GetTranferLogList();

        string Title = "\tTransfer Log List Screen";
        string SubTitle = "\t\t(" + to_string(vTransferRecord.size()) + ") Record(s).";

        _DrawScreenHeader(Title, SubTitle);

        cout << "\n\t_______________________________________________________";
        cout << "_________________________________________\n" << endl;

        cout << setw(8) << left << "" << "| " << left << setw(20) << "Date/Time";
        cout << "| " << left << setw(10) << "sUser";
        cout << "| " << left << setw(10) << "dUser";
        cout << "| " << left << setw(10) << "Amount";
        cout << "| " << left << setw(10) << "sBalance";
        cout << "| " << left << setw(10) << "dBalance";
        cout << "| " << left << setw(10) << "User";
        cout << setw(8) << left << "" << "\n\t_______________________________________________________";
        cout << "_________________________________________\n" << endl;

        if (vTransferRecord.size() == 0)
            cout << "\t\t\t\tNo Logins Available In the System!";
        else

            for (clsBankClient::stTransferRecord Record : vTransferRecord)
            {

                PrintTranferRecordLine(Record);
                cout << endl;
            }

        cout << "\n\t_______________________________________________________";
        cout << "_________________________________________\n" << endl;

    }

};


