import graphene
from graphene_django import DjangoObjectType
from decimal import Decimal

from .models import BalanceSheet

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
    balance_sheet = graphene.Field(BalanceSheetType)

    def resolve_balance_sheet(self, info, **kwargs):
        balance_sheet = BalanceSheet(cash=Decimal(200.0), current_liabilities=round(Decimal(788.9),6))
        # balance_sheet.cash = Decimal(2000.23)
        # balance_sheet.current_liabilities = Decimal(1502.33)
        
        return balance_sheet
