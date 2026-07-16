# Contact Manager

A contact management system developed in Python following the principles of Clean Architecture.

## Features

- Create a contact
- Update a contact
- Delete a contact
- Search for a contact
- List all contacts
- Filter contacts using multiple criteria
- Manage contact statuses
- Mark contacts as favorites or professional contacts
- Automatically track creation and modification dates

## Project Structure

The project follows the Clean Architecture pattern.

src/
│
├── entities/
│   ├── contact.py
│   ├── email.py
│   ├── number.py
│   ├── name.py
│   ├── birthday.py
│   └── tag.py
│
├── use_cases/
│   ├── create.py
│   ├── update.py
│   ├── delete.py
│   ├── filter_contact.py
│   └── interfaces/
|       └──contact_repository.py
│
├── interfaces_adapters/
│   ├── controllers/
|   |   └──contact_controller.py
│   ├── presenters/
|   |   └──contact_presenter.py
│   └── repositories/
|       └──in_memory_controller_repository.py
│
├── frameworks/
│   └── cli/
│
└── main_cli.py


## Technologies

- Python 3.11+
- Dataclasses
- Enum
- Typing
- Clean Architecture
