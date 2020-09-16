# sngy_project
Тестовое задание 

1. Создать проект с приложением, в котором описать модель БД со следующими полями:
 
Имя: name (varchar 200)
Компания: company_name (varchar 100)
Должность: position_name (varchar 100)
Дата приёма: hire_date (date)
Дата увольнения: fire_date (date, null)
Ставка, руб.: salary (int)
Ставка, %: fraction (int)
База, руб.: base (int)
Аванс, руб.: advance (int)
Почасовая оплата: by_hours (boolean)

2. Создать слой API с использованием graphene и graphene-django. API должен быть доступен по endpoint’у /api, иметь встроенный web GraphQL-клиент GraphiQL и реализовывать следующую схему:
- тип OccupationType – должен быть связан с моделью Occupation (используя graphene-django).
- запрос getOccupation(occupationId!): OccupationType – должен принимать id модели Occupation и возвращать соответствующий этому id экземпляр модели Occupation из БД.
- запрос getOccupations(): [OccupationType] – должен возвращать список всех имеющихся в БД моделей Occupation.
- мутация addOccupation(
name: String!,
companyName: String!,
positionName: String!,
hireDate: Date!,
fireDate: Date,
salary: Int!,
fraction: Int!,
base: Int!,
advance: Int!,
by_hours: Boolean!
): OccupationType – должна принимать все поля, указанные в модели Occupation, 
создавать новую запись в БД с этими полями, и возвращать новосозданный экземпляр модели в качестве результата.
