from flask import Flask, render_template, redirect, Blueprint, request
from repositories import owner_repository, vet_repository, pet_respository
from models.pet import Pet

pets_blueprint = Blueprint("pets", __name__)


@pets_blueprint.route('/pets')
def list_pets():
    pets = pet_respository.select_all()
    no_vet_pets = False
    


    return render_template('pets/index.html', pets = pets, no_vet_pets = no_vet_pets)

@pets_blueprint.route('/pets/types/<type>')
def list_by_type(type):
    pets = pet_respository.get_animals_by_type(type)
    no_vet_pets = False
    

    return render_template('pets/index.html', pets = pets, no_vet_pets = no_vet_pets)

@pets_blueprint.route('/pets/novet/list')
def list_novet():
    pets = pet_respository.get_no_vets()
    no_vet_pets = True
    vets = vet_repository.select_all()

    return render_template('pets/index.html', pets = pets, no_vet_pets = no_vet_pets, vets = vets)



@pets_blueprint.route('/pets/<id>')
def show_pet(id):
    print("running")
    pet = pet_respository.select_by_id(id)
    print(pet.name)
    
    return render_template('pets/show.html', pet = pet)


@pets_blueprint.route('/pets/<id>/delete', methods = ['POST'])
def delete_pet(id):
    pet_respository.delete_by_id(id)

    return redirect('/pets')

@pets_blueprint.route('/pets/new')
def new_pet_form():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()

    return render_template('pets/new.html', owners = owners, vets = vets, owner_known = False)

@pets_blueprint.route('/pets/new/owner-id/<owner_id>')
def new_pet_form_owner_known(owner_id):
    owner = owner_repository.select_by_id(owner_id)
    vets = vet_repository.select_all()

    return render_template('pets/new.html', owner = owner, vets = vets, owner_known = True)




@pets_blueprint.route('/pets/new', methods = ['POST'])
def create_pet():
    name = request.form['name']
    dob = request.form['dob']
    animal_category = request.form['animal_category']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    notes = ""
    owner = owner_repository.select_by_id(owner_id)
    vet = vet_repository.select_by_id(vet_id)
    pet = Pet(name, dob, animal_category, owner, vet, notes)
    pet_respository.create(pet)
    pets = owner_repository.get_all_pets(owner_id)

    return render_template('owners/show.html', owner = owner, pets = pets)

@pets_blueprint.route('/pets/<id>/edit')
def edit_form_pet(id):
    pet = pet_respository.select_by_id(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()

    return render_template('pets/edit.html', pet = pet, vets = vets, owners = owners)

@pets_blueprint.route('/pets/<id>', methods = ['POST'])
def update_pet(id):
    name = request.form['name']
    dob = request.form['dob']
    animal_category = request.form['animal_category']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    notes = request.form['notes']
    owner = owner_repository.select_by_id(owner_id)
    vet = vet_repository.select_by_id(vet_id)
    pet = Pet(name, dob, animal_category, owner, vet, notes, id)
    pet_respository.update_pet(pet)
    

    return render_template('pets/show.html', pet=pet)

@pets_blueprint.route('/pets/novet/list', methods = ['POST'])
def reassign_pets():
    vet_id = request.form['vet_id']
    pet_respository.reassign_all_pets(vet_id)
    

    return redirect('/pets')


