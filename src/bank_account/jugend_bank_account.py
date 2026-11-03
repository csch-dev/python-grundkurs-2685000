#!/usr/bin/env python3

from typing import List, Tuple

from bank_account.bank_account import BankAccount

class JugendBankAccount(BankAccount):
    def abheben(self, betrag: float) -> None:
        if betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError("Abhebung fehlgeschlagen: Maximalbetrag von 25 EUR überschritten.")
