import graphene

import tupleQL.schema

class Query(tupleQL.schema.Query, graphene.ObjectType):
    pass

class Mutation(tupleQL.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
