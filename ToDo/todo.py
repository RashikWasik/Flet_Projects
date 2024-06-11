import flet as ft

def main(page: ft.Page):

    box = ft.TextField(hint_text="Enter Task", width=300)

    def pidamu(e):    
        page.add(ft.Checkbox(label=box.value))

    page.add(ft.Row([     
        box,
        ft.ElevatedButton(text="Add",on_click=pidamu)
    ]))

ft.app(target=main)
