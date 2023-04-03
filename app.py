from shiny import App, render, ui, reactive
from utils import square


app_ui = ui.page_fluid(
    ui.input_slider("slider_1", "N", 0, 100, 20),
    ui.input_radio_buttons(
        "radio_choice_1", "Columns:", {1: f"1", 2: "2",3: "3",4: "4"}, selected=4
    ),
    ui.output_text_verbatim("text_output_1"),
	ui.output_ui("generated_ui_1")
  
    # ui.output_text_verbatim("banana")
)


def server(input, output, session):
    info = {'name':"pawel",'number':10}
	
    # @reactive.Effect()
    # def some_function():
    #     print("works?")
    #     info['yes'] = f"new {input.radio_choice_columns()} {input.n()}"
    #     return 0
        
	#     # @reactive.Effect()


    @output
    @render.text
    def selector(**kwargs):
        print("kwargs selector",kwargs)
        squared = square(input.n() * int(input.radio_choice()))
        if int(input.radio_choice()) == "2":
            weekday = "today"
        return f"{input.n()} squared is {squared} and {input.radio_choice()} {some_function()}" 
   
    @output
    @render.ui
    def generated_ui_1():
        columns = [
            ui.column(
            	column_width(),
            	ui.div(
                {"class": "app-col"},
                f"{number}:{info}",
            	),
        		)
            for number in range(5)
		]
        row = ui.row(
            columns
		)
        return row

    # @reactive
    def column_width():
        col_width = int(12 / int(input.radio_choice_1()))
        return col_width
  	


app = App(app_ui, server, debug=True)
