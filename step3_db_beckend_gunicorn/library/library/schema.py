import graphene
from graphene_django import DjangoObjectType
from todo.models import TodoModel
from users.models import Users


"""GraphQL"""

class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = TodoModel
        fields = '__all__'


class UsersMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    users = graphene.Field(UsersType)

    @classmethod
    def mutate(cls, root, info, birthday_year, id):
        users = Users.objects.get(pk=id)
        users.birthday_year = birthday_year
        users.save()
        return UsersMutation(users=users)


class Mutation(graphene.ObjectType):
    update_users = UsersMutation.Field()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String()

    all_todo = graphene.List(TodoType)
    all_users = graphene.List(UsersType)
    user_by_id = graphene.Field(UsersType, id=graphene.Int(required=True))  # Запросы с параметрами
    todo_by_user_name = graphene.List(TodoType,
                                      first_name=graphene.String(required=False))

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'goodbye!'

    def resolve_all_todo(self, info):
        return TodoModel.objects.all()

    def resolve_all_users(self, info):
        return Users.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExist:
            return None

    def resolve_todo_by_user_name(self, info, first_name=None):
        todo = TodoModel.objects.all()

        if first_name:
            return todo.filter(users__first_name=first_name)
            # try:
            #     return todo.filter(users__first_name=first_name)
            # except TodoModel.DoesNotExist:
            #     # return f'таких todo с именем {first_name} нет в базе данных'
            #     return 'ddd'
        else:
            return todo
            # return f'таких todo с именем {first_name} нет в базе данных'


schema = graphene.Schema(query=Query, mutation=Mutation)

# {
########   пробные

# hello
# goodbye

########   получение даныхх с модели

# allTodo{
#   id
#   todoDescriptions
#   users {
#       id
#       firstName
#       password
# }
# }

########   получение набора связанной модели

#    allUsers{
#     firstName
#     todomodelSet{
#         todoDescriptions
#       	users{
#           id
#         }
#       }
#   }

######## Alias. Иногда нам может потребоваться получить одни и те же данные два раза.

#   usersAgain:allUsers{
#     firstName
#   }

######## Запросы с параметрами

# userById(id: 1){
#   id
#   firstName
#   birthdayYear
# }

#   usersIdAgain:userById(id: 10){
#     firstName
#     id

#   }

######## Фильтрация даных
# 	todoByUserName(firstName:"jek"){
#     todoDescriptions
#   }

#   todoAgain:todoByUserName{
#     todoDescriptions
#   }

######## Изменение данных. Мутации (изменение модели)

# mutation updateUsers {
#   updateUsers(id:1, birthdayYear: 193) {
#     users{
#       id
#       firstName
#       birthdayYear
#     }
#   }
# }


# }
