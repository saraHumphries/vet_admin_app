
from repositories import owner_repository, vet_repository
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner


def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select_by_id(row['vet_id'])
        owner = owner_repository.select_by_id(row['owner_id'])
        pet = Pet(row['name'], row['dob'], row['animal_category'], owner, vet, row['notes'], row['id'])
        pets.append(pet)
    return pets

def delete_by_id(id):
    sql = "DELETE FROM pets WHERE id=%s"
    values = [id]
    run_sql(sql, values)