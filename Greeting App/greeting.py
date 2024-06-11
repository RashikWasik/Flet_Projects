import flet as ft

def main(page: ft.Page):

    page.theme_mode = "dark" 
    
    name_1 = ft.TextField(label="Enter first name", width=300, autofocus=True)   # label likhle ekrokom
    name_2 = ft.TextField(hint_text="Enter second name", width=300)   # hint_text likhle arekrokom
   
    def pidamu(e):     
        page.controls.append(ft.Text(f"Hello {name_1.value} {name_2.value} !"))
        name_1.value = ""
        name_2.value = ""
        name_1.focus()    
        page.update()
        
    page.add(ft.Row([     
        name_1,
        name_2,
        ft.ElevatedButton("Hi",on_click=pidamu)   
    ]))

ft.app(target=main)
