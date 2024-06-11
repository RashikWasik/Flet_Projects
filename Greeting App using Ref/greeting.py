import flet as ft

def main(page: ft.Page):

    page.title = "Greetings App"

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = ""
        last_name.current.value = ""
        first_name.current.focus()
        page.update()

    page.add(
        ft.TextField(ref=first_name, label="First Name", width=300, autofocus=True),
        ft.TextField(ref=last_name, label="Last Name", width=300),
        ft.ElevatedButton("Hi", on_click=btn_click),
        ft.Column(ref=greetings) 
    )

ft.app(target=main)
