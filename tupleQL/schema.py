import graphene
from graphene_django import DjangoObjectType
from decimal import Decimal

from .models import BalanceSheet
from api.alpha_vantage.fundamentals import get_balance_sheet

# TODO: Move this to a utils file
def Price(value):
    return round(Decimal(value), 6)

#-----------------------------------------------------------------------------------------------------------------------
# Types
#-----------------------------------------------------------------------------------------------------------------------
class BalanceSheetType(DjangoObjectType):
    class Meta:
        model = BalanceSheet


#-----------------------------------------------------------------------------------------------------------------------
# Queries
#-----------------------------------------------------------------------------------------------------------------------
class Query(graphene.ObjectType):
    balance_sheet = graphene.Field(BalanceSheetType, ticker=graphene.String(required=True))

    def resolve_balance_sheet(self, info, **kwargs):
        tkr = kwargs.get('ticker')
        alpha_vantage_response = get_balance_sheet(tkr)

        balance_sheet = BalanceSheet(
            ticker=tkr,
            cash=Price(alpha_vantage_response['cashAndCashEquivalentsAtCarryingValue']),
            accounts_receivable=Price(alpha_vantage_response['currentNetReceivables']),
            current_liabilities = Price(alpha_vantage_response['totalLiabilities']),
        )
        
        return balance_sheet
