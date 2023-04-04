import graphene

import tupleQL.schema

class Query(tupleQL.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)