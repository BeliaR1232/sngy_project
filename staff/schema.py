import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation


class Query(ObjectType):
    getOccupation = graphene.Field(OccupationType, id=graphene.Int())
    getOccupations = graphene.List(OccupationType)

    def resolve_getOccupation(self, info, id):
        try:
            return Occupation.objects.get(pk=id)
        except Occupation.DoesNotExist:
            return None

    def resolve_getOccupations(self, info):
        return Occupation.objects.all()


class OccupationInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    company_name = graphene.String(required=True)
    position_name = graphene.String(required=True)
    hire_date = graphene.Date(required=True)
    fire_date = graphene.Date()
    salary = graphene.Int(required=True)
    fraction = graphene.Int(required=True)
    base = graphene.Int(required=True)
    advance = graphene.Int(required=True)
    by_hours = graphene.Boolean(required=True)
    

class CreateOccupation(graphene.Mutation):
    class Arguments:
        input = OccupationInput()
    
    ok = graphene.Boolean()
    occupation = graphene.Field(OccupationType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        occupation_instance = Occupation(name = input.name,
                                        company_name = input.company_name,
                                        position_name = input.position_name,
                                        hire_date = input.hire_date,
                                        fire_date = input.fire_date,
                                        salary = input.salary,
                                        fraction = input.fraction,
                                        base = input.base,
                                        advance = input.advance,
                                        by_hours = input.by_hours)
        occupation_instance.save()
        return CreateOccupation(ok=ok, occupation=occupation_instance)
        

class Mutation(graphene.ObjectType):
    add_occupation = CreateOccupation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
