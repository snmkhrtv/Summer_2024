import tkinter as tk
from tkinter import ttk
import folium
import webbrowser
import geopandas as gpd
import matplotlib.pyplot as plt
import os

win = tk.Tk()
win.title('EasyMap')
win.geometry("450x250+500+100")
win.resizable(False, False)
icon = tk.PhotoImage(file='../icon.png')
win.iconphoto(False, icon)

selected_tiles = None
color_style = None
column_name = None
gdf = None


def on_tile_layer_select(event):
    global selected_tiles, tiles_cbx
    selected_tiles = tiles_cbx.get()


def on_location_select(event):
    global sel_loc, zoom, region_cbx, gdf
    if region_cbx.get() == "Россия":
        gdf = gpd.read_file("Russia_regions.geojson")
    elif region_cbx.get() == "Санкт-Петербург":
        gdf = gpd.read_file("../spb_d.geojson")


def on_color_selected(event):
    global color_style, color_cbx
    color_style = color_cbx.get()


def on_pokaz_select(event):
    global column_name, pokaz_cbx
    pokazateli = {"Численность населения":"pop",
                  "Плотность населения":"density"}
    if pokaz_cbx.get() in pokazateli:
        column_name = pokazateli.get(pokaz_cbx.get())
    elif pokaz_cbx.get()=="Районы": column_name = "district"

def save_folium_map():
    global file_name, column_name, selected_tiles, color_style
    m = gdf.explore(column=column_name,
                    tooltip="district",
                    popup=True,
                    tiles=selected_tiles,
                    cmap=color_style,
                    style_kwds=dict(color="black", weight = 1))
    m.save(file_name.get() + '.html')
    new = 2
    url = "file:///" + os.path.realpath(file_name.get() + '.html')
    webbrowser.open(url, new=new)

def save_matplotlib_map():
    global column_name, color_style, file_name, gdf
    path = gdf

    f_name = file_name.get()

    if pokaz_cbx.get() == "Районы":
        m = path.plot(column=column_name, legend=True, cmap=color_style, edgecolor='black', linewidth=0.5,
                      legend_kwds={"title": f_name}
                      ).set_axis_off()
    else:
        m = path.plot(column=column_name, legend=True, cmap=color_style, edgecolor='black', linewidth=0.5,
                      legend_kwds={"label": f_name, "orientation":"horizontal"}
                      ).set_axis_off()


    plt.savefig(file_name.get()+ '.pdf')
    plt.show()


library_choice = tk.StringVar()


def select_library():

    global region_cbx, tiles_cbx, file_name, color_cbx, pokaz_cbx

    library = library_choice.get()
    if library == "Folium":
        region_label = ttk.Label(win, text="Выберите регион")
        region_label.grid(row=2, column=0, padx=15, sticky='e')

        region_cbx = ttk.Combobox(win, values=["Санкт-Петербург", "Россия"])
        region_cbx.grid(row=2, column=1, padx=15, pady=10)
        region_cbx.bind("<<ComboboxSelected>>", on_location_select)

        tile_label = ttk.Label(win, text="Выберите тайлы")
        tile_label.grid(row=3, column=0, padx=15, sticky='e')

        tiles_cbx = ttk.Combobox(win,
                                 values=["Mapbox Bright", "Mapbox Control Room",
                                         "cartodbpositron", "cartodbdark_matter", "openstreetmap"])
        tiles_cbx.grid(row=3, column=1)
        tiles_cbx.bind("<<ComboboxSelected>>", on_tile_layer_select)

        color_label = ttk.Label(win, text="Выберите цветовую шкалу")
        color_label.grid(row=4, column=0, padx=15, pady=10, sticky='e')

        color_cbx = ttk.Combobox(win, values=["OrRd", "PuBu", "Greens", "tab20c"])
        color_cbx.grid(row=4, column=1)
        color_cbx.bind("<<ComboboxSelected>>", on_color_selected)

        tk.Label(win, text='Выберите показатель').grid(row=5, column=0, padx=15, sticky="e")

        pokaz_cbx = ttk.Combobox(win, values=("Численность населения", "Плотность населения", "Районы"))
        pokaz_cbx.grid(row=5, column=1)
        pokaz_cbx.bind("<<ComboboxSelected>>", on_pokaz_select)

        file_label = ttk.Label(win, text="Введите название файла")
        file_label.grid(row=6, column=0, pady=10, sticky="e")

        file_name = tk.Entry(win)
        file_name.grid(row=6, column=1, sticky="ew", pady=10, padx=15)

        save_button = ttk.Button(win, text="Сохранить HTML", command=save_folium_map)
        save_button.grid(row=7, column=0, padx=15)

    elif library == "Matplotlib":
        region_label = ttk.Label(win, text="Выберите регион:")
        region_label.grid(row=2, column=0, padx=15, sticky='e')

        region_cbx = ttk.Combobox(win, values=["Санкт-Петербург", "Россия"])
        region_cbx.grid(row=2, column=1)
        region_cbx.bind("<<ComboboxSelected>>", on_location_select)

        tk.Label(win, text='Выберите показатель').grid(row=3, column=0, padx=15, pady=10, sticky="e")

        pokaz_cbx = ttk.Combobox(win, values=("Численность населения", "Плотность населения", "Районы"))
        pokaz_cbx.grid(row=3, column=1)
        pokaz_cbx.bind("<<ComboboxSelected>>", on_pokaz_select)

        color_label = ttk.Label(win, text="Выберите цветовую шкалу:")
        color_label.grid(row=4, column=0, padx=15, sticky='e')

        color_cbx = ttk.Combobox(win, values=["OrRd", "PuBu", "Greens", "tab20c"])
        color_cbx.grid(row=4, column=1, padx=15)
        color_cbx.bind("<<ComboboxSelected>>", on_color_selected)

        file_label = ttk.Label(win, text="Введите название карты")
        file_label.grid(row=5, column=0, sticky="e", pady=10)

        file_name = tk.Entry(win)
        file_name.grid(row=5, column=1, sticky="ew", padx=15)

        save_button = ttk.Button(win, text="Сохранить в PDF", command=save_matplotlib_map)
        save_button.grid(row=6, column=0)


radio_label = ttk.Label(win, text="Выберите бибилотеку для визуализации")
radio_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

folium_radio = tk.Radiobutton(win, text="Folium", variable=library_choice, value="Folium", command=select_library)
folium_radio.grid(row=1, column=0)

matplotlib_radio = tk.Radiobutton(win, text="Matplotlib",
                                  variable=library_choice, value="Matplotlib", command=select_library)
matplotlib_radio.grid(row=1, column=1)

win.mainloop()