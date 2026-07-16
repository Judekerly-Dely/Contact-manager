from src.interfaces_adapters.controllers.contact_controller import ContactController
from src.interfaces_adapters.repositories.in_memory_contact_repository import InMemoryContactRepository


class _C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    RED = "\033[31m"

def _banner(text: str):

    print(
        f"\n{_C.BOLD}{_C.CYAN}"
        f"{'='*50}"
        f"{_C.RESET}"
    )

    print(
        f"{_C.BOLD}{_C.CYAN}"
        f"  {text}"
        f"{_C.RESET}"
    )

    print(
        f"{_C.BOLD}{_C.CYAN}"
        f"{'='*50}"
        f"{_C.RESET}\n"
    )

def _ok(message:str):
    print(f"{_C.GREEN} ✓ {message}{_C.RESET}"    )

def _err(message:str):
    print(f"{_C.RED} ✗ {message}{_C.RESET}")

def run_cli():
    repository = InMemoryContactRepository()
    controller = ContactController(repository)
    _banner("Contact Manager")

    print("Commands: add | list | filter | delete | quit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ("quit","exit","q"):
            print("Bye!")
            break

        elif cmd == "add":
            first_name = input("First name : ").strip()
            last_name = input("Last name : ").strip()
            phone = input("Phone : ").strip()
            email = input("Email : ").strip()
            tag = input("Tag : ").strip()
            result = controller.create_contact(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "email": email,
                    "tags":[tag] if tag else []
                })

            if result["success"]:
                _ok(f"Created {result['contact']['first_name']}")
            else:
                _err(result["message"])

        elif cmd == "list":
            result = controller.filter_contact()

            if not result["success"]:
                _err(result["message"])
                continue
            contacts = result["contacts"]

            if not contacts:
                print("(No contacts)")

            else:
                for contact in contacts:
                    print(
                        f"""
                        ID: {contact['id']}
                        Name: {contact['first_name']} {contact['last_name']}
                        Phone: {contact['phone']}
                        Email: {contact.get('email')}
                        Tags: {contact.get('tags')}
                        ----------------------
                        """
                    )

        elif cmd == "filter":
            name = input(
                "Search name : "
            ).strip()

            result = controller.filter_contact(
                {
                    "first_name": name
                }
            )
            for contact in result["contacts"]:

                print(
                    contact
                )

        elif cmd == "delete":

            contact_id = input(
                "Contact ID : "
            ).strip()

            result = controller.delete_contact(
                contact_id
            )

            if result["success"]:

                _ok(result["message"])

            else:

                _err(result["message"])

        else:
            print("Unknown command")