import dash_bootstrap_components as dbc
import dash_html_components as html

from system.layouts.pages.info.logbook_handler import LogBook_Handler

lg_handler = LogBook_Handler()

logbook_page = html.Div(
    [html.Div(lg_handler.consume_data("2021-09-22"), id="logbook-div"),
     dbc.Modal(
         [
             dbc.ModalHeader("Logbook", id="logbook-act-modal-header"),
             dbc.ModalBody(
                 "Logbook Description", id="logbook-act-modal-body"
             )
         ],
         id="logbook-act-modal",
         is_open=False,
         backdrop=True,
         size="lg",
         scrollable=False
     ),
     dbc.Modal(
         [
             dbc.ModalHeader("Logbook", id="logbook-stu-modal-header"),
             dbc.ModalBody(
                 "Logbook Description", id="logbook-stu-modal-body"
             )
         ],
         id="logbook-stu-modal",
         is_open=False,
         backdrop=True,
         size="lg",
         scrollable=False
     ),
     dbc.Modal(
         [
             dbc.ModalHeader("Logbook", id="logbook-nut-modal-header"),
             dbc.ModalBody(
                 "Logbook Description", id="logbook-nut-modal-body"
             )
         ],
         id="logbook-nut-modal",
         is_open=False,
         backdrop=True,
         size="lg",
         scrollable=False
     ),
     dbc.Modal(
         [
             dbc.ModalHeader("Logbook", id="logbook-exe-modal-header"),
             dbc.ModalBody(
                 "Logbook Description", id="logbook-exe-modal-body"
             )
         ],
         id="logbook-exe-modal",
         is_open=False,
         backdrop=True,
         size="xl",
         scrollable=False
     )
     ])
