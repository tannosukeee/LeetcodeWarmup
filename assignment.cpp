#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    int choice;

    do
    {
        cout << "\n==============================" << endl;
        cout << "            MENU              " << endl;
        cout << "==============================" << endl;
        cout << "1. Display third powers" << endl;
        cout << "2. Display loan payment chart" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
        {
            int a, b;

            cout << "\nEnter two integers: ";
            cin >> a >> b;

            // Make sure a is the smaller number
            if (a > b)
            {
                int temp = a;
                a = b;
                b = temp;
            }

            cout << "\nThird powers of the numbers from "
                 << a << " to " << b << ":" << endl;

            for (int i = a; i <= b; i++)
            {
                cout << i * i * i << endl;
            }

            break;
        }

        case 2:
        {
            double loanAmount, rate;
            double monthlyRate;
            double z;
            double monthlyPayment;
            double totalInterest;

            cout << "\nEnter the loan amount: $";
            cin >> loanAmount;

            cout << "Enter the annual interest rate: ";
            cin >> rate;

            monthlyRate = rate / 1200.0;

            cout << fixed << setprecision(2);

            cout << "\n"
                 << setw(10) << "Term"
                 << setw(20) << "Monthly Payment"
                 << setw(20) << "Total Interest" << endl;

            cout << setw(10) << "Years"
                 << setw(20) << "($)"
                 << setw(20) << "($)" << endl;

            cout << "--------------------------------------------------" << endl;

            for (int term = 1; term <= 5; term++)
            {
                z = (1 - pow(1 + monthlyRate, -12 * term)) / monthlyRate;

                monthlyPayment = loanAmount / z;

                totalInterest =
                    (term * 12 * monthlyPayment) - loanAmount;

                cout << setw(10) << term
                     << setw(20) << monthlyPayment
                     << setw(20) << totalInterest << endl;
            }

            break;
        }

        case 3:
            cout << "\nProgram ended." << endl;
            break;

        default:
            cout << "\nInvalid choice. Please enter 1, 2, or 3."
                 << endl;
        }

    } while (choice != 3);

    return 0;
}
